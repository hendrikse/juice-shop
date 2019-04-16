pipeline {
  agent {
    docker {
        image 'node:7-alpine'
    }
  }
  stages {
     stage('Build') {
      steps {
        echo 'Building...'
        sh 'export PATH=/usr/local/bin:$PATH'
        sh 'npm install'
      }
    }
    stage('Start') {
      steps {
        sh 'npm start &'
        sh 'sleep 30'
      }
    }
    stage('Selenium') {
      steps {
        sh 'python3 selenium_script.py'
      }
    }
    stage('ZAP active scan') {
      steps {
        sh 'python3 zap_script.py'
      }
    }
  }
}
