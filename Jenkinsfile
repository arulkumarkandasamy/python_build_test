pipeline {
  agent { docker { image 'python:3.7.2' } }
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
        python update_values.py
        cd ${params.repository}-charts                        
        git add --all .                        
        git commit -m "Update values yaml with new docker image"                        
        git push origin ${params.branch}

        '''
      }
    }
  }
}