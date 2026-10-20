pipeline {
    agent any
    options { skipDefaultCheckout(true) }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Setup') {
            steps { bat 'python --version' }
        }
        stage('Validate Application') {
            steps { bat 'python scripts/check_app.py' }
        }
        stage('Package Release') {
            steps { bat 'python scripts/build_release.py' }
        }
            stage('Validate Release') {
            steps { bat 'python scripts/check_release.py' }
        }
        stage('Archive Release') {
            steps { archiveArtifacts artifacts: 'dist/*.zip', fingerprint: true }
        }
        stage('Build Metadata') {
            steps {
             bat 'python scripts/write_build_info.py'
                archiveArtifacts artifacts: 'build-info.txt'
            }
        }
    }
}
