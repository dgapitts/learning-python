#chatgpt question : how about using python templates to inject variables (context hcl)

from string import Template

# Define the template string
hcl_template = Template('''
resource "aws_instance" "$resource_name" {
  ami           = "$ami"
  instance_type = "$instance_type"

  tags {
    Name = "$tag_name"
  }
}
''')

# Define the variables to inject
variables = {
    "resource_name": "example",
    "ami": "ami-0c55b159cbfafe1f0",
    "instance_type": "t2.micro",
    "tag_name": "example-instance"
}

# Substitute variables into the template
hcl_content = hcl_template.substitute(variables)

# Write the HCL content to a file
with open("example.tf", "w") as file:
    file.write(hcl_content)


