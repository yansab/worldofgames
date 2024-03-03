properties([pipelineTriggers([pollSCM('30 * * * *')])])
pipeline {
    agent any

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
                echo 'Build our application as Image Docker'
                bat 'docker build -t flaskwog:1.0.4 . '
            }
        }
        stage('Run') {
            steps {
                echo 'Running our docker image expose port 8777'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing our score web page and fail the pipline in case its failed'
//                 bat 'C:\\Users\\yaniv\\AppData\\Local\\Programs\\Python\\Python39\\python.exe e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                echo 'Terminate our tested container & push new image to Docker Hub'
            }
        }
    }
}
