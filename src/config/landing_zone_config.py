from dataclasses import dataclass
from typing import Dict, List

@dataclass
class LandingZoneConfig:
    organization_name: str = "enterprise"
    root_email: str = "root@company.com"
    
    # Account structure
    core_accounts: Dict[str, str] = None  # Shared infrastructure
    security_accounts: Dict[str, str] = None  # Security services
    workload_accounts: Dict[str, str] = None
    
    # Security settings
    enable_guardduty: bool = True
    enable_security_hub: bool = True
    enable_config: bool = True
    
    # Network settings
    transit_gateway_asn: int = 64512
    vpc_cidr_blocks: Dict[str, str] = None
    
    def __post_init__(self):
        if self.core_accounts is None:
            self.core_accounts = {
                "shared-services": "shared@company.com",  # Network hub
                "dns": "dns@company.com"  # Centralized DNS
            }
            
        if self.security_accounts is None:
            self.security_accounts = {
                "security": "security@company.com",
                "log-archive": "logs@company.com", 
                "audit": "audit@company.com"
            }
        
        if self.workload_accounts is None:
            self.workload_accounts = {
                "dev": "dev@company.com",
                "staging": "staging@company.com",
                "prod": "prod@company.com"
            }
            
        if self.vpc_cidr_blocks is None:
            self.vpc_cidr_blocks = {
                "shared": "10.0.0.0/16",
                "dev": "10.1.0.0/16",
                "staging": "10.2.0.0/16", 
                "prod": "10.3.0.0/16"
            }