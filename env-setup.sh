# scripts/env-setup.sh
#!/bin/bash

ENV=$1
if [ -z "$ENV" ]; then
  echo "Usage: $0 <environment>"
  exit 1
fi

# Set environment variables
export ENVIRONMENT=$ENV
export TF_VAR_environment=$ENV

# Load environment-specific variables
if [ -f "environments/${ENV}.tfvars" ]; then
  echo "Loading environment variables for $ENV"
else
  echo "Environment file not found: environments/${ENV}.tfvars"
  exit 1
fi

echo "Environment setup complete for $ENV"