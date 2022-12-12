import discord                                  #Installs discord.py library assisting in apps using Discord API

intents = discord.Intents.default()             #Help indicate which events can be sent in the app
intents.message_content = True
client = discord.Client(intents=intents)        #Connection to Discord

@client.event                                   #When Cyre logs in, it prompts the bot to log a message noting that it is online (in terminal)
async def on_ready():
    print(f'{client.user} is now online!')

@client.event                                   #Lets the bot know to only trigger when the author=user
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('```Here is a list of commands to get you started! \n\n<!hello> - Bot will greet you \n<!hicyre> - Bot will personally greet you (command under work) \n<!badrobot> - Bot will cry \n<!goodrobot> - Bot will smile```')

    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')

    #Implement response to author

    if message.content.startswith('!hicyre'):
        await message.channel.send('What\'s up <@622157526951133205>! `*command undergoing maintenance*`')

    if message.content.startswith('!badrobot'):
        await message.channel.send(':sob::robot:')

    if message.content.startswith('!goodrobot'):
        await message.channel.send(':grin::robot:')

client.run('MTA1MTcxNzk5ODA2ODYzMzYzMQ.Gf4KbL.DDqy1MLY0ojHhTmdGfLscU7HdH1HiI_--S-o8I')