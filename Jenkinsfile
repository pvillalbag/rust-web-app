pipeline {
	environment {
		REGISTRY = credentials('REGISTRY')
		REGISTRY_HOST = '52.18.239.125'
		
		DOCKER_NETWORK_NAME = 'docker_network'
		DOCKER_IMAGE = 'web'
		DB_IMAGE = 'mysql'
		MYSQL_ROOT_PASSWORD = 'pass'
		MYSQL_DATABASE = 'heroes'
		MYSQL_USER = 'user'
		MYSQL_PASSWORD = 'password'
		
		AWS_STAGING = credentials('AWS')
        AWS_STAGING_DEFAULT_REGION = 'eu-west-1'
        AWS_STAGING_CLUSTER_NAME= 'cluster-of-User6'
		
		DOCKER_PF_WEB = 'web-port-forward-smoke-test'
		DOCKER_PF_DB = 'db-port-forward-smoke-test'
		
		K8S_IT_POD = 'integration-tests'
		
		SLACK_CHANNEL = 'a-bit-of-everything'
		SLACK_TEAM_DOMAIN = 'devopspipelines'
	}
	agent any
	
	stages {
		stage('Connect to K8S Staging'){
			steps {
				sh 'docker run -v ${HOME}:/root --rm \
					-v /var/run/docker.sock:/var/run/docker.sock \
					-e AWS_ACCESS_KEY_ID=${AWS_STAGING_USR} \
					-e AWS_SECRET_ACCESS_KEY=${AWS_STAGING_PSW} \
					mendrugory/awscli \
					aws eks --region ${AWS_STAGING_DEFAULT_REGION} \
					update-kubeconfig --name ${AWS_STAGING_CLUSTER_NAME}'
			}
		}
		
		stage('Deploy to Staging') {
			agent {
				docker {
					image 'mendrugory/ekskubectl'
					args '-v ${HOME}/.kube:/root/.kube \
					-e AWS_ACCESS_KEY_ID=${AWS_STAGING_USR} \
					-e AWS_SECRET_ACCESS_KEY=${AWS_STAGING_PSW}'
				}
			}                        
			steps {
				sh 'kubectl apply -f deployment/staging/staging.yaml'
				sh 'kubectl apply -f deployment/staging/integration_tests.yaml'
			}                
		}
		
		stage('Staging: PF DB Migration') {    
			steps {
				script {
					PODNAME = sh(script: "docker run -v ${HOME}/.kube:/root/.kube \
						-e AWS_ACCESS_KEY_ID=${AWS_STAGING_USR} \
						-e AWS_SECRET_ACCESS_KEY=${AWS_STAGING_PSW} \
						mendrugory/ekskubectl \
						kubectl get pods -n staging -l app=db \
						-o jsonpath='{.items[0].metadata.name}'", returnStdout: true)
					echo "The pod is ${PODNAME}"
					sh(script: "docker run --name ${DOCKER_PF_DB} \
						-v ${HOME}/.kube:/root/.kube -p 3306:3306 --rm \
						-v /var/run/docker.sock:/var/run/docker.sock    \
						-e AWS_ACCESS_KEY_ID=${AWS_STAGING_USR} \
						-e AWS_SECRET_ACCESS_KEY=${AWS_STAGING_PSW} \
						mendrugory/ekskubectl kubectl port-forward \
						--address 0.0.0.0 -n staging ${PODNAME} 3306:3306 &")
				}
			}
		}
		
		stage('Staging: DB Migration') {
			agent {
				dockerfile {
					filename 'dockerfiles/diesel-cli.dockerfile' 
					args '--entrypoint="" --net=host \
					-e DATABASE_URL=mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@0.0.0.0:3306/${MYSQL_DATABASE}'    
				}
			}
			steps {
				sh 'diesel migration run'    
			}                
		}
		
		stage('Staging: Integration Test') {
			agent {
				dockerfile {
					filename 'mendrugory/ekskubectl' 
					args '-v ${HOME}/.kube:/root/.kube \
						-e AWS_ACCESS_KEY_ID=${AWS_STAGING_USR} \
						-e AWS_SECRET_ACCESS_KEY=${AWS_STAGING_PSW}'
					}
				}
			steps {
				sh 'kubectl exec -n staging -it ${K8S_IT_POD} -- python3 integration_tests/integration_test.py' 
			}                
		}
	}//stages
	post {
		success {
			slackSend (
				channel: "${SLACK_CHANNEL}",
				teamDomain: "${SLACK_TEAM_DOMAIN}",
				tokenCredentialId: 'SLACK_TOKEN_ID',
				color: '#00FF00',
				message:  "SUCCESSFUL: Job '${JOB_NAME} [${BUILD_NUMBER}]' (${BUILD_URL})")
		}
		failure {
			slackSend (
				channel: "${SLACK_CHANNEL}",
				teamDomain: "${SLACK_TEAM_DOMAIN}",
				tokenCredentialId: 'SLACK_TOKEN_ID',
				color: '#FF0000',
				message:  "SUCCESSFUL: Job '${JOB_NAME} [${BUILD_NUMBER}]' (${BUILD_URL})")
		}
		always {
			sh 'docker kill ${DOCKER_IMAGE} ${DB_IMAGE} || true'
			sh 'docker network rm ${DOCKER_NETWORK_NAME} || true'
			sh 'docker kill ${DOCKER_PF_WEB} ${DOCKER_PF_DB} || true'
			
			/*sh 'docker run -v ${HOME}/.kube:/root/.kube \
				-v /var/run/docker.sock:/var/run/docker.sock \
				-e AWS_ACCESS_KEY_ID=${AWS_STAGING_USR} \
				-e AWS_SECRET_ACCESS_KEY=${AWS_STAGING_PSW} \
				mendrugory/ekskubectl \
				kubectl delete po ${K8S_IT_POD} -n staging'*/
		}
	}
}