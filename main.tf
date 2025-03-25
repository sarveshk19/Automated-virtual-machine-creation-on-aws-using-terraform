provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "my_instance" {
  ami           = "ami-0e731c8a588258d0d"
  instance_type = "t2.micro"
  count = "3"
  tags = {
    "Name" = "MyEC2instanc"
  }
 
}