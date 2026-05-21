pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/yadunandancodezilla-alt/Automation-Test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate 
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --html=report.html --self-contained-html
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}