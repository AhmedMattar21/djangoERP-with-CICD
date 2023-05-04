pipeline {
   agent {
	    docker {
		    image 'python:3.10-alpine'
		}
    }
    stages {
        stage('Build') {
            steps {
                sh 'sudo pip3 install -r requirements.txt '
                sh 'python3 manage.py runserver'
            }   
        }
        stage('Test') {
            steps {
                echo 'Running Test 1'
                echo 'Running Test 2'
                echo 'Running Test 3'
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
