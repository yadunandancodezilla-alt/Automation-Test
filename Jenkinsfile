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
 
