# terraform/main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# VPC Module
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "app-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true
}

# EC2 Instances for different environments
locals {
  environments = {
    dev = { instance_type = "t3.micro", count = 1 }
    staging = { instance_type = "t3.small", count = 2 }
    prod = { instance_type = "t3.medium", count = 3 }
  }
}

resource "aws_instance" "app_servers" {
  for_each = local.environments

  ami           = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS
  instance_type = each.value.instance_type
  count         = each.value.count

  subnet_id              = module.vpc.public_subnets[0]
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  tags = {
    Environment = each.key
    Name        = "app-${each.key}-${count.index + 1}"
  }
}

resource "aws_security_group" "app_sg" {
  name        = "app-sg"
  description = "Application security group"
  vpc_id      = module.vpc.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}