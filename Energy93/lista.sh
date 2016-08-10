#!/bin/bash
# Add this line to crontab:
# #*/1 * * * * ~/lista.sh



curl http://www.181.fm/station_playing/181-energy93.html -s | col -b > /tmp/song.tmp
#set -x
SONG=`grep ffffff /tmp/song.tmp | cut -d'>' -f2 | cut -d '<' -f1`
ESTA=`grep "$SONG" titulos.txt | wc -l`

if [ $ESTA -eq 0 ]
then
    echo $SONG >> titulos.txt
fi
rm -f /tmp/song.tmp
