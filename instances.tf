resource "aws_instance" "amb-dev" {
  count = 3
  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  key_name = "curso-terraform"

  tags = {
    Name = "amb-dev-${count.index}"
  }
}