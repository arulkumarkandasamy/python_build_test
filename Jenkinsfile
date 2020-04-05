pipeline {
  agent { docker { image 'arulkumar1967/python-yaml:latest' } }
  stages {
    stage('build') {
      steps {
        sh '''
        if [ -d "helloworld" ]; then rm -Rf helloworld; fi
        git clone https://github.com/arulrevtest/helloworld.git
        ls -la
        ls -la helloworld
        python --version
        chmod 777 update_values.py
        ls -la
        ./update_values.py 'helloworld' '0.1.31'
        cd ${params.repository}-charts                        
        git add --all .                        
        git commit -m "Update values yaml with new docker image"                        
        git push origin ${params.branch}

        '''
      }
    }
  }
}