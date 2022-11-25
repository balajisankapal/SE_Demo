pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/balajisankapal/SE_Demo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x function.py"
                sh "./function.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
