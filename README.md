# AntiScam
Discord bot code to stop users that are scamming with fake messages of free discord nitro on servers in order to steal users accounts.

# How to use
Here is an example image of the most simple main python script to run a discord bot to avoid discord massive scams on servers.

```python
from discord.ext import commands
from AntiScam import AntiScam

white_list = [] # Here you can add the IDs of the users allowed to bypass the AntiScam system.
logs_channel = None # Here you can add the ID of the channel where the logs will be sent.

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') # Remove this line if you want to use the help command.

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verified', logs_channel=logs_channel) # Here you can change the names of the roles.

bot.run('<bot-token>')
```

To run the bot, the PyCord module must be installed (if you have installed pip3, it can be installed with `sudo pip3 install -r requirements.txt`)
