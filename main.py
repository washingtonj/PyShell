import os
import subprocess

from scripts.docker import docker as DockerInstall
from scripts.nodeJS import node as NodeInstall

distro = subprocess.check_output('lsb_release -is', shell=True).decode('utf-8').lower()


print('Verifying that all necessary packages are installed ...')
os.system('which curl || sudo apt install curl -y')
os.system('clear')

based = input('Distro is based in \n '
                    '1 - Debian \n '
                    '2 - RHAEL \n '
                    '3 - Arch \n '
                    'Select a option: ')

if based == '1':
  pkgmgmt = 'deb'
elif based == '2':
  pkgmgmt = 'rpm'
elif based == '3':
  pkmgmt = 'pacman'


print("Welcome to Let's Install \nSelect a option for install")
choice = subprocess.check_output('whiptail'
                                 ' --title "Lets Install"'
                                 ' --checklist'
                                 ' --fb "Select a option for install" 20 90  6'
                                 ' "1" "Docker Engine - Dockerize your services and Apps " "OFF" '
                                 ' "2" "Docker Compose - Run multi containers using Docker-compose file " "OFF" '  
                                 ' "3" "NodeJS - Executes JavaScript code outside of a web browser. " "OFF" 3>&1 1>&2 2>&3 ', shell=True).decode('utf-8')


for value in choice.split('"'):
  if value ==  "1":
    docker = DockerInstall(distro, based)
    docker.engine()
 
  elif value == "2":
    docker = DockerInstall(distro, based)
    docker.compose()
 
  elif value == "3":
    version = input('Insert a version of NodeJS: ')
    node = NodeInstall(pkgmgmt, version)    
    node.install()
