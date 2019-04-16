pipeline {
  agent {
    docker {
      image 'node:6-alpine'
      args '-p 3000:3000'
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
  }
}
