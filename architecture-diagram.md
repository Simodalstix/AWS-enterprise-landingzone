# AWS Enterprise Landing Zone Architecture Diagram

## Layout Structure (Top to Bottom)

### 1. Management Account (Root)
**Position**: Top center
**Components**:
- AWS Organizations icon
- CloudTrail (organization-wide)
- Budgets
- Service Control Policies (SCPs)

### 2. Organizational Units Layer
**Position**: Below Management Account
**Layout**: Four columns

#### Core OU (Left Column)
- Shared Services Account
  - VPC (10.0.0.0/16)
  - Transit Gateway (hub)
  - NAT Gateway
  - AWS RAM (resource sharing)
- DNS Account
  - Route 53 Resolver
  - Centralized DNS management

#### Security OU (Center-Left Column)
- Security Account
  - GuardDuty (master)
  - Security Hub (master)
  - Config (aggregator)
- Log Archive Account
  - S3 bucket (CloudTrail logs)
- Audit Account
  - Cross-account roles

#### Workloads OU (Center-Right Column)  
- Dev Account
  - VPC (10.1.0.0/16)
  - Private subnets
- Staging Account
  - VPC (10.2.0.0/16)
  - Private subnets
- Prod Account
  - VPC (10.3.0.0/16)
  - Public + Private + DB subnets

#### Sandbox OU (Right Column)
- Individual developer accounts
- Temporary workloads
- Experimentation environments

### 3. Networking Layer
**Position**: Bottom section
**Components**:
- Transit Gateway (center hub)
- VPC attachments (spokes to each account VPC)
- Route tables (Shared RT, Workload RT)

## Connection Lines

### Governance Flows
- Management Account → All OUs (SCPs)
- Security Account → All accounts (GuardDuty, Security Hub)
- Log Archive ← All accounts (CloudTrail)

### Network Flows
- Transit Gateway ↔ All VPCs (via RAM sharing)
- Shared Services VPC → Internet Gateway
- Workload VPCs → NAT Gateway (in Shared Services)
- RAM shares Transit Gateway to all OUs

### Cross-Account Access
- Audit Account → All accounts (read-only roles)
- Security Account → All accounts (security roles)

## AWS Icons Needed

### Core Services
- AWS Organizations
- AWS Accounts (multiple)
- VPC
- Transit Gateway
- Subnets (Public/Private/DB)

### Security
- GuardDuty
- Security Hub
- AWS Config
- CloudTrail
- KMS
- IAM

### Networking
- Route 53
- Internet Gateway
- NAT Gateway
- Security Groups

### Management
- CloudWatch
- Budgets
- S3

## Color Coding
- **Core OU**: Orange theme (infrastructure)
- **Security OU**: Red theme (security services)
- **Workloads OU**: Blue theme (applications)
- **Sandbox OU**: Green theme (experimentation)
- **Management Account**: Purple theme
- **Network connections**: Gray lines
- **Security flows**: Red dashed lines
- **RAM sharing**: Orange dashed lines

## Labels
- Account names with email domains
- CIDR blocks for each VPC
- Service names under each icon
- OU names as section headers