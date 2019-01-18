pipeline {
  agent {
    docker {
      image 'nikolaifranke/jenkins:test'
      args '-p 3000:3000'
    }

  }
  stages {
    stage('Selenium test') {
      steps {
        sh 'python script.py'
      }
    }
    stage('Build') {
      steps {
        sh 'npm install'
      }
    }
    stage('Start') {
      steps {
        sh 'npm start'
      }
    }
  }
}
