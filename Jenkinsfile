pipeline {
  agent {
    docker {
      image 'node:11'
      args '-p 3000:3000'
    }

  }
  stages {
    stage('Selenium test') {
      steps {
        sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
        sh 'python get-pip.py'
        sh 'pip install selenium'
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
