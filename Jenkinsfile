pipeline {
	agent any
	stages{
		stage('Saludos') {
			steps {
				echo "Hola!"
				echo "Testing webhook"
				sh "env"
			}
		}
		stage('Mi usuario') {
			steps {
				echo "Mi nombre de usuario es: "
				sh "whoami"
			}
		}
		stage('Meteorología') {
			agent {
				docker {
					image 'ubuntu:latest'
				}
			}
			steps {
				sh "curl http://wttr.in/cijuela"
			}
		}
	}
}