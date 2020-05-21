import os


class docker:
    def __init__(self, distro, pkgMgmt):
        self.necessaryPackages = "apt-transport-https ca-certificates curl gnupg-agent software-properties-common"
        self.distro = distro
        self.pkgMgmt = pkgMgmt

    def engine(self):
        # Installing Docker in Debian based system's
        if self.pkgMgmt == 'deb':
            print('Veryfing that all necessary packages has installed.')
            os.system(
                f'which {self.necessaryPackages} || sudo apt install {self.necessaryPackages} -y')

            print('Adding Docker’s official GPG key')
            os.system(
                f"curl -fsSL https://download.docker.com/linux/{self.distro}/gpg | sudo apt-key add -")

            print('Adding docker repository')
            os.system('sudo add-apt-repository'
                      f' "deb [arch=amd64] https://download.docker.com/linux/{self.distro}'
                      ' $(lsb_release -cs)'
                      ' stable"')

            print('Installing Docker')
            os.system(
                'sudo apt update && sudo apt install docker-ce docker-ce-cli containerd.io -y')
       
        # Installing Docker in RedHat based system's
        elif self.pkgMgmt == 'rpm':
            print('Checking updates ...')
            os.system('sudo yum check-update')
            
            print('Installing all dependencies ...')
            os.system('sudo yum install -y yum-utils device-mapper-persistent-data lvm2')

            print('Adding the Docker repository ...')
            os.system('sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')

            print('Installing Docker Engine')
            os.system('sudo yum install docker')
        
        # Installing Docker in Arch based system's
        elif self.pkgMgmt == 'pacman':
            print('Checking Updates ...')
            os.system('sudo pacman -Syu')

            print('Installing Docker')
            os.system('sudo pacman -Sy docker')
        
        # Add user in Docker group,'not sudo exec'
        print('Adding your user in Docker group')
        os.system('sudo usermod -aG docker $USER')

        print('Docker engine has been installed')

    def compose(self):
        print('Installing Docker-compose')
        os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')

        print('Adding exec permission')
        os.system('sudo chmod +x /usr/local/bin/docker-compose')

        print('Docker compose has been installed')
