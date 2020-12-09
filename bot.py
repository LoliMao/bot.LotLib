
from discord.ext import commands
import discord
import asyncio
import random
import youtube_dl


bot = commands.Bot(command_prefix="<", description="Bot de Baptistia#6190")
musics = {}
ytdl = youtube_dl.YoutubeDL()


@bot.event
async def on_ready():
    print("Logged in...")
    print("Welcome, LoliMao")
    print ("Invite url = https://discord.com/api/oauth2/authorize?client_id=785560672661536818&permissions=8&scope=bot")



@bot.command()
async def coucou (ctx):
    ctx.send("Coucou, je suis **Lotlib**, un bot créé par *Baptistia #6190*.")


@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    number_of_text_channels = len (server.text_channels)
    number_of_voice_channels = len (server.voice_channels)
    server_description = server.description
    number_of_member = server.member_count
    server_name = server.name
    messsage = f"Le serveur *{server_name}* a ({number_of_text_channels}) salons écrit, ({number_of_voice_channels}) salons vocaux ainsi que ({number_of_member}) membres. \nLa description du server est {server_description}."
    await ctx.send (messsage)


@bot.command()
async def bonjour(ctx):
    server = ctx.guild
    server_name = server.name
    hello_message = f"Bonjour jeune *padawan* ! Savais-tu que tu te trouvais dans le serveur *{server_name}* ? Ce serveur est génial car **JE** suis dedans."
    await ctx.send (hello_message)
    

@bot.command()
async def say(ctx, chiffre, *text):
    for i in range(int(chiffre)):
        print(" ".join(text))
        await ctx.send(" ".join(text))


@bot.command()
async def chinese(ctx, *chinese_text):
    chinese_char = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
    chinese_texte = []
    for word in chinese_text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord ("a")
                transformed = chinese_char[index]
                chinese_texte.append(transformed)
            else:
                chinese_texte.append(char)
        chinese_texte.append (" ")
    print ("".join (chinese_texte))
    await ctx.send ("".join (chinese_texte))


@bot.command()
@commands.has_permissions (manage_messages=True,)
async def clear(ctx, nombre: int):
 messages = await ctx.channel.history(limit=nombre + 1).flatten()
 for message in messages:
  await message.delete()

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join (reason)
    server = ctx.guild
    server_name = server.name
    await user.send(f"Vous avez été expulsé du serveur **{server_name}**.\nRaison : {reason}")
    await ctx.guild.kick(user, reason=reason)
    await ctx.send (f"```{user} a été expulsé.\nRaison : {reason}```")
    print(f"L'utilisateur {user} a été expulsé du serveur {server_name}.\nRaison : {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, *,reason="Aucune raison n'a été donnée"):
       server = ctx.guild
       server_name = server.name
       Ban = "Tu as été banni"
       reason:str ="".join (reason)
       embed_user = discord.Embed(title="Révoquer le bannissement", description=f"Vous avez été banni.",
                             url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLhLMYB8Um23XZlFXEuCjil1p6LJKTrd0v",
                             color=0xfa8072)
       embed_user.set_thumbnail(url="https://emoji.gg/assets/emoji/BanneHammer.png")
       embed_user.add_field(name="Serveur", value=server_name, inline=True)
       embed_user.add_field(name="Raison", value=reason, inline=False)
       embed_user.add_field(name="**Bannissement**", value=Ban)
       await user.send(embed=embed_user)
       await ctx.guild.ban (user, reason=reason)
       embed = discord.Embed(title="**Bannissement**", description="Un modérateur a frappé !",
                             url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLhLMYB8Um23XZlFXEuCjil1p6LJKTrd0v",
                             color=0x4b1414)
       embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
       embed.set_thumbnail(url="https://emoji.gg/assets/emoji/BanneHammer.png")
       embed.add_field(name="Membre banni", value=user.name, inline=True)
       embed.add_field(name="Modérateur", value=ctx.author.name, inline=True)
       embed.add_field(name="Raison", value=reason, inline=False)

       await ctx.send (embed=embed)
       print(f"L'utilisateur {user} a été banni du serveur {server_name} pour la raison: {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User,*reason):
    server = ctx.guild
    reason = " ".join (reason)
    server_name = server.name
    embed_user = discord.Embed(title="Débannissement", description=f"Un modérateur vous a débanni du serveur **{server_name}**.", color=0x4b1414)
    embed_user.add_field(name="Modérateur", value=ctx.author.name, inline=True)
    embed_user.add_field(name="Raison", value=reason, inline=False)
    embed = discord.Embed(title="**Débannissement**", description="Un modérateur a débanni quelqu'un.",
                          color=0x4b1414)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://emoji.gg/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre Débanni", value=user.name, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=False)

    await user.send (embed=embed_user)
    await ctx.guild.unban(user)
    await ctx.send (embed=embed)
    print (f"L'utilisateur {user} a été débanni du serveur {server_name} pour {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def showban(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send ("La liste des ID des utilisateurs bannis est:")
    await ctx.send ("\n".join (ids))


@bot.command()
@commands.has_permissions(manage_guild=True)
async def roulette(ctx):
    await ctx.send("La roulette va commencer dans 10 secondes. Envoyez \"moi\" dans ce channel pour y participer.")

    players = []
    def check(message):
        return message.channel == ctx.message.channel and message.author not in players and message.content == "moi"

    try:
        while True:
            participation = await bot.wait_for('message', timeout=10, check=check)
            players.append(participation.author)
            print("Nouveau participant :")
            print(participation)
            await ctx.send(f"**{participation.author.name}** participe au tirage ! Le tirage commence dans 10 secondes...")
    except: #Timeout
        print("Démarrage du tirage")

        gagner = ["mute de 24h", "mute de 1min", "mute de 5min", "mute de 1h"]
        await ctx.send("Le tirage va commencer dans 3...")
        await asyncio.sleep(1)
        await ctx.send("2")
        await asyncio.sleep(1)
        await ctx.send("1")
        loser = random.choice(players)
        price = random.choice(gagner)
        await ctx.send (f"La personne qui a gagné un {price} est...")
        await ctx.send (f"**{loser}** !")
        print(f"La personne qui a gagné un {price} est...")
        print(f"{loser} !")


async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(
                                                send_messages=False,
                                                speak=False),
                                            reason="Creation du role 'Muted' pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

    return await createMutedRole(ctx)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseignée."):
    gif = ["https://tenor.com/view/monsters-inc-shhh-quiet-sully-gif-14740084",
           "https://tenor.com/view/minnie-mouse-shhh-be-quiet-gif-8327015",
           "https://tenor.com/view/the-mask-mask-quiet-gif-7266789",
           "https://tenor.com/view/secret-gif-4440624",
           "https://tenor.com/view/shhh-quite-stop-wait-shush-gif-14462328"]
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a bien été mute.```Raison: {reason}```")
    await ctx.send(random.choice(gif))


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseignée."):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send (f"{member.mention} a bien été unmute.```Raison: {reason}```")


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)



bot.run(process.env.BOT_TOKEN)
