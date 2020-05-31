import os


class zsh:
    def __init__(self, based):
        self.package = based

    def install(self):
        if self.package == 'deb':
            os.system('apt install zsh curl git -y')
        elif self.package == 'rpm':
            os.system('yum -y install zsh curl git')
        elif self.package == 'pacman':
            os.system('pacman -S zsh curl git')
        os.system(
            'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

    def restore(self, folder):
        os.system(f'cp {folder}/.bashrc ~/')
        os.system(f'cp {folder}/.zshrc ~/')
        os.system(f'cp -r {folder}/themes/* ~/.oh-my-zsh/themes')
