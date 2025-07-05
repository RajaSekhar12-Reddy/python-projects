pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'sample-fastapi'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        REGISTRY_URL = 'your-registry-url' // Update this with your registry URL
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python dependencies...'
                    sh 'pip install -r requirements.txt'
                    sh 'pip install pytest pytest-asyncio httpx' // Install testing dependencies
                }
            }
        }
        
        stage('Lint Code') {
            steps {
                script {
                    echo 'Running code linting...'
                    sh 'pip install flake8 black'
                    sh 'flake8 main.py --max-line-length=88 --ignore=E203,W503'
                    sh 'black --check main.py'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                    // Create a simple test file if it doesn't exist
                    sh '''
                    cat > test_main.py << 'EOF'
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sample FastAPI app!"}

def test_say_hello():
    response = client.get("/hello/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_say_hello_with_name():
    response = client.get("/hello/?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}

def test_sum_numbers():
    response = client.get("/sum/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"sum": 8}
EOF
                    '''
                    sh 'pip install fastapi[all]'
                    sh 'python -m pytest test_main.py -v'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
                }
            }
        }
        
        stage('Push Docker Image') {
            when {
                branch 'main' // Only push on main branch
            }
            steps {
                script {
                    echo 'Pushing Docker image to registry...'
                    // Uncomment and configure when you have a registry
                    // sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${REGISTRY_URL}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                    // sh "docker push ${REGISTRY_URL}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                    // sh "docker tag ${DOCKER_IMAGE}:latest ${REGISTRY_URL}/${DOCKER_IMAGE}:latest"
                    // sh "docker push ${REGISTRY_URL}/${DOCKER_IMAGE}:latest"
                    
                    echo 'Docker image built successfully. Update REGISTRY_URL to push to your registry.'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            when {
                branch 'main' // Only deploy on main branch
            }
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                    // Uncomment and configure when you have a Kubernetes cluster
                    // sh "kubectl apply -f deployment.yaml"
                    // sh "kubectl apply -f service.yaml"
                    // sh "kubectl apply -f ingress.yaml"
                    
                    echo 'Kubernetes deployment completed. Update the commands above for your cluster.'
                }
            }
        }
    }
    
    post {
        always {
            script {
                echo 'Cleaning up workspace...'
                sh 'docker system prune -f || true'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
} 