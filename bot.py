import discord
import datas
admins = datas.get_admin()
bot_command = discord.SlashCommandGroup('bot', '機器人')
guild_id = [991254723745288303]


@bot_command.command(description='機器人的資訊')
async def info(ctx):
	await ctx.defer()
	embed = discord.Embed(
		title='Godot TW', description='我是台灣Godot 社群機器人 :D', color=discord.Colour.blurple())
	embed.add_field(name='生日', value='10月26日 2022')
	embed.add_field(name='ID', value='998505359096430662')
	embed.set_thumbnail(url="https://i.imgur.com/Nq09oyw.png")
	await ctx.followup.send("這是我的身分證 :D", embed=embed)


@bot_command.command(description='重新載入機器人')
async def reload_bot(ctx):
	await ctx.defer()
	if ctx.author.guild_permissions.administrator:
		datas.datas = datas.load_data()
		await ctx.followup.respond('正在重新載入!!')
	else:
		await ctx.followup.respond('你沒有指令權限!!')


@bot_command.command(description='儲存機器人數據')
async def save_data(ctx):
	file = discord.File('Datas.json')
	await ctx.defer()
	await ctx.followup.send(file=file, content='好了 :D')
