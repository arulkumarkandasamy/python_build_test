pipeline {
  agent { docker { image 'arulkumar1967/python-git-yaml:latest' } }
  stages {
    stage('build') {
      steps {
        sh '''
        if [ -d "helloworld" ]; then rm -Rf helloworld; fi
        git clone https://github.com/arulrevtest/helloworld.git
        chmod -R 777 helloworld
        '''
        dir ('helloworld') {
            sh ''' 
                cat values.yaml
            '''
        }
      }
    }
  }
}