# CI/CD Pipeline for Flask Application

## Overview
This project sets up a CI/CD pipeline for a simple Python Flask web application using both Jenkins and GitHub Actions. The pipeline automates building, testing, and deploying the application.

## Features
- Jenkins CI/CD Pipeline
- GitHub Actions CI/CD Workflow
- Dockerized Flask Application
- Automated Testing with Pytest
- Docker Image Management
- Deployment using Docker Compose
- Redis Integration

---

## 1. Jenkins CI/CD Pipeline
### Objective
To automate the testing, building, and deployment of the Flask application using Jenkins.

### Pipeline Stages
1. **Clone Repository** - Pulls the source code from GitHub.
2. **Install Dependencies** - Installs required Python packages.
3. **Run Tests** - Runs unit tests using Pytest.
4. **Build Docker Image** - Builds a Docker image of the Flask app.
5. **Login to Docker Registry** - Authenticates with DockerHub or another registry.
6. **Push Docker Image** - Pushes the built image to a registry.
7. **Deploy Application** - Uses Docker Compose to run the Flask and Redis services.
8. **Cleanup** - Removes unused Docker resources.

### Jenkins Setup
1. Install Jenkins and required plugins (e.g., Docker Pipeline, GitHub Integration).
2. Add credentials for GitHub and DockerHub.
3. Create a new Jenkins pipeline and use the provided `Jenkinsfile`.

### Jenkinsfile
Refer to the [`Jenkinsfile`](Jenkinsfile) for detailed pipeline configuration.

---

## 2. GitHub Actions CI/CD Pipeline
### Objective
To set up an automated workflow for building, testing, and deploying the Flask app using GitHub Actions.

### Workflow Steps
1. **Checkout Code** - Fetches the latest code from the repository.
2. **Set Up Python** - Installs Python 3.10.
3. **Install Dependencies** - Installs Python packages.
4. **Run Tests** - Executes unit tests using Pytest.
5. **Build Docker Image** - Builds the Flask app Docker image.
6. **Login to DockerHub** - Authenticates with DockerHub.
7. **Push Docker Image** - Uploads the Docker image to DockerHub.
8. **Cleanup** - Removes unused Docker resources.

### GitHub Actions Setup
1. Store DockerHub credentials as GitHub Secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).
2. Push changes to the repository, triggering the workflow.

### Workflow File
Refer to the [`.github/workflows/ci.yml`](.github/workflows/ci.yml) for detailed configuration.

---

## 3. Running the Application Locally
### Prerequisites
- Install [Docker](https://docs.docker.com/get-docker/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)
- Clone the repository:
  ```sh
  git clone https://github.com/your-repository.git
  cd your-repository
  ```

### Run Using Docker Compose
```sh
docker-compose up -d
```
Access the Flask app at: [http://localhost:5000](http://localhost:5000)

---

## 4. Project Structure
```
├── Dockerfile
├── Jenkinsfile
├── app.py
├── docker-compose.yml
├── requirements.txt
├── test.py
├── .github/workflows/ci.yml
├──.github/actions/actions.yml
```

- `Dockerfile` - Defines how to containerize the Flask app.
- `Jenkinsfile` - Defines the Jenkins pipeline.
- `app.py` - The Flask application.
- `docker-compose.yml` - Manages multi-container setup.
- `requirements.txt` - Lists dependencies.
- `test.py` - Pytest unit tests.
- `.github/workflows/ci.yml` - GitHub Actions CI/CD workflow.

---

## 5. Testing
To run tests locally, execute:
```sh
pytest test.py
```

---

## 6. Deployment
### Using Jenkins
- Jenkins triggers the deployment after a successful pipeline run.

### Using GitHub Actions
- Merges to the `jenkins` branch trigger a new build and deployment.

---

## 7. Contributors
- [@safayavatsal]

---
