properties([pipelineTriggers([pollSCM('30 * * * *')])])
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_FILE_PATH = "C:\\python_ws\\wog_jenkins\\worldofgames"
        CONTAINER_NAME = "flaskwog-container"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout World of Games Repo'
                bat '''
                    cd C:\\python_ws\\wog_jenkins
                    git clone https://github.com/yansab/worldofgames.git
                    cd worldofgames
                    dir
                '''
            }
        }
        stage('Build') {
            steps {
               script {
                    // Use DOCKER_IMAGE_TAG as the tag for the Docker image
                    def image = "flaskwog:${DOCKER_IMAGE_TAG}"

                    // Build the Docker image
                    bat "cd ${DOCKER_FILE_PATH} && docker build -t ${image} ."

                    // Check if the Docker image exists locally
                    def imageBuildFailed = (bat(script: "echo %ERRORLEVEL%", returnStatus: true) != 0)
                    
                     if (imageBuildFailed) {
                          error "Failed to build Docker image."
                    } else {
                          echo "Docker image exists: ${image}"
                    }
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    echo 'Running our docker image expose port 8777'
                    // Define port mapping
                    def portMapping = "8777:5000"

                    // Run the Docker container
                    bat "docker run -d --name ${CONTAINER_NAME} -p ${portMapping} -v ${DOCKER_FILE_PATH}\\scores.txt:/app/scores.txt flaskwog:${DOCKER_IMAGE_TAG}"
               }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing our new container of flaskwog image'
                bat "cd ${DOCKER_FILE_PATH} && C:\\Users\\yaniv\\AppData\\local\\Programs\\Python\\Python39\\python.exe e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                echo 'Terminate our tested container & push new image to Docker Hub'
                bat "docker tag flaskwog:${DOCKER_IMAGE_TAG} yanivsa/flaskwog:${DOCKER_IMAGE_TAG} && docker push yanivsa/flaskwog:${DOCKER_IMAGE_TAG} "
                bat "docker kill ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME} "
            }
        }
    }
}
