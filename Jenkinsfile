pipeline {
    agent {
        docker {
            image 'python:3.10' // Or any appropriate version
            args '-u root'      // Optional: to run as root if needed
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Turtlemonk473/django_assignment.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
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
