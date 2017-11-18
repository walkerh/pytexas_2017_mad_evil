import os, sys, types
pwd_new = types.ModuleType('pwd')

def getpwnam(n):
    '''I'm whoever you want me to be...'''
    return (n, '*', os.getuid(), os.getgid(),
            'Fake', '/root', '/bin/bash')

pwd_new.getpwnam = getpwnam
sys.modules['pwd'] = pwd_new
