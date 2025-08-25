# AWS Enterprise Landing Zone

Production-ready AWS Landing Zone using CDK with enterprise organizational structure, governance, and security baseline.

## Architecture

### Organizational Structure
- **Core Accounts**: Security, Log Archive, Audit, Shared Services
- **Workload Accounts**: Dev, Staging, Production
- **OUs**: Security OU, Workloads OU, Sandbox OU

### Security Baseline
- GuardDuty threat detection
- Security Hub centralized findings
- Config rules for compliance
- KMS centralized key management
- Cross-account IAM roles

### Networking Foundation
- Transit Gateway hub-and-spoke model
- Standardized VPC templates
- Network segmentation and security groups

### Governance & Compliance
- Service Control Policies (SCPs)
- Organization-wide CloudTrail
- Budget controls and monitoring
- Automated compliance checking

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Deploy landing zone
cdk bootstrap
cdk deploy --all
```

## Project Structure

```
src/
├── constructs/
│   ├── account/          # Account factory, baseline setup
│   ├── governance/       # SCPs, Config rules, compliance
│   ├── security/         # GuardDuty, Security Hub, IAM
│   ├── networking/       # Transit Gateway, VPC patterns
│   └── monitoring/       # Cross-account observability
├── stacks/
│   ├── core_stack.py     # Organization setup, root account
│   ├── security_stack.py # Security services and baselines
│   ├── network_stack.py  # Networking foundation
│   └── workload_stack.py # Account provisioning
├── config/
│   └── landing_zone_config.py  # Environment configurations
└── utils/
    └── account_utils.py  # Account management utilities
```

## Key Features

- **Single Responsibility**: Each construct handles one specific concern
- **Modularity**: Reusable constructs for common patterns
- **Security First**: Multi-layered security with centralized management
- **Compliance Ready**: Automated governance and monitoring
- **Scalable**: Hub-and-spoke networking with proper segmentation

## Configuration

Modify `src/config/landing_zone_config.py` to customize:
- Account structure and emails
- Network CIDR blocks
- Security settings
- Organizational units

## Deployment Order

1. Core Stack - Organization and accounts
2. Security Stack - Security baseline
3. Network Stack - Transit Gateway and shared VPC
4. Workload Stack - Environment VPCs