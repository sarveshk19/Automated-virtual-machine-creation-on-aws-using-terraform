# VM Automation with Terraform

## 📋 Project Overview
This project automates the creation of AWS virtual machines (EC2 instances) using Terraform scripts generated from JSON configuration files. It includes Python scripts that read provider and resource configurations and dynamically create `terraform.tf` files for quick provisioning.

## 📁 Project Structure


├── providers.json        # AWS provider configurations
├── resources.json        # AWS instance configurations
├── providers.py          # Python script to generate Terraform provider block
├── resources.py          # Python script to generate Terraform resource block
└── vm_configuration.json # (External) Custom configuration file read by resources.py


## ⚙️ How It Works
- **providers.py**: Reads provider information from `providers.json` and appends provider configurations to `terraform.tf`.
- **resources.py**: Reads VM details (from `vm_configuration.json`) and appends EC2 instance resource definitions to `terraform.tf`.
- The generated `terraform.tf` can be applied with Terraform commands to provision the specified AWS instances.

## 📑 Prerequisites
- Python 3.x
- Terraform installed and configured
- `python-terraform` package (install using `pip install python-terraform`)
- Valid AWS credentials set up (either via environment variables, AWS CLI config, or Terraform secrets management)

## 🚀 Setup & Usage
1. Clone this repository.
2. Ensure `providers.json` and `resources.json` (or `vm_configuration.json`) are updated with your AWS region, AMI, instance type, and other settings.
3. Run:
   bash
   python providers.py
   python resources.py
   
4. Initialize and apply Terraform:
   bash
   terraform init
   terraform apply -auto-approve
   

## 🗂 Example Configuration
### providers.json
json
{
  "aws": {
    "region": "ap-south-1"
  }
}


### resources.json
json
{
  "aws_instance": {
    "my_instance": {
      "ami": "ami-0440d3b780d96b29d",
      "instance_type": "t2.micro",
      "tags": {
        "Name": "new_instance"
      }
    }
  }
}


## ✅ Features
- Automatic Terraform configuration generation
- Easy customization via JSON
- Supports creation of multiple VMs

## 🔎 Future Improvements
- Add error handling and validations
- Support for multiple cloud providers
- CLI-based input support

## 📞 Contact
sarvesh.spk.1909@gmail.com
For questions or feedback, please reach out!

