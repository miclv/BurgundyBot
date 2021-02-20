import discord


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(selfself, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('ODEyMzkzNTAyNjMzMzYxNDM5.YDAGaA.ry1Pg_sO2Q9_C-BrB-5c0RRNffc')