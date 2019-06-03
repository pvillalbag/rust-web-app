pipeline {
	environment {
		REGISTRY = credentials('REGISTRY')
		REGISTRY_HOST = '34.254.188.166'
	}
	agent any
	
	stages {	 
		stage('Docker registry log in') {
			steps {
				sh 'docker login ${REGISTRY_HOST} -u ${REGISTRY_USR} -p ${REGISTRY_PSW}'
			}
		}	 
		stage('Unit Test') {
			agent{
				docker{
					image '${REGISTRY_HOST}/rust-base'
				}
			}
			steps {
				sh 'rustup default nightly-2018-04-04'
				sh 'cargo test'
			}
		}
	}
}