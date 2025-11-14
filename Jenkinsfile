pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = "8838036650/python-app"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Vijayalakshmi1608/python-jenkins-docker-integration'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {

                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${DOCKER_HUB_REPO}:${IMAGE_TAG} .
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                    docker push ${DOCKER_HUB_REPO}:${IMAGE_TAG}
                """
            }
        }

        stage('Deploy to Local Server') {
            steps {
                sh """
                    # Stop old container if running
                    docker rm -f python-app || true

                    # Pull latest image
                    docker pull ${DOCKER_HUB_REPO}:${IMAGE_TAG}

                    # Run new container
                    docker run -d --name python-app -p 8100:8100 ${DOCKER_HUB_REPO}:${IMAGE_TAG}
                """
            }
        }
    }
}
