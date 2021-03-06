import os
import subprocess

from scripts.docker import docker as DockerInstall
from scripts.nodeJS import node as NodeInstall
from scripts.ohmyzsh import zsh as ZshInstall
from scripts.asdf import asdf as AsdfInstall

distro = subprocess.check_output(
    'lsb_release -is', shell=True).decode('utf-8').lower()


print('Verifying that all necessary packages are installed ...')
os.system('which curl || sudo apt install curl -y')
os.system('clear')

based = input('Distro is based in \n '
              '1 - Debian \n '
              '2 - RHAEL \n '
              '3 - Arch \n '
              'Select a option: ')

print(based)


if based == '1':
    pkgmgmt = 'deb'
elif based == '2':
    pkgmgmt = 'rpm'
elif based == '3':
    pkgmgmt = 'pacman'

print(pkgmgmt)


print("Welcome to Let's Install \nSelect a option for install")
choice = subprocess.check_output('whiptail'
                                 ' --title "Lets Install"'
                                 ' --checklist'
                                 ' --fb "Select a option for install" 20 90  6'
                                 ' "1" "Docker Engine - Dockerize your services and Apps " "OFF" '
                                 ' "2" "Docker Compose - Run multi containers using Docker-compose file " "OFF" '
                                 ' "3" "NodeJS - Executes JavaScript code outside of a web browser. " "OFF" '
                                 ' "4" "ASDF - Extendable version manager with support for Ruby, Node.js & more. " "OFF" '
                                 ' "5" "Oh My ZSH - Adicione themas e personalize seu terminal. " "OFF" 3>&1 1>&2 2>&3 ', shell=True).decode('utf-8')
                                 
print(choice)


# for value in choice.split('"'):
#     if value == "1":
#         docker = DockerInstall(distro, pkgmgmt)
#         docker.engine()

#     elif value == "2":
#         docker = DockerInstall(distro, pkgmgmt)
#         docker.compose()

#     elif value == "3":
#         version = input('Insert a version of NodeJS (Not choice = 12.x): ')
#         if version == '':
#             version = '12'
#         node = NodeInstall(pkgmgmt, version)
#         node.install()

#     elif value == "4":
#         asdf = AsdfInstall(pkgmgmt)
#         asdf.install()

#     elif value == "5":
#         ohmyzsh = ZshInstall(pkgmgmt)
#         ohmyzsh.install()
#         zshoption = input('Do you want to restore the settings? (y/n):  ')
#         if zshoption == "y":
#             folder = input('Insert a restore folder: \n')
#             ohmyzsh.restore(folder)