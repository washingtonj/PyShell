import os

class node():
  def __init__(self, based, ver='12'):
    self.version = ver
    self.package = based

  def install(self):
    if self.package == 'deb':
      os.system(f'curl -sL https://deb.nodesource.com/setup_{self.version}.x | sudo -E bash - && sudo apt install -y nodejs')
    elif self.package == 'rpm':
      os.system(f'curl -sL https://rpm.nodesource.com/setup_{self.version}.x | sudo bash - && yum install -y nodejs')
    elif self.package == 'pacman':
      os.system('sudo pacman -Syu nodejs npm')