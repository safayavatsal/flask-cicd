pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "flask-app"               // Docker image name
        DOCKER_REGISTRY = "your-docker-registry"       // Replace with your Docker registry, e.g., 'docker.io', 'AWS_ECR'
        DOCKER_CREDENTIALS = "docker-credentials-id"   // Jenkins credentials ID for Docker Registry (DockerHub, AWS, etc.)
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Pull the repository containing your app
                git 'https://your-repository-url.git'  // Replace with your Git repository URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the provided Dockerfile
                    docker.build("${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:latest")
                }
            }
        }

        stage('Login to Docker Registry') {
            steps {
                script {
                    // Login to Docker Registry (DockerHub, AWS ECR, etc.)
                    docker.withRegistry('https://${DOCKER_REGISTRY}', "${DOCKER_CREDENTIALS}") {
                        echo "Logged in to Docker Registry"
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to the registry
                    docker.withRegistry('https://${DOCKER_REGISTRY}', "${DOCKER_CREDENTIALS}") {
                        docker.image("${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:latest").push()
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Deploy the Flask and Redis containers using Docker Compose
                    echo "Deploying Flask app with Redis using Docker Compose"
                    sh '''
                    docker-compose -f docker-compose.yml up -d
                    '''
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Optional: Clean up any stopped containers or unused images
                    echo "Cleaning up unused containers and images"
                    sh '''
                    docker-compose -f docker-compose.yml down
                    docker system prune -f
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'The pipeline has completed successfully.'
        }

        failure {
            echo 'The pipeline has failed.'
        }

        always {
            echo 'This will always run, regardless of success or failure.'
        }
    }
}
