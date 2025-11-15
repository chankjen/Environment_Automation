# 🚀 Automating Environments & Deployments, Launch Readiness & Operations

## 📋 Lesson Overview
This comprehensive lesson covers modern DevOps practices for automating software delivery pipelines, ensuring launch readiness, and establishing operational excellence. The curriculum is structured into three core modules with hands-on practical exercises:

### 🎯 Learning Objectives
By completing this lesson, you will master:
- **Infrastructure as Code (IaC)** with Terraform & Ansible
- **CI/CD Pipeline Automation** with GitHub Actions & GitOps
- **Launch Readiness Automation** with comprehensive checklists
- **Operational Excellence** with monitoring, alerting, and incident response
- **Production-grade deployment strategies** (blue-green, canary, feature flags)

---

## 📂 Module Structure

```
lesson-automation/
├── module-1-environments/        # Environment Automation
│   ├── terraform/
│   │   ├── main.tf               # Infrastructure provisioning
│   │   └── environments/         # Environment-specific configs
│   └── ansible/
│       ├── site.yml              # Configuration management
│       └── templates/            # Environment templates
├── module-2-cicd/               # CI/CD Pipeline Automation  
│   ├── src/
│   │   └── app.py                # Sample Flask application
│   ├── .github/workflows/
│   │   └── ci-cd.yml             # GitHub Actions pipeline
│   ├── manifests/                # Kubernetes manifests
│   └── argocd/                   # GitOps configurations
├── module-3-operations/         # Launch Readiness & Operations
│   ├── scripts/
│   │   └── launch-readiness-check.py  # Automated readiness checks
│   ├── monitoring/
│   │   ├── prometheus-config.yaml     # Monitoring configuration
│   │   └── grafana-dashboard.json     # Operations dashboard
│   └── incident-response-runbook.md   # Incident response template
└── capstone-project/            # End-to-end integration project
```

---

## ⚙️ Prerequisites

### Required Tools
- **Python 3.11+** with pip
- **Docker** and **Docker Compose**
- **Terraform v1.5+**
- **Ansible v2.14+**
- **kubectl** (Kubernetes CLI)
- **Git**
- **AWS CLI** (or Azure/Azure CLI for cloud environments)

### Cloud Accounts (Free Tiers Acceptable)
- AWS, Azure, or Google Cloud account
- Docker Hub account
- GitHub account

### Local Setup
```bash
# Install Python dependencies
pip install -r requirements.txt  # Create this file with needed packages

# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y python3-pip git docker.io terraform ansible

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

---

## 🚀 How to Run the Files

### Module 1: Environment Automation

#### 1. Terraform Environment Setup
```bash
cd module-1-environments/terraform

# Initialize Terraform
terraform init

# Create environment-specific variables file
cp environments/example.tfvars environments/dev.tfvars
# Edit dev.tfvars with your configuration

# Plan and apply infrastructure
terraform plan -var-file=environments/dev.tfvars
terraform apply -var-file=environments/dev.tfvars -auto-approve
```

#### 2. Ansible Configuration Management
```bash
cd module-1-environments/ansible

# Test connection to provisioned servers
ansible all -i inventory.ini -m ping

# Run configuration playbook
ansible-playbook -i inventory.ini site.yml --extra-vars "app_env=dev"
```

### Module 2: CI/CD Pipeline (Flask Application)

#### 1. Run Flask Application Locally
```bash
cd module-2-cicd/src

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\activate  # Windows

# Install dependencies
pip install flask requests

# Set environment variables
export ENVIRONMENT=development
export FLASK_APP=app.py
export FLASK_ENV=development

# Run the application
flask run --host=0.0.0.0 --port=5000
```

#### 2. Test the Application
```bash
# In a new terminal
curl http://localhost:5000/
# Expected output: {"environment":"development","message":"Hello from CI/CD Pipeline!","status":"healthy"}

curl http://localhost:5000/health
# Expected output: {"status":"ok"}
```

#### 3. GitHub Actions Pipeline
```bash
# The pipeline runs automatically on GitHub when you push to main branch
# To test locally, you can use act (GitHub Actions runner for local testing)
cd module-2-cicd
act -s DOCKER_USERNAME=yourusername -s DOCKER_PASSWORD=yourpassword
```

### Module 3: Launch Readiness & Operations

#### 1. Launch Readiness Check
```bash
cd module-3-operations/scripts

# Set environment variables for testing
export ENVIRONMENT=staging

# Run the launch readiness check
python launch-readiness-check.py staging
```

#### 2. Monitoring Stack Setup
```bash
cd module-3-operations/monitoring

# Start Prometheus and Grafana with Docker Compose
docker-compose up -d

# Access Grafana dashboard at: http://localhost:3000
# Default credentials: admin/admin
```

---

## 🧪 Expected Outputs

### Flask Application
```json
{
  "environment": "development",
  "message": "Hello from CI/CD Pipeline!",
  "status": "healthy"
}
```

### Launch Readiness Check
```
🚀 Launch Readiness Check for STAGING
============================================================

🔍 Running check: Health Endpoint
  ✅ PASSED: Health endpoint is healthy

🔍 Running check: Database Connection  
  ✅ PASSED: Database connection successful

🔍 Running check: Resource Utilization
  ✅ PASSED: Resources healthy: CPU 45%, Memory 60%

🔍 Running check: Security Scans
  ✅ PASSED: No critical security vulnerabilities found

============================================================
🎯 Final Status: 🟢 ALL CHECKS PASSED
```

### Terraform Apply
```
Apply complete! Resources: 15 added, 0 changed, 0 destroyed.

Outputs:
vpc_id = "vpc-0a1b2c3d4e5f6g7h8"
public_subnet_ids = ["subnet-0a1b2c3d4e5f6g7h8", "subnet-1a2b3c4d5e6f7g8h9"]
```

---

## 🔄 Capstone Project Integration

To run the complete end-to-end system:

```bash
cd capstone-project

# 1. Provision infrastructure
terraform -chdir=infrastructure apply -auto-approve

# 2. Deploy application
kubectl apply -f kubernetes/production/

# 3. Run launch readiness checks
python scripts/launch-readiness-check.py production

# 4. Monitor operations
docker-compose -f monitoring/docker-compose.yml up -d
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

**Flask Application Won't Start:**
```bash
# Check if port is already in use
sudo lsof -i :5000

# Kill process using port 5000
sudo kill -9 $(sudo lsof -t -i:5000)
```

**Terraform Permission Errors:**
```bash
# Configure AWS credentials
aws configure
# or set environment variables
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
```

**Docker Build Failures:**
```bash
# Check Docker daemon status
sudo systemctl status docker

# Clean up Docker resources
docker system prune -f
```

---

## 📚 Next Steps

### Continue Learning
1. **Extend the CI/CD Pipeline**: Add integration tests, performance testing, and security scanning
2. **Implement Feature Flags**: Use LaunchDarkly or Flagsmith for progressive delivery
3. **Add Cost Optimization**: Implement cloud cost monitoring and auto-scaling policies
4. **Create Game Days**: Simulate incidents to test your incident response procedures

### Industry Certifications to Pursue
- **AWS Certified DevOps Engineer**
- **Certified Kubernetes Administrator (CKA)**
- **HashiCorp Certified: Terraform Associate**
- **Google Professional Cloud DevOps Engineer**

### Join Communities
- **DevOps subreddit**: r/devops
- **Kubernetes Slack**: kubernetes.slack.com
- **Terraform Community**: discuss.hashicorp.com
- **CNCF Slack**: cloud-native.slack.com

---

## 🤝 Contributing

This lesson is open source! Contributions are welcome:
1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/your-feature`)
3. **Commit** your changes (`git commit -am 'Add some feature'`)
4. **Push** to the branch (`git push origin feature/your-feature`)
5. **Open** a pull request

## 📄 License

This lesson is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

> **"The only way to go fast is to go well."**  
> — Martin Fowler, Chief Scientist at ThoughtWorks

**Happy Automating!** 🚀✨  
*Last Updated: November 15, 2025*
