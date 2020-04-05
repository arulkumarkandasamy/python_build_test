pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh '''
        git clone https://github.com/arulrevtest/helloworld.git
        ls -la helloworld

        '''
      }
    }
  }
}