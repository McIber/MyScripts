#! /usr/bin/env python

#def check_process(process):


from functions import *
import syslog
from time import sleep

retornoprocesso = False
process = '/usr/local/bin/rtorrent'
lock_file = '/home/hyggelig/.config/rtorrent/session/rtorrent.lock' 
service = 'rtorrent'


syslog.openlog( 'rtorrent-check', 0, syslog.LOG_LOCAL4 )

# Example of how to use
if isThisRunning(process) == True:
  syslog.syslog( 'rTorrent Running!' )
  #syslog.syslog( '%%TEST-6-LOG: Log msg: %s' % 'Running!' )
else:
  syslog.syslog('rTorrent not running, trying to restart')
  if fileExists(lock_file):
    syslog.syslog( 'rTorrent lock file exists, trying to delete' )
    os.remove(lock_file)
    syslog.syslog( 'rTorrent lock file deleted' )
  syslog.syslog( 'restarting rtorrent service...' )
  runService(service)
  sleep (5)
  if isThisRunning(process) == True:
    syslog.syslog( 'rTorrent service restarted' )
  else:
    syslog.syslog( 'Error starting rTorrent service' )