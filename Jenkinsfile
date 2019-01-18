pipeline {
  agent {
    docker {
      image 'jenkinsagent:latest'
      args '-p 3000:3000'
    }

  }
  stages {  
     stage('Build') {
      steps {
        sh 'npm install'
      }
    }
    stage('Start') {
      steps {
        sh 'npm start &'
        sh 'sleep 30'
      }
      stage('Test') {
        steps {
          sh 'python3 script.py'
        }
    }
  }
}
