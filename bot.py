import discord
import datas
admins = datas.get_admin()
bot_command = discord.SlashCommandGroup('bot', '機器人')
guild_id = [991254723745288303]


@bot_command.command(description='重新載入機器人', guild_ids=guild_id)
async def reload_bot(ctx):
    if ctx.author.id in admins:
        datas.datas = datas.load_data()
        await ctx.respond('正在重新載入!!')
    else:
        await ctx.respond('你沒有指令權限!!')


@bot_command.command(description='儲存機器人數據', guild_ids=guild_id)
async def save_data(ctx):
    file = discord.File('Datas.json')
    await ctx.defer()
    await ctx.followup.send(file=file, content='好了 :D')
