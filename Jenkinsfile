pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('') {
      steps {
        sh 'docker run --rm -p 3000:3000 bkimminich/juice-shop'
      }
    }
  }
}