#! /bin/sh
#
# Source : store-it.appspot.com/tou/tou.html

RTMPDUMP=rtmpdump

RTMP="`echo $1 | sed 's/<break>.*$//'`"
APP="`echo ${RTMP} | sed 's/^.*\/\(ondemand\/\?\)/\1/'`"
PLAYPATH="`echo $1 | sed 's/^.*<break>//'`"
AUTH="`echo $1 | sed 's/^.*auth=//;s/&.*$//'`"

OUT=$2

echo $RTMP
echo $APP
echo $PLAYPATH
echo $AUTH

set -x
exec ${RTMPDUMP} --app ${APP} \
   --flashVer 'WIN 10,0,22,87' \
   --swfVfy 'http://static.tou.tv/lib/ThePlatform/4.1.2/swf/flvPlayer.swf' \
   --auth "${AUTH}" \
   --tcUrl "${RTMP}" --rtmp "${RTMP}" \
   --playpath "${PLAYPATH}" \
   -o $OUT --verbose 
