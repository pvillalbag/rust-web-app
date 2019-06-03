pipeline {
	environment {
		REGISTRY = credentials('REGISTRY')
		REGISTRY_HOST = 34.254.188.166
	}
	agent any
	
	stages {	 
		stage('Docker registry log in') {
			steps {
				sh 'docker login ${REGISTRY_HOST} -u ${REGISTRY_USR} -p ${REGISTRY_PSW}'
			}
		}
	}
}