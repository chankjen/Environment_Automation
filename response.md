# Incident Response Runbook: Application Outage

## Incident Classification
- **Severity**: P1 (Critical)
- **Impact**: All users unable to access application
- **Scope**: Production environment

## Immediate Actions

### 1. Initial Assessment (0-5 minutes)
- [x] Verify incident existence
  ```bash
  curl -I https://production-app.example.com/health