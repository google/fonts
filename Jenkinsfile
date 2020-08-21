
node('master') {

    stage('Git checkout') {
        try {
            scm_data = checkout([
                $class: 'GitSCM',
                branches: [[name: 'master']],
                gitTool: 'Default',
                userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/Monotype/google-fonts.git']]]
            )
        } catch(e) {
            currentBuild.result = 'FAILURE'
            slackSend(channel: "fonttools-jenkins",
                      color: "#bf0000",
                      message:":linux: google-fonts failed during Git checkout.")
            throw(e)
        }
    }

    stage('Update Git Clone') {
        sh """
            git remote add --track master upstream git://github.com/google/fonts.git
            git fetch upstream
            git pull upstream master
            git rebase upstream/master
            git push -f origin master
        """
    }

}