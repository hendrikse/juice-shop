pipeline {
  node{
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
