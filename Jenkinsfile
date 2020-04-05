pipeline {
  agent { docker { image 'arulkumar1967/python-git-yaml:latest' } }
  stages {
    stage('build') {
      steps {
      script {
        sh '''
        if [ -d "helloworld" ]; then rm -Rf helloworld; fi
        git clone https://github.com/arulrevtest/helloworld.git
        ls -la
        ls -la helloworld
        python --version
        chmod -R 777 helloworld
        ls -la
        #./update_values.py 'helloworld' '0.1.31'
        sed -i 's/^# version=.*/version=0.1.31/' helloworld/values.yaml
        cat helloworld/values.yaml
        pwd
        '''
        dir('helloworld') {       
        sh '''              
            git add --all .                        
            git commit -m "Update values yaml with new docker image"                        
            git push origin ${params.branch}
            '''
        }

        '''
      }
      }
    }
  }
}