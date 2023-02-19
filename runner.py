import os
import threading
import subprocess




def run_ews():
    os.chdir('./ews')
    os.system('npm start')
    
t1 = threading.Thread(target=run_ews)
t1.start()
        