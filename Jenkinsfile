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
                echo 'archiving the app'
                //sh 'tar -czf artifact.tar.gz App/*'
            }   
        }
        stage('Deploy Infrastructure') {
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                 credentialsId: 'jenkins-awscli', 
                 screteKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                 )]){
                    
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh './create-stack.sh dj-${BUILD_NUMBER} scripts/infrastructure.yml scripts/infra-parameters.json'
                }

                 }
            }   
        }
        stage('Configure Infrastructure') {
            steps {
                echo 'Installing Dependancies'
                
            }  
        }
    }
}
