pipeline {
  agent {
    docker {
      image 'nikolaifranke/jenkins:latest'
      args '-p 3000:3000'
    }

  }
  stages {
    stage('Script') {
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
