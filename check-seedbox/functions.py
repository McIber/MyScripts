import re
from subprocess import Popen, PIPE, STDOUT
import os.path


def findThisProcess( process_name ):
  comando = 'ps -ef | grep %s | grep -v SCREEN |grep -v grep' % process_name
  ps = Popen(comando, shell=True, stdout=PIPE)
  output = ps.stdout.read()
  ps.stdout.close()
  ps.wait()
  return output

def isThisRunning( process_name ):
  output = findThisProcess( process_name )

  if re.search(process_name, output) is None:
    return False
  else:
    return True

def fileExists (file_path):
  return os.path.exists(file_path)
  
def runService (service_name):
  comando = 'service %s start' % service_name
  ps = Popen(comando, shell=True)


