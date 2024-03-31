//http://localhost:8080/jenkins/generic-webhook-trigger/invoke?token=abc123

pipeline {
    agent any
    triggers {
        GenericTrigger(
                genericVariables: [
                        [key: 'refsb', value: '$.changes[0].ref.id'],
                        [key: 'repository_slug', value: '$.repository.slug'],
                        [key: 'actor', value: '$.actor.name'],
                        [key: 'type', value: '$.changes[0].type'],
                ],

                token: abc123,
                tokenCredentialId: '',
                printContributedVariables: true,
                printPostContent: true,
                silentResponse: false,
                regexpFilterText: '$refsb',
                regexpFilterExpression: '^(.*/main)',
        )
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}