pipeline {
   agent {
	    docker {
		    image 'python:3.10-alpine'
		}
    }
    stages {
        stage('Build') {
            steps {
               //  Change the home dir cus jenkins has no permissions 
               //   on the server's home dir.
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user -r requirements.txt'
                    sh 'python3 manage.py runserver &'
                }
            }   
        }
        stage('Test') {
            steps {
                echo 'Installing Dependancies'
                sh '''
                    sudo apk update
                    sudo apk add curl
                    '''
                echo 'Running Test 1'
                sh '''
                    #!/bin/bash
                    if curl -I "http://127.0.0.1:8000" | grep -i "OK"
                    then
                        exit 0
                    else
                        exit 1
                    fi
                    '''
            }   
        }
        stage('Archive') {
            steps {
                echo 'Running Test 1'
                echo 'Running Test 2'
                echo 'Running Test 3'
            }   
        }
    }
}
