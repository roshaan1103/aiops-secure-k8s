pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/roshaan1103/aiops-secure-k8s.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Fetch Metrics') {
            steps {
                sh '''
                . venv/bin/activate
                python ml/scripts/fetch_metrics.py
                '''
            }
        }

        stage('Anomaly Detection') {
            steps {
                sh '''
                . venv/bin/activate
                python ml/detect_anomalies.py
                '''
            }
        }

        stage('Forecasting') {
            steps {
                sh '''
                . venv/bin/activate
                python ml/forecast_cpu.py
                '''
            }
        }

        stage('Decision Engine') {
            steps {
                sh '''
                . venv/bin/activate
                python ml/decision_engine.py
                cat data/decision.txt
                '''
            }
        }

        stage('K8s Actuation (Controlled)') {
            steps {
                sh '''
                . venv/bin/activate
                python ml/k8s_actuator.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'data/*.csv,data/*.png,data/decision.txt', fingerprint: true
        }
    }
}

