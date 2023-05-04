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
                    sh 'pip3 install --user -r App/requirements.txt'
                    sh 'python3 App/manage.py runserver &'
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
                sh 'tar -cvzf artifact.tar.gz App/*'
            }   
        }
        stage('Deploy Infrastructure') {
            steps {
                echo 'Installing Dependancies'
                sh '''
                echo hello
                echo "hello again"
                ls
                '''
            }   
        }
        stage('Configure Infrastructure') {
            steps {
                echo 'Installing Dependancies'
                
            }  
        }
    }
}
