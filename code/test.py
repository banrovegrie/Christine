import os
import pprint

try: 
    from googleapiclient import discovery
    from dotenv import load_dotenv
    import discord
    from discord.ext import commands
except:
    os.system('pip install google-api-python-client')
    os.system('pip install python-dotenv')

load_dotenv()

API_KEY = os.getenv('PERSPECTIVE_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='=')
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

print("CONNECTED")

attributes = ['TOXICITY', 'INSULT', 'PROFANITY', 'SEVERE_TOXICITY', 'IDENTITY_ATTACK', 'FLIRTATION', 'SEXUALLY_EXPLICIT', 'THREAT']

analyze_request = {
  'comment': {'text':''},
  'requestedAttributes': {}
}
for att in attributes:
  analyze_request['requestedAttributes'][att] = {}

@bot.listen('on_message')
async def talk_it(message):
  if message.author.bot:
    return
  text = message.content
  analyze_request['comment']['text'] = text
  response = service.comments().analyze(body=analyze_request).execute()
  response = response['attributeScores']
  msg = ''
  for att in attributes:
    value = response[att]['summaryScore']['value']
    value = f"```\n{att}: {value}\n```"
    msg += value
  await message.channel.send(msg)


bot.run(DISCORD_TOKEN)




# # Generates API client object dynamically based on service name and version.
# service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

# analyze_request = {
#   'comment': { 'text': 'friendly greetings from python' },
#   'requestedAttributes': {'TOXICITY': {}}
# }

# response = service.comments().analyze(body=analyze_request).execute()

# print(response)
# import json
# print json.dumps(response, indent=2)