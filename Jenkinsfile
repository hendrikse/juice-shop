pipeline {
  agent {
    docker {
      image '10.15-alpine'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'npm install'
        sh 'npm run'
      }
    }
  }
}