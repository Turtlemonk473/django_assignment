pipeline {
    agent any
    environment {
        VENV_DIR = '.venv'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Turtlemonk473/django_assignment.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Server') {
            steps {
                sh './$VENV_DIR/bin/python manage.py migrate'
                sh 'nohup ./$VENV_DIR/bin/python manage.py runserver 0.0.0.0:8000 &'
            }
        }
    }
}
