# AutoInfra

AutoInfra is an AI-powered infrastructure-as-code generator. Describe your cloud needs in plain English and AutoInfra generates and deploys Terraform configs for you.

## Features
- AI Terraform file generation
- Automated `plan` and `apply`
- Supports AWS (extendable)
- FastAPI endpoints

## Setup
1. Add your `.env` with OpenAI API key and AWS creds.
2. Install deps: `pip install -r requirements.txt`
3. Run: `uvicorn app.main:app --reload`
