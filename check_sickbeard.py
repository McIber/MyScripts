#! /usr/bin/env python

#def check_process(process):


from functions import *
import syslog
from time import sleep

retornoprocesso = False
process = 'SickBeard.py'
lock_file = '/var/run/sickbeard/sickbeard.pid' 
service = 'sickbeard'


syslog.openlog( 'sickbeard-check', 0, syslog.LOG_LOCAL4 )

# Example of how to use
if isThisRunning(process) == True:
  syslog.syslog( 'SickBeard Running!' )
  #syslog.syslog( '%%TEST-6-LOG: Log msg: %s' % 'Running!' )
else:
  syslog.syslog('SickBeard not running, trying to restart')
  if fileExists(lock_file):
    syslog.syslog( 'SickBeard lock file exists, trying to delete' )
    os.remove(lock_file)
    syslog.syslog( 'SickBeard lock file deleted' )
  syslog.syslog( 'restarting sickbeard service...' )
  runService(service)
  sleep (2)
  if isThisRunning(process) == True:
    syslog.syslog( 'SickBeard service restarted' )
  else:
    syslog.syslog( 'Error starting SickBeard service' )
