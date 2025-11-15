# scripts/launch-readiness-check.py
import sys
import requests
import json
from datetime import datetime

class LaunchReadinessChecker:
    def __init__(self, environment):
        self.environment = environment
        self.checks = []
        self.results = {}

    def add_check(self, name, function):
        self.checks.append({'name': name, 'function': function})

    def run_all_checks(self):
        print(f"🚀 Launch Readiness Check for {self.environment.upper()}")
        print("=" * 60)
        
        all_passed = True
        
        for check in self.checks:
            print(f"\n🔍 Running check: {check['name']}")
            try:
                result = check['function']()
                self.results[check['name']] = result
                status = "✅ PASSED" if result['passed'] else "❌ FAILED"
                print(f"  {status}: {result['message']}")
                
                if not result['passed']:
                    all_passed = False
            except Exception as e:
                print(f"  ❌ ERROR: {str(e)}")
                all_passed = False
        
        print("\n" + "=" * 60)
        final_status = "🟢 ALL CHECKS PASSED" if all_passed else "🔴 SOME CHECKS FAILED"
        print(f"🎯 Final Status: {final_status}")
        
        return all_passed

# Example check functions
def check_health_endpoint():
    try:
        response = requests.get(f"https://{env}-app.example.com/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'ok':
                return {'passed': True, 'message': 'Health endpoint is healthy'}
        return {'passed': False, 'message': f'Health endpoint returned {response.status_code}'}
    except Exception as e:
        return {'passed': False, 'message': f'Health check failed: {str(e)}'}

def check_database_connection():
    # Implementation would connect to database
    return {'passed': True, 'message': 'Database connection successful'}

def check_resource_utilization():
    # Mock implementation - would check actual resource usage
    cpu_usage = 45  # %
    memory_usage = 60  # %
    
    if cpu_usage < 80 and memory_usage < 85:
        return {'passed': True, 'message': f'Resources healthy: CPU {cpu_usage}%, Memory {memory_usage}%'}
    else:
        return {'passed': False, 'message': f'High resource usage: CPU {cpu_usage}%, Memory {memory_usage}%'}

def check_security_scans():
    # Mock implementation - would check actual security scan results
    return {'passed': True, 'message': 'No critical security vulnerabilities found'}

if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 1 else "staging"
    
    checker = LaunchReadinessChecker(env)
    
    # Add all readiness checks
    checker.add_check("Health Endpoint", check_health_endpoint)
    checker.add_check("Database Connection", check_database_connection)
    checker.add_check("Resource Utilization", check_resource_utilization)
    checker.add_check("Security Scans", check_security_scans)
    
    # Run all checks
    success = checker.run_all_checks()
    
    sys.exit(0 if success else 1)