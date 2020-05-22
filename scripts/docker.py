import os


class docker:
    def __init__(self, distro, pkgMgmt):
        self.distro = distro
        self.pkgMgmt = pkgMgmt

    def engine(self):
        # Installing Docker in Debian based system's
        if self.pkgMgmt == 'deb':
            print('Veryfing that all necessary packages has installed.')
            os.system(
                'apt install apt-transport-https ca-certificates curl wget gnupg-agent software-properties-common -y')

            print('Adding Docker’s official GPG key')
            os.system(f"curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -")

            print('Adding docker repository')
            os.system('add-apt-repository'
                      f' "deb [arch=amd64] https://download.docker.com/linux/{self.distro}'
                      ' $(lsb_release -cs)'
                      ' stable"')

            print('Installing Docker')
            os.system(
                'apt update && apt install docker-ce docker-ce-cli containerd.io -y')

        # Installing Docker in RedHat based system's
        elif self.pkgMgmt == 'rpm':
            print('Remove old version')
            os.system('yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine')

            print('Checking updates ...')
            os.system('yum check-update')

            print('Installing all dependencies ...')
            os.system(
                'yum install -y yum-utils device-mapper-persistent-data lvm2')

            print('Adding the Docker repository ...')
            os.system(
                'yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')

            print('Installing Docker Engine')
            os.system(
                'yum install docker-ce docker-ce-cli containerd.io --skip-broken -y')

        # Installing Docker in Arch based system's
        elif self.pkgMgmt == 'pacman':
            print('Checking Updates ...')
            os.system('pacman -Syu')

            print('Installing Docker')
            os.system('pacman -Sy docker')

        # Add user in Docker group,'not sudo exec'
        print('Adding your user in Docker group')
        os.system('usermod -aG docker $USER')

        print('Docker engine has been installed')

    def compose(self):
        print('Installing Docker-compose')
        os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')

        print('Adding exec permission')
        os.system('chmod +x /usr/local/bin/docker-compose')

        print('Docker compose has been installed')
