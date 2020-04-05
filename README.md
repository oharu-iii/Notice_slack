# Notice_slack
Slackbot to notify you of python deep learning results and progress.

## How to use

### Add environment variables and Make a channel
You have to add two environment variables:
1. 'SLACK_WEBHOOK' for getting a slack Web-hook url.
1. 'SLACKBOTTOKEN_TEST_HARU' for getting a slack access token. 

And you have to make a channel 'notice' and add the slackbot there.

### Start learning model
If you want to run 'train.py', you can use the following command:
```
$ bash run.sh train.py
```

If you want to run it in the background, you can use the following command:
```
$ nohup ./run.sh train.py &
```

If you use nohup, the slackbot can show progress and error contents.

### Progress
If you post '進捗' to #notice, the slackbot show at least 20 lines from nohup.out.

## Try this
```
$ nohup ./run.sh correct.py &
```
```
$ nohup ./run.sh incorrect.py &
```