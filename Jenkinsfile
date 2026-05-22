pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest pytest-html selenium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --html=report.html
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Automation Test Report'
                ])
            }
        }
    }
}
