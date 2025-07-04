# app/generator.py

import openai
import os

openai.api_key = os.getenv(\"OPENAI_API_KEY\")

def generate_terraform_code(prompt=\"Create a VPC with 2 public subnets and an EC2 instance.\"):
    system_prompt = \"\"\"You are an expert DevOps engineer. Generate valid Terraform code based on user instructions. Include providers, resources, and outputs.\"\"\"
    
    response = openai.ChatCompletion.create(
        model=\"gpt-4o\",
        messages=[
            {\"role\": \"system\", \"content\": system_prompt},
            {\"role\": \"user\", \"content\": prompt}
        ]
    )
    
    terraform_code = response.choices[0].message.content
    with open(\"generated_infra.tf\", \"w\") as f:
        f.write(terraform_code)
    return terraform_code

if __name__ == \"__main__\":
    tf_code = generate_terraform_code(\"Set up a VPC, 2 public subnets, and an EC2 instance in us-east-1.\")
    print(\"Generated Terraform:\\n\", tf_code)
