pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '1. Building..'
            }
        }
        stage('Test') {
            environment {
                TESTING_STRING = 'AWS Workshop'
            }
            steps {
                echo '2. Testing..'
                sh 'grep -Fq "$TESTING_STRING" index.html'
            }
        }
        stage('Deploy') {
            environment {
                S3_BUCKET = 's3://s3.belajar-aws.cloud'
            }
            steps {
                echo '4. Deploying....'
                sh 'aws s3 cp . $S3_BUCKET --recursive'
            }
        }
    }
}