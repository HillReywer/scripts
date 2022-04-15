#!/bin/bash

TOKEN=''

CHAT_ID=""
SUBJECT=""
MESSAGE='Login: '$(whoami)' at '$(date)' server: '$(hostname)
PROXY_CURL=""
LOG_FILE="/dev/null"

date +"%Y-%m-%d %H:%M:%S" >> $LOG_FILE
echo $CHAT_ID >> $LOG_FILE
/usr/bin/curl -k -s --header 'Content-Type: application/json' --request 'POST' --data "{\"chat_id\":\"${CHAT_ID}\",\"text\":\"${SUBJECT}\n${MESSAGE}\"}" "https://api.telegram.org/bot${TOKEN}/sendMessage" 2>&1 >> $LOG_FILE
echo "" >> $LOG_FILE