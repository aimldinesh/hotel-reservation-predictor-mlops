pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "proven-splicer-458605-g2"
    }

    stages {
        stage('Clone GitHub Repository') {
            steps {
                script {
                    echo 'Cloning GitHub Repository...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/aimldinesh/hotel-reservation-predictor-mlops.git'
                        ]]
                    )
                }
            }
        }

        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies...'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Build & Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing Docker image to GCR...'
                        sh '''
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }
    }
}
