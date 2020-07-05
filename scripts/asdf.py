import os 

class asdf:
    def __init__(self, based):
        self.package = based

    def install(self):
        if self.package == "deb":
            os.system('apt install curl git -y')
        elif self.package == "pacman":
            os.system('dnf install curl git -y')
        elif self.package == "pacman":
            os.system('pacman -S curl git')
        os.system('git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.7.8')

        terminal = input("Select a terminal for ADD \n 1 = Bash \n 2 = ZSH \n") 
        if terminal == '1':
            bash = 'bashrc'
        else:
            bash = 'zshrc'

        os.system(f'echo ". $HOME/.asdf/asdf.sh" >> ~/.{bash}')
        os.system(f'echo ". $HOME/.asdf/completions/asdf.bash" >> ~/.{bash}')     