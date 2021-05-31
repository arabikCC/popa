import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
	print('я абкакался')
    

# Clear message
@bot.command (pass_context = True)
@commands.has_permissions(administrator = True)
async def clear (ctx, amount = 1000):
	await ctx.channel.purge(limit = amount)
 #kick 
@bot.command (pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.kick(reason = reason)
	await ctx.send(f'kick user {member.mention}')

#ban
@bot.command (pass_context = True)
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
	await member.ban(reason = reason)
	await ctx.send(f'ban user {member.mention}')
	

# Unban
@bot.command (pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx,*, member):
	await ctx.channel.purge(limit = 1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'Unbanned user {user.mention}')

		return

 #mute 
@bot.command (pass_context = True)
@commands.has_permissions(administrator = True)
async def mute(ctx,member:discord.Member):
	await ctx.channel.purge(limit=1)
	mute = discord.utils.get(ctx.message.guild.roles,name="mute")
	await member.add_roles(mute)
	await ctx.send(f'{member.mention} замучен')
	await asyncio.sleep(amount)
	await member.remove_roles(mute)

#unmute
@bot.command (pass_context = True)
@commands.has_permissions(administrator = True)
async def unmute(ctx, member:discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='mute')
    await member.remove_roles(mute_role)
    await ctx.send(f'{member.mention} размучен')

a = ['хуесос','отчим','сдохла']
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	else:
		content = message.content.split()
		for word in content:
			if word in a:
				await message.delete()
				await message.channel.send('Чел может у тебя мать в канаве, во первых ps 4, во вторых нормальный геймпад, с ним всё хорошо третий ты слит')
	await bot.process_commands(message)






bot.run(os.getenv('TOKEN'))