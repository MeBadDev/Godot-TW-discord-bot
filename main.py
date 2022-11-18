import discord
import datas
from dotenv import load_dotenv
from os import getenv
bot = discord.Bot()
@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")

@bot.slash_command(description = "Godot新手教學資源",guild_ids=[991254723745288303])
async def tutorials(ctx):
	await ctx.respond("""
Step By Step: https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html
GDQuest: https://www.youtube.com/c/Gdquest
Heart Beast: https://www.youtube.com/c/uheartbeast
""")
#get object document
@bot.slash_command(description = "獲得任何物件的文檔",guild_ids=[991254723745288303])
async def objects(ctx,nodes:str):
	link = 'https://docs.godotengine.org/en/stable/classes/class_%s.html' % nodes.lower()
	await ctx.respond(link)
@bot.slash_command(description = '給金幣!!',guild_ids = [991254723745288303])
#give people coin
async def give_coin(ctx,amount:int,user:discord.Option(discord.SlashCommandOptionType.user)):
	if ctx.author.id in datas.datas['Admins']:
		datas.add_coin(user.id,amount)
		await ctx.respond('<@%s> 送了 <@%s> %s:coin:!!' % (ctx.author.id,user.id,amount))
	else:
		coin_count = datas.get_coin(ctx.author.id)
		if coin_count < amount:
			await ctx.respond("你沒有足夠的金幣!!")
		else:
			datas.datas['Coins'][str(ctx.author.id)] -= amount
			await ctx.respond('<@%s> 給了 <@%s> %s:coin:!!' % (ctx.author.id,user.id,amount))
			
	 
#how much coin do we have?
@bot.slash_command(description = '有多少金幣?',guild_ids = [991254723745288303])
async def coins(ctx,user:discord.Option(discord.SlashCommandOptionType.user)):
	await ctx.respond('<@%s> 有 %s:coin:!!' % (user.id,datas.get_coin(user.id)))
load_dotenv()
bot.run(getenv('TOKEN'))