pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh '''
        if [ -d "helloworld" ]; then rm -Rf helloworld; fi
        git clone https://github.com/arulrevtest/helloworld.git
        ls -la helloworld
        PYTHON = `which python`
        ${PYTHON} update_values.py 'helloworld' '0.1.31'
        cd ${params.repository}-charts                        
        git add --all .                        
        git commit -m "Update values yaml with new docker image"                        
        git push origin ${params.branch}

        '''
      }
    }
  }
}