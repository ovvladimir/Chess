# terminal
import os

if os.name == 'nt':
    os.system('REG ADD HKCU\\Console /v FaceName /t REG_SZ /d "MS Gothic" /f')

os.system("start cmd /c python chess.py")

if os.name == 'nt':
    os.system('REG ADD HKCU\\Console /v FaceName /t REG_SZ /d "Consolas" /f')

# import subprocess
# subprocess.run('REG query "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Console\\TrueTypeFont"')
# subprocess.run(
#    'REG ADD HKCU\\Console /v FaceName /t REG_SZ /d "MS Gothic" /f',
#    stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NEW_CONSOLE)
