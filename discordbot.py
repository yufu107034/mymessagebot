import discord   
from discord.ext import commands 
import os
TOKEN = os.environ['TOKEN']
client = discord.Client()
client = commands.Bot(command_prefix='/',help_command=None)
@client.event                             
async def on_ready():                  
    print('online')
@client.command()        
async def 回報(ctx,*,msg):
    user_msg = await client.fetch_user(954528596460986440)
    A=ctx.author.id
    await ctx.send("已收到回覆")
    await user_msg.send(f"回報者<@{A}>回報內容:"+msg)
client.run(TOKEN) 
