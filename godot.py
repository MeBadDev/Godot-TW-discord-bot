import discord
import datas
admins = datas.get_admin()
godot_command = discord.SlashCommandGroup('bot', '機器人')
guild_id = [991254723745288303]


@godot_command.command(description="Godot新手教學資源", guild_ids=[991254723745288303])
async def tutorials(ctx):
    await ctx.respond("""
Step By Step: https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html
GDQuest: https://www.youtube.com/c/Gdquest
Heart Beast: https://www.youtube.com/c/uheartbeast
""")

# get object document


@godot_command.command(description="獲得任何物件的文檔", guild_ids=guild_id)
async def objects(ctx, object: str):
    link = 'https://docs.godotengine.org/en/stable/classes/class_%s.html' % object.lower()
    await ctx.respond(link)
