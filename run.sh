#!/bin/bash
# $? : exit code of the last command

python $1
exit_code=$?

if [ $exit_code = 0 ]; then
    echo 'good'
    curl -X POST --data-urlencode "payload={\"channel\": \"#notice\", \"text\": \"学習完了！ [ $1 ]\"}" $SLACK_WEBHOOK
else
    echo 'bad'
    curl -X POST --data-urlencode "payload={\"channel\": \"#notice\", \"username\": \"Incomplete...\", \"text\": \"だめだった…… [ $1 ]\", \"icon_emoji\": \":cry:\"}" $SLACK_WEBHOOK
fi