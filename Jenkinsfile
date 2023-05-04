pipeline {
   agent {
	    docker {
		    image 'm4tt4r/python3-ubuntu'
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
                echo 'Running Test 1'
            }   
        }
        stage('Archive') {
            steps {
                sh 'tar -cvzf artifact.tar.gz .'
            }   
        }
    }
}
