pipeline {
    agent any 
        stages {

            stage('Checkout code') {
                steps {
                    git credentialsId: 'MY_PAT', url: "https://github.com/gayathri7022/Exam4.git", branch: "main"
                }
            }

            stage('Install dependencies') {
                steps {
                    bat '''
                        "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                        call .\\venv\\Scripts\\activate
                        pip install -upgrade pip
                        pip install pytest
                    '''
                }
            }

            stage ('Test') {
                steps {
                    bat '''
                        call .\\venv\\Scripts\\activate
                        pytest test.py
                    '''
                }
            }

            stage('Deploy') {
                steps {
                    bat '''
                        call .\\venv\\Scripts\\activate
                        "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" C:\\Users\\mjmnj\\OneDrive\\Documents\\SEPP\\Exam4\\Library.py
                    '''
                }
            }

        }

        post {
            success {
                echo 'pipeline succeded'
            }
            failure {
                echo 'pipeline failed'
             }
        }
}