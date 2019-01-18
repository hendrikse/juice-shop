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
    }
    stage('Selenium') {
      steps {
        sh 'python3 script.py'
      }
    }
    stage('ZAP active scan') {
      steps {
         sh 'curl "http://localhost:8090/JSON/ascan/action/scan/?zapapiformat=JSON&formMethod=GET&url=localhost%3A3000&recurse=&inScopeOnly=&scanPolicyName=&method=&postData=&contextId="'
      }
    }
  }
}
