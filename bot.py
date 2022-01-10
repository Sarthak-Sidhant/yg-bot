import time
import discord
from discord.ext import commands
import time
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='=', intents=intents)
bot.remove_command('help')
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="=help"))
@bot.event
async def on_guild_join(ctx):
    channel = await ctx.guild.owner_id.create_dm()
    await channel.send("Thanks for adding the bot! Use setprefix to change the prefix of the bot in the server! Default prefix is '='")
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server! We Welcome you!')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'hello' in message.content.lower():
        await message.reply('Hello!')
        await message.add_reaction('👋')
    elif message.content.startswith('prefix'):
        await message.reply("=")
    elif 'heil hitler' in message.content.lower():
        await message.reply('The German penal code prohibits publicly denying the Holocaust and disseminating Nazi propaganda, both off- and online. This includes sharing images such as swastikas, wearing an SS uniform and making statements in support of Hitler.')
    elif 'hitler' in message.content.lower():
        await message.reply("Who? That Fascist Fuhrer of Germany? He's the worst. Responsible for killing 7 million Jews!")
    elif message.content.startswith('hi'):
        await message.reply('Hey There!')
    elif f'<@!{bot.user.id}>' in message.content:
        await message.reply("WHO SUMMONED ME? TELL ME WHAT WORK DO YOU HAVE?")
    elif 'good bot' in message.content.lower():
        await message.reply('Thank you!')
    elif 'bad bot' in message.content.lower():
        await message.reply('I am sorry! I will try to improve! Give your feedback on our GitHub repository!')
    await bot.process_commands(message)
@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send('Pong! ' + str(round(latency, 2)) + ' ms')
@bot.command()
async def everyone(ctx):
    i = 0
    for i in range(1):
        await ctx.message.delete()
        await ctx.send(ctx.message.guild.default_role, delete_after=0.1)
        time.sleep(1)
@bot.command()
async def help(ctx, *, category=None):
    if category == 'ww2':
        ctx.send("=ww2 bob - Battle of Britain\n=ww2 tov - Treaty of Versailles")
    else:
        author = ctx.message.author
        embed = discord.Embed(
            title='YG Bot Help',
            colour = discord.Colour.orange()
        )
        embed.add_field(name='ping', value='Returns the latency!', inline=False)
        embed.add_field(name='World War 2', value="Exclusive WW2 commands! Input '=help ww2' for details!")
        embed.add_field(name='Moderation', value='Kick, ban and others, =help mod for details!', inline=False)
        await ctx.send(embed=embed)
@bot.command()
async def kick(ctx, member: discord.Member, *, reason='{reason}'):
    await member.kick(reason=reason)
    msg = f"{member} has been kicked because {reason}. And don't worry, I am not sad"
    await ctx.send(msg)
    await member.create_dm.send(msg)
@bot.command()
async def mute(ctx, member: discord.Member, *, reason='{reason}'):
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    msg = f"**{member}**has been muted because {reason}. The person who muted him be like-"
    await ctx.send(msg)
    await ctx.send(file=discord.File('fail.gif'))
    await member.create_dm.send(msg)
@bot.command()
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    msg = f"{member} has been unmuted."
    await ctx.send(msg)
    await member.create_dm.send(msg)
# The WW2 show begins
@bot.command()
async def ww2(ctx, battle_name="None"):
  if battle_name.lower() == "bob":
    embed = discord.Embed(
      title='World War 2',
      colour = discord.Colour.orange()
    )
    embed.add_field(name='__Battle of Britain__', value="Battle of Britain was a full-on Air force battle between Nazi Germany's Luftwaffe and Great Britain's Royal Air force. The RAF won this battle, but many civilians were killed in Luftwaffe Bombing raids.\n After the fall of France, Adolf Hitler wanted to invade Britain, but before that, he needed air and naval superiority!\n So, the Luftwaffe started attacking RAF bases and runways, and inflicted a huge amount of damage. As a strategic plan, Churchill ordered a bombing raid over Berlin, pretty insignificant, but Hitler was furious. He ordered the Luftwaffe to focus its attacks on civilian targets.\nThis led to bombing raids over London and other cities, but gave time to the RAF to rebuild its bases.\nThe Luftwaffe launched a full-blown attack on what is known as 'Battle of Britain day' and the RAF successfully repelled it, placing air superiority in British Hands.\n**Hitler's invasion had to be postponed.**", inline=False)
    await ctx.send(embed=embed)
  elif battle_name.lower() == 'tov':
      await ctx.send("Treaty of Versailles was a treaty between the Allies and Germany after WW1 and one of the main reasoms for the rise of Hitler. Run '=tov terms' to know about the terms of the treaty!")
@bot.command()
async def tov(ctx, terms=None):
    if terms == "terms":
        await ctx.send("1) Germany can't have an Air Force \n2) It can't have an army of more than a **100,000 men**\n3) The surrender of all German colonies\n4) The return of **Alsace-Lorraine** to France\n5) Cession of some other territories to **Belgium, Lithuania, Czechoslovakia and Poland**\n6) Danzig to become a free city\n7) Plebiscites to be held in northern Schleswig to settle the Danish-German frontier.\n8) Occupation and special status for the **Saar Land** under French control\n9) Demilitarization of the **Rhineland**\n10) Germany would have to pay all war reparations to the allies\n11) **Austria** was taken from Germany and made a seperate country\n12) Germany has to take full responsibity for starting the War\n13) Provision for the trial of the former Kaiser and other war leaders.\nGermany felt extremely humiliated by all this, and nobody was madder about the treaty than Hitler. He made fiery speeches against it which rose him to prominence ")
        await ctx.send(file=discord.File('map.png'))
bot.run('ODk1NTU4MDI0NjI0NzM4MzU1.YV6TZw.bHmbu8UqiYNuTnS627umihldq7A')
