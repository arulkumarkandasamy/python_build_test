pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh '''
        $WORKING_DIR = 'helloworld'
        if [ -d "$WORKING_DIR" ]; then rm -Rf $WORKING_DIR; fi
        git clone https://github.com/arulrevtest/helloworld.git
        ls -la helloworld

        '''
      }
    }
  }
}