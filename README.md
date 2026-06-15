# VectorOps CI/CD Pipeline

A DevSecOps portfolio project demonstrating Azure DevOps CI/CD for a Python application with automated linting, unit testing, security scanning, and dependency vulnerability scanning.

## Project Purpose

This project was built as part of the VectorOps LLC DevSecOps learning roadmap. The goal is to demonstrate how a secure CI/CD pipeline can automatically validate code quality, run tests, and scan for security issues before changes are accepted.

No work, government, client, or sensitive data is used in this project.

## What This Project Demonstrates

* Azure DevOps Pipelines
* Azure Repos
* GitHub portfolio publishing
* Python application structure
* Automated unit testing with Pytest
* Code linting with Ruff
* Python security scanning with Bandit
* Dependency vulnerability scanning with pip-audit
* YAML-based pipeline configuration
* DevSecOps workflow documentation

## Pipeline Flow

```text
Code Commit
    ↓
Azure DevOps Pipeline
    ↓
Install Dependencies
    ↓
Ruff Linting
    ↓
Pytest Unit Tests
    ↓
Bandit Security Scan
    ↓
pip-audit Dependency Scan
    ↓
Application Execution
    ↓
Pipeline Pass / Fail
```

## Tools Used

| Tool         | Purpose                                             |
| ------------ | --------------------------------------------------- |
| Azure DevOps | Runs the CI/CD pipeline                             |
| Azure Repos  | Stores the working pipeline code                    |
| GitHub       | Hosts the public portfolio version                  |
| Python       | Application language                                |
| Ruff         | Checks code quality and formatting                  |
| Pytest       | Runs automated unit tests                           |
| Bandit       | Scans Python code for security issues               |
| pip-audit    | Scans Python dependencies for known vulnerabilities |
| YAML         | Defines the Azure DevOps pipeline                   |

## Project Structure

```text
vectorops-secure-pipeline/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── azure-pipelines.yml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/VectorOps77/vectorops-cicd-pipeline.git
cd vectorops-cicd-pipeline
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the application:

```bash
python3 app/main.py
```

Run unit tests:

```bash
python3 -m pytest
```

Run linting:

```bash
python3 -m ruff check .
```

Run Python security scanning:

```bash
python3 -m bandit -r app
```

Run dependency vulnerability scanning:

```bash
python3 -m pip_audit
```

## Security Notes

This project intentionally avoids storing secrets, credentials, API keys, environment files, or client data in the repository.

The pipeline includes automated checks to support secure development practices, including static code scanning and dependency vulnerability scanning.

## Portfolio Statement

I built a CI/CD pipeline with automated testing, dependency scanning, security scanning, and build validation using Azure DevOps and Python.

## Current Status

Initial DevSecOps pipeline completed.

## Future Enhancements

* Add GitHub Actions mirror workflow
* Add secret scanning with Gitleaks
* Add SonarCloud code quality scanning
* Add branch protection rules
* Add pull request validation
* Add deployment stage to Azure App Service
* Add Docker build and Trivy image scanning in a future container phase

## Learning Outcome

This project helped me understand how DevSecOps pipelines automate code quality, testing, and security validation.

## Disclaimer

This is a fictional portfolio project created for DevSecOps learning and demonstration purposes. No work, government, client, or sensitive data is included.
