pipeline {
    agent any 
    stages {
        stage('Welcome message') {
            steps {
                echo 'Hello world!' 
            }
        }
        
        stage('Clone SCM') {
            steps{
                // bat 'rmdir /s /q devops-batch-sam;'
                bat "git clone https://github.com/GuptaTanay/devops-batch-sam.git"
            }
        }
        stage('See the contents of directory')
        {
            steps{
                
                bat 'cd devops-batch-sam'
                bat 'dir'
            }
        }
        stage('Run python code')
        {
            steps{
                // bat 'C:\\Users\\tanay\\anaconda3\\condabin\\conda create -y -n jenkins_env python=3.7 anaconda'
                // bat 'C:\\Users\\tanay\\anaconda3\\condabin\\conda activate jenkins_env'
                // bat 'C:\\Users\\tanay\\anaconda3\\condabin\\conda install -y numpy'
                // bat 'C:\\Users\\tanay\\anaconda3\\python D:\\Training\\Devops\\devops-batch\\demo.py'
                // bat 'C:\\Users\\tanay\\anaconda3\\condabin\\conda deactivate'
                // bat 'conda remove '
                bat 'cd devops-batch-sam'
                bat 'dir'
                bat 'cd devops-batch-sam'
                bat 'dir'
                // bat 'copy C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Training\\Test\\devops-batch\\a.csv .'
            }
        }
        stage('Print csv file')
        {
            steps{
                bat 'cd devops-batch-sam'
                bat 'copy devops-batch-sam/a.csv a.csv'
                bat 'type a.csv'
                bat 'del a.csv'
            }
        }
    }
    
}