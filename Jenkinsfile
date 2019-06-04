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
		stage('Smoke Test') {
			agent{
				dockerfile{
					filename 'dockerfiles/docker-compose.dockerfile'
					args "--net host -v /var/run/docker.sock:/var/run/docker.sock"
				}
			}
			steps {
				sh 'docker-compose up -d'
				sh 'sleep 30'
				sh 'curl --fail -I http://0.0.0.0:8888/health'
			}
			post {
				always {
					sh "docker-compose down"
				}
			}        
		}
	}
}