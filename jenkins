pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Turtlemonk473/django_assignment.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Server') {
            steps {
                sh 'python manage.py migrate'
                sh 'nohup python manage.py runserver 0.0.0.0:8000 &'
            }
        }
    }
}
