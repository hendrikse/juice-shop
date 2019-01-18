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
        sh 'curl "http://172.17.0.4:8090/JSON/core/action/accessUrl/?zapapiformat=JSON&formMethod=GET&url=http%3A%2F%2F172.17.0.5%3A3000"'
        sh 'curl "http://172.17.0.4:8090/JSON/ascan/action/scan/?zapapiformat=JSON&formMethod=GET&url=http%3A%2F%2F172.17.0.5%3A3000"'
        sh 'echo "Waiting for active scan to finish (assuming scan id 0)"'
        sh 'while [[ $(grep -oP "\\d+" <<< "$(curl -s "http://172.17.0.4:8090/JSON/ascan/view/status/?zapapiformat=JSON&formMethod=GET&scanId=0")") != 100 ]]; do echo "Hi"; sleep 3; done'
        sh 'curl "http://172.17.0.4:8090/OTHER/core/other/htmlreport/?formMethod=GET"'
      }
    }
  }
}
