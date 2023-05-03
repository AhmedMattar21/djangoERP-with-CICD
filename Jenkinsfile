pipeline {
   agent {
	    docker {
		    image 'python:3.10-alpine'
		}
    }
    stages {
        stage('Hello') {
            steps {

                sh 'python3 --version'
                echo 'Hello python'
                
            }
        }
    }
}
