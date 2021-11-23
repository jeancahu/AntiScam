import discord

message_content = ''
last_message = ''
last_message_content = ''
spam_counter = 0


async def AntiScam(
        message,
        bot,
        white_list = [],
        muted_role = "Muted",
        verified_role = "Verified",
        logs_channel = 0):

    global message_content, \
        last_message, \
        last_message_content, \
        spam_counter

    message_content = "{}: {}" \
        .format(message.author.id, message.content) \
        .replace("'", "`")

    # AntiScam-System
    if message_content == last_message_content and \
       message.content != '' and \
       message.author.id not in whitelist:

        spam_counter += 1
        await message.delete()
    else:
        last_message = message
        last_message_content = message_content
        spam_counter = 0

    if len(message.mentions) > 10 and message.author.id not in whitelist:
        await message.delete()
        spam_counter = 2

    if spam_counter > 1 and message.author.id not in whitelist:
        spam_counter = 0
        muted = discord.utils.get(message.author.guild.roles, name=muted_role)
        verified = discord.utils.get(message.author.guild.roles, name=verified_role)
        await last_message.delete()
        await message.author.add_roles(muted)
        await message.author.remove_roles(verified)

        if Type(logs_channel) == int:
            logs_channel = bot.get_channel (logs_channel)

        await logs_channel.send("USUARIO MUTEADO: {}".format(message_content))
