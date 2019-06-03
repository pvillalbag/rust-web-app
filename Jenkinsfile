pipeline {
	agent {
	 dockerfile{
		 filename 'dockerfiles/mycustomizedubuntu'
		 args '-v /var/run/docker.sock:/var/run/docker.sock'
		}
	}
	stages {	 
		stage('Check Curl') {
			when {branch 'master'} 
				steps {
					sh 'curl --version'
				}
			}
		stage('Check the Weather') {
			steps {
				sh 'curl wttr.in'
			}
		}
	}
}