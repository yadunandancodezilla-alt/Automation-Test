
pipeline {
    agent any

    stages {

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
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Automation Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
    }
}
