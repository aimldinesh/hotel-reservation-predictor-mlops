pipeline{
    agent any

    stages{
        stage('Cloning Github Repositories to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github Repositories to Jenkins.............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/aimldinesh/hotel-reservation-predictor-mlops.git']])
                }
            }
        }
    }
}