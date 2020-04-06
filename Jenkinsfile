pipeline {
  agent { docker { image 'arulkumar1967/python-git-yaml:latest' } }
  stages {
    stage('build') {
      steps {
        sh '''
        if [ -d "helloworld" ]; then rm -Rf helloworld; fi
        git clone https://github.com/arulrevtest/helloworld.git
        ls -la
        ls -la helloworld
        python --version
        chmod -R 777 helloworld
        ls -la       
        git commit -a -m "Update values yaml with new docker image"                        
        git push origin master
        '''
      }
    }
  }
}