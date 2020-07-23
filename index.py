
from scripts.asdf import asdf as AsdfInstall
from scripts.ohmyzsh import zsh as ZshInstall
from scripts.nodeJS import node as NodeInstall
from scripts.docker import docker as DockerInstall

from whiptail.runner import stdcheck, stdin, stdout
from whiptail.start import whiptail
start = whiptail(20, 120)


# Running Code
distro = stdcheck("lsb_release -is")

based = start.radiolist("Selecione uma distribuição.", f"Me parece que sua distro é a {distro} :)", {
    "Debian": "Ubuntu, ZorinOS e outros.",
    "RHAEL": "CentOS e outros",
    "Arch": "Manjaro e Outros"
})

choice = start.checklist("Vamos instalar!", "Selecione o que deseja instalar", {
    "Docker Engine": "Dockerize your services and Apps",
    "Docker Compose": "Run multi containers using Docker-compose file",
    "NodeJS": "Executes JavaScript code outside of a web browser. ",
    "ASDF": "Extendable version manager with support for Ruby, Node.js & more.",
    "Oh My ZSH": "Your terminal never felt this good before.."
})

# Define a package manager for using in install process
if based == '0':
    pkgmgmt = 'deb'
elif based == '1':
    pkgmgmt = 'rpm'
elif based == '2':
    pkgmgmt = 'pacman'


# Execute script for install
for value in choice.split('"'):
    if value == "0":
        docker = DockerInstall(distro, pkgmgmt)
        docker.engine()

    elif value == "1":
        docker = DockerInstall(distro, pkgmgmt)
        docker.compose()

    elif value == "2":
        version = input('Insert a version of NodeJS (Not choice = 12.x): ')
        if version == '':
            version = '12'
        node = NodeInstall(pkgmgmt, version)
        node.install()

    elif value == "3":
        asdf = AsdfInstall(pkgmgmt)
        asdf.install()

    elif value == "4":
        ohmyzsh = ZshInstall(pkgmgmt)
        ohmyzsh.install()
        zshoption = input('Do you want to restore the settings? (y/n):  ')
        if zshoption == "y":
            folder = input('Insert a restore folder: \n')
            ohmyzsh.restore(folder)
