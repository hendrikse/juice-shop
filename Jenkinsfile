pipeline {
  agent {
    docker {
      image 'node:11'
      args '-p 3000:300'
    }

  }
  stages {
    stage('Node Install') {
      steps {
        sh 'npm install'
      }
    }
  }
}