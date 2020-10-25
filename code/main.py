import os

try: 
    from googleapiclient import discovery
    from dotenv import load_dotenv
    import discord
    from discord.ext import commands
    from functions import *
except:
    os.system('pip3 install google-api-python-client')
    os.system('pip3 install python-dotenv')
    os.system('pip3 install discord.py')

load_dotenv()

API_KEY = os.getenv('PERSPECTIVE_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='=')
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

attributes = ['TOXICITY', 'INSULT', 'PROFANITY', 'SEVERE_TOXICITY', 'IDENTITY_ATTACK', 'FLIRTATION', 'SEXUALLY_EXPLICIT', 'THREAT']

analyze_request = {
    'comment': {'text':''},
    'requestedAttributes': {}
}
for att in attributes:
    analyze_request['requestedAttributes'][att] = {}

print("CONNECTED")

@bot.listen('on_message')
async def talk_it(message):
    # condition to be changed later: made to prevent spamming
    if message.author.bot:
        return
    if message.channel.name != 'bot-test' and message.channel.name != '_bot':
        return

    text = message.content
    print(text)
    analyze_request['comment']['text'] = text
    response = service.comments().analyze(body=analyze_request).execute()
    response = response['attributeScores']
    
    msg = ''
    refined_attributes = {}
    for att in attributes:
        value = response[att]['summaryScore']['value']
        refined_attributes[att] = value
        value = f"```\n{att}: {value}\n```"
        msg += value

    tags = tagger(refined_attributes)
    if len(tags) > 0:
        msg += "\n```"
        for tag in tags:
            msg += tag + ", "
        msg = msg[:-2]
        msg += "\n```"
        await message.channel.send(msg)
    else:
        msg += "no triggers"
        await message.channel.send(msg)

bot.run(DISCORD_TOKEN)