pipeline {
   agent {
	    docker {
		    image 'python/python:3.10-alpine'
		}
    }
    stages {
        stage('Hello') {
            steps {

                sh 'uname -a'
                echo 'Hello World'
                
            }
        }
    }
}
