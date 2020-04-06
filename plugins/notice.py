import slackbot.bot as bot
import os


@bot.listen_to('学習完了')
def remove_nohup(message):
    try:
        os.remove('./nohup.out')
        pass
    except FileNotFoundError:
        message('File not found...')


@bot.listen_to('だめだった')
def echo_error_contents(message):
    try:
        with open('./nohup.out') as f:
            s = f.readlines()
        for i, line in enumerate(s[::-1]):
            if 'Traceback' in line:
                break
        message.send('```' + ''.join(s[-1 * (i + 1):]) + '```')
        os.remove('./nohup.out')
    except FileNotFoundError:
        message.send('File not found...')


@bot.listen_to('進捗')
def echo_progress(message):
    try:
        with open('./nohup.out') as f:
            lines = f.readlines()
        if len(lines) > 20:
            message.send('Progress is here.\n```' + ''.join(lines[-20:]) + '```')
        else:
            message.send('Progress is here.\n```' + ''.join(lines) + '```')
    except FileNotFoundError:
        message.send('File not found...')
