# VM Automation with Terraform

## 📋 Project Overview
This repository automates the creation of AWS virtual machines (EC2 instances) using dynamically generated Terraform configurations. Python scripts parse provider and resource configurations from JSON files and generate a `terraform.tf` file, making VM deployment seamless.

## 📁 Repository Structure


├── providers.json        # AWS provider configurations
├── resources.json        # AWS instance configuration template
├── providers.py          # Python script to generate Terraform provider configuration
├── resources.py          # Python script to generate Terraform resource definitions
└── vm_configuration.json # (External) custom configuration for resource creation

## ⚙️ How It Works
- **providers.py**: Reads from `providers.json` and writes provider details into `terraform.tf`.
- **resources.py**: Reads VM configurations (from `vm_configuration.json`) and appends AWS EC2 instance resources to `terraform.tf`.
- The generated Terraform configuration file can then be used for provisioning with Terraform.

## ✅ Prerequisites
- Python 3.x
- Terraform installed
- Install Python dependencies:
  bash
  pip install python-terraform
  
- AWS CLI configured or environment variables set for access keys.

## 🚀 How to Use
1. Clone this repository:
   bash
   git clone <your-repo-url>
   cd <repo-folder>
   
2. Update `providers.json` and `vm_configuration.json` with your AWS region and VM specifications.
3. Run the Python scripts to generate the Terraform configuration:
   bash
   python providers.py
   python resources.py
   
4. Initialize and apply Terraform:
   bash
   terraform init
   terraform apply -auto-approve
   

## 📑 Example Configurations
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


## 🔎 Future Enhancements
- Add dynamic input via CLI
- Support additional cloud providers
- Integrate testing for configuration files

## 📬 Contributing
Pull requests are welcome! For significant changes, please open an issue first to discuss what you would like to change.

📞 License
This project is licensed under the MIT License — feel free to use and modify it.

