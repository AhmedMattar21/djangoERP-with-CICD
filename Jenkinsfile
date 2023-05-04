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
                sh 'ls'
                sh 'chmod +x scripts/test-1.sh'
                sh './scripts/test-1.sh'
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
