import discord
from discord.ext import commands
import requests
import json
from apscheduler.schedulers.asyncio import AsyncIOScheduler

def get_meme():
  response = requests.get('http://3650000.xyz/api?type=json&mode=1')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler = AsyncIOScheduler()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(f'{self.user} 已连接到 Discord!')

            # 定义定时任务：每天的特定时间发送消息
        self.scheduler.add_job(self.send_scheduled_message, 'cron', hour=8, minute=0, args=[1223565631434264636,get_meme()])

            # 启动调度器
        self.scheduler.start()

    async def send_scheduled_message(self, channel_id, message):
        channel = self.get_channel(1223565631434264636)
        if channel:
            await channel.send(message)


    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('test') # Replace with your own token.


