import discord
import datas
admins = datas.get_admin()
coins_command = discord.SlashCommandGroup(
	'coins', '金幣 :money_mouth::moneybag:')
guild_id = [991254723745288303]


@coins_command.command(description='給金幣!!')
# give people coin
async def give_coin(ctx, user: discord.SlashCommandOptionType.user, amount: int):
	await ctx.defer()
	coin_count = datas.get_coin(ctx.author.id)
	if coin_count < amount:
		await ctx.followup.send("你沒有足夠的金幣!!")
	else:
		if ctx.author.id != user.id:
			datas.datas['Coins'][str(ctx.author.id)] -= amount
			await ctx.followup.send('<@%s> 給了 <@%s> %s:coin:!!' % (ctx.author.id, user.id, amount))
		else:
			await ctx.followup.send('你不能給自己金幣!')

# how much coin do we have?


@coins_command.command(description='有多少金幣?')
async def count(ctx, user: discord.SlashCommandOptionType.user):
	await ctx.defer()
	await ctx.followup.send('<@%s> 有 %s:coin:!!' % (user.id, datas.get_coin(user.id)))


@coins_command.command(description='設置金幣數量')
async def set_coin(ctx, user: discord.SlashCommandOptionType.user, amount: int):
	await ctx.defer()
	if ctx.author.guild_permissions.administrator:
		datas.set_coin(user.id, amount)
		await ctx.followup.send("<@%s> 現在有 %s:coin:!" % (user.id, amount))
	else:
		await ctx.followup.send('你沒有指令權限!!')
