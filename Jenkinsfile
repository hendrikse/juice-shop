pipeline {
  agent {
    docker {
      image 'kakehashi/node-pip'
      args '-p 3000:3000'
    }

  }
  stages {
    stage('Selenium test') {
      steps {
        sh 'pip3 install selenium'
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
