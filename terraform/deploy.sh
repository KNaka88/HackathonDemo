#!/bin/bash

# Flight Agent DynamoDB Infrastructure Deployment Script
# This script helps deploy the DynamoDB tables for the Flight Agent application

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."
    
    # Check if terraform is installed
    if ! command -v terraform &> /dev/null; then
        print_error "Terraform is not installed. Please install Terraform first."
        exit 1
    fi
    
    # Check if AWS CLI is installed
    if ! command -v aws &> /dev/null; then
        print_error "AWS CLI is not installed. Please install AWS CLI first."
        exit 1
    fi
    
    # Check AWS credentials
    if ! aws sts get-caller-identity &> /dev/null; then
        print_error "AWS credentials not configured. Please run 'aws configure' first."
        exit 1
    fi
    
    print_success "Prerequisites check passed"
}

# Function to initialize Terraform
init_terraform() {
    print_status "Initializing Terraform..."
    terraform init
    print_success "Terraform initialized"
}

# Function to validate Terraform configuration
validate_terraform() {
    print_status "Validating Terraform configuration..."
    terraform validate
    terraform fmt -check=true
    print_success "Terraform configuration is valid"
}

# Function to plan deployment
plan_deployment() {
    print_status "Planning deployment..."
    terraform plan -out=tfplan
    print_success "Deployment plan created"
}

# Function to apply deployment
apply_deployment() {
    print_status "Applying deployment..."
    terraform apply tfplan
    print_success "Deployment completed successfully"
}

# Function to show outputs
show_outputs() {
    print_status "Deployment outputs:"
    terraform output
}

# Function to check if tfvars file exists
check_tfvars() {
    if [ ! -f "terraform.tfvars" ]; then
        print_warning "terraform.tfvars file not found"
        print_status "Creating terraform.tfvars from example..."
        
        if [ -f "terraform.tfvars.example" ]; then
            cp terraform.tfvars.example terraform.tfvars
            print_warning "Please edit terraform.tfvars with your configuration before proceeding"
            print_status "Opening terraform.tfvars for editing..."
            ${EDITOR:-nano} terraform.tfvars
        else
            print_error "terraform.tfvars.example not found"
            exit 1
        fi
    fi
}

# Function to display help
show_help() {
    echo "Flight Agent DynamoDB Infrastructure Deployment Script"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  deploy    - Full deployment (init, validate, plan, apply)"
    echo "  init      - Initialize Terraform"
    echo "  validate  - Validate Terraform configuration"
    echo "  plan      - Plan deployment"
    echo "  apply     - Apply deployment"
    echo "  destroy   - Destroy infrastructure"
    echo "  output    - Show deployment outputs"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 deploy     # Full deployment"
    echo "  $0 plan       # Just plan"
    echo "  $0 destroy    # Destroy everything"
}

# Function to destroy infrastructure
destroy_infrastructure() {
    print_warning "This will destroy all DynamoDB tables and data!"
    read -p "Are you sure you want to continue? (yes/no): " confirm
    
    if [ "$confirm" = "yes" ]; then
        print_status "Destroying infrastructure..."
        terraform destroy -auto-approve
        print_success "Infrastructure destroyed"
    else
        print_status "Destruction cancelled"
    fi
}

# Main script logic
main() {
    case "${1:-deploy}" in
        "deploy")
            check_prerequisites
            check_tfvars
            init_terraform
            validate_terraform
            plan_deployment
            
            print_warning "Review the plan above carefully"
            read -p "Do you want to apply this plan? (yes/no): " confirm
            
            if [ "$confirm" = "yes" ]; then
                apply_deployment
                show_outputs
            else
                print_status "Deployment cancelled"
            fi
            ;;
        "init")
            check_prerequisites
            init_terraform
            ;;
        "validate")
            check_prerequisites
            validate_terraform
            ;;
        "plan")
            check_prerequisites
            check_tfvars
            init_terraform
            validate_terraform
            plan_deployment
            ;;
        "apply")
            check_prerequisites
            apply_deployment
            show_outputs
            ;;
        "destroy")
            check_prerequisites
            destroy_infrastructure
            ;;
        "output")
            terraform output
            ;;
        "help"|"-h"|"--help")
            show_help
            ;;
        *)
            print_error "Unknown command: $1"
            show_help
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
