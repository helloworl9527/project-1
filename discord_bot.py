import discord
from discord.ext import commands
import requests
import json
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import httpx
import asyncio

def get_meme(type):
    if type == 1:
        response = requests.get('https://t.mwm.moe/pc?json')   #横版壁纸
        json_data = json.loads(response.text)
        return json_data['url']
    elif type == 2:
        response = requests.get('https://t.mwm.moe/mp?json')    #竖屏壁纸
        json_data = json.loads(response.text)
        return json_data['url']
    elif type == 3:
        response = requests.get('http://3650000.xyz/api?type=json&mode=1')    #竖屏壁纸
        json_data = json.loads(response.text)
        return json_data['url']

# async def submit_image_to_api(image_path):
#     url = 'https://aiapiv2.animedb.cn/ai/api/detect?force_one=1&model=anime'
#     async with httpx.AsyncClient() as client:
#         response = await client.post(url, files={'file': ('image.jpg', httpx.get(image_path).content, 'image/jpeg')})
#         print(response.text)




class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler = AsyncIOScheduler()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(f'{self.user} 已连接到 Discord!')

            # 定义定时任务：每天的特定时间发送消息
        self.scheduler.add_job(self.send_scheduled_message, 'cron', hour=11, minute=20, args=[1223565631434264636,get_meme(type=1)])

            # 启动调度器
        self.scheduler.start()

    async def send_scheduled_message(self, channel_id, message):
        channel = self.get_channel(1223565631434264636)
        if channel:
            await channel.send(message)


       
# 在你的代码中调用这个函数来提交文件到API地址
        
    
    async def on_message(self, message):
        if message.author == self.user:
            return
#发送消息命令
        if message.content.startswith('Animepc'):
            await message.channel.send(get_meme(type=1))
        elif message.content.startswith('Animemp'):
            await message.channel.send(get_meme(type=2))
        elif message.content.startswith('Meimei'):
            await message.channel.send(get_meme(type=3))
        elif message.attachments:  # 检查消息是否包含附件
            for attachment in message.attachments:

                if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif']):
                    # 在这里处理图片
                    print(f"Received image: {attachment.url}")
                    await message.channel.send(f"图片已接收！{attachment.url}")
                    url = attachment.url
                    response = requests.get(url)
                    with open('local_image.jpg', 'wb') as f:
                        f.write(response.content)

                    with open('local_image.jpg', 'rb') as f:
                        files = {'image': f}
                        r = httpx.post('https://aiapiv2.animedb.cn/ai/api/detect?force_one=0&model=anime&ai_detect=2', data=None, files=files, timeout=30)
                        response_json = r.json()
                        name_value = response_json['data'][0]['name']
                        cartoonname_value = response_json['data'][0]['cartoonname']
                        print(name_value, cartoonname_value)




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('#') # Replace with your own token.


