import subprocess
import os

def stdin(command):
    return os.system(command)

def stdout(command):
    popen = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
    return popen.stderr.read().decode("utf-8")

def stdcheck(command):
    return subprocess.check_output(command, shell=True).strip().decode("utf-8")
