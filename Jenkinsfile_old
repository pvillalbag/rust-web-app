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
			    dockerfile {
			        filename 'dockerfiles/mycustomizedubuntu'
			        args '-v /var/run/docker.sock:/var/run/docker.sock'
			    }
			}
			when {branch 'master'}
				steps {
					sh "curl --version"
				}
			
			steps {
				sh "curl http://wttr.in/cijuela"
			}
		}
	}
}