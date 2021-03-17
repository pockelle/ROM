import datetime
import time
import discord
import sys
import os
import base64
import json
from Script.ColorHandler import adbHandler, colorHandler, textHandler

with open('C:\\Users\\Nino\\PycharmProjects\\pythonProject\\Script\\Setting.json','r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

def searchMem(name):
    user = bot.get_all_members()
    for m in user:
        if m.name == name:
            return m.id

def card(adb):
    time.sleep(3)
    # print('high light top item')
    adb.tap(410, 146)
    time.sleep(3)
    # tab to buy
    adb.tap(804, 487)
    time.sleep(3)

def to_64(text):
    mess_bytes = text.encode('utf-8')
    text64 = base64.b64encode(mess_bytes)
    return text64.decode('utf-8')

def get_now():
    return time.strftime('%d%b%Y - %p %I:%M:%S', time.localtime())

# 消耗積分
async def Points(item, text, adb):
    price = text.findTheNum(318, 392, 448, 413, adb)
    POINTS = str(price[:-1])
    hot = text.findhot(530, 110, 729, 138, adb)
    HOT_ITEM = str(hot[:-2])

    await bot.wait_until_ready()
    if bot.is_ready():
        # await bot.get_channel( #ID ).send(get_now() + "\n" "裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
        # 向西 ID
        await bot.get_channel(814102824233205791).send(
            get_now() + "\n""裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
        # 英靈團 ID
        await bot.get_channel(814755925499183124).send(
            get_now() + "\n""裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
        # 交易所 7Days ID
        await bot.get_channel(815253957886607371).send(
            get_now() + "\n""裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
        # # 中BBB
        # await bot.get_channel(427400359032520704).send(get_now() + "\n" "裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)

# ZENY
async def Zeny(item, text, adb):
    price = text.findTheNum(316, 383, 441, 409, adb)
    ZENY = str(price[:-1])
    hot = text.findhot(530, 110, 729, 138, adb)
    HOT_ITEM = str(hot[:-2])

    await bot.wait_until_ready()
    if bot.is_ready():
        # await bot.get_channel( #ID ).send(get_now() + "\n" "裝備 : " + item + "\n""Zeny : " + ZENY)
        # 向西 ID
        await bot.get_channel(814102824233205791).send(get_now() + "\n""裝備 : " + item + "\n""Zeny : " + ZENY + HOT_ITEM)
         # 英靈團 ID
        await bot.get_channel(814755925499183124).send(get_now() + "\n""裝備 : " + item + "\n""Zeny : " + ZENY + HOT_ITEM)
         # 交易所 7Days ID
        await bot.get_channel(815253957886607371).send(get_now() + "\n""裝備 : " + item + "\n""Zeny : " + ZENY + HOT_ITEM)
        # 中BBB
        # await bot.get_channel(427400359032520704).send(get_now() + "\n" "裝備 : " + item + "\n""Zeny : " + ZENY +"\n" + HOT_ITEM)

# [交易所]ROM BOT
TOKEN = jdata["ROM Bot TOKEN"]

bot = discord.Client()

@bot.event
async def on_ready():
    print(f"{bot.user} login.")

async def Do():
    adb = adbHandler()
    UserPort = '5571'

    # connect
    adb.connect(UserPort)

    print("開始運行..")
    color = colorHandler()
    text = textHandler()

    # input item
    Card = jdata["Open_input_card"]

    # +15 find point
    # 納戶特基格的斗篷 = text.orc(272, 64, 303, 84, "+15", adb)

    while adb.isConnect:
        # Card
        for index, num in enumerate(Card):
            # click search
            adb.tap(189, 121)
            time.sleep(5)

            # find item
            adb.tap(414, 137)
            time.sleep(4)

            # input item
            os.system("adb -s 127.0.0.1:" + UserPort + " shell am broadcast -a ADB_INPUT_B64 --es msg '" + to_64(
                num) + "'")
            time.sleep(5)

            # click yellow serch
            for x in range(2):
                adb.tap(707, 136)
                time.sleep(2)

            time.sleep(2)
            # Tap Left side
            adb.tap(468, 206)
            time.sleep(2)

            # 有沒有粉紅波利
            noitem = color.findPointColor(558, 323, 242, 189, 171, adb)
            if noitem > -1:
                # print('NOITEM')
                time.sleep(2)
                continue
            else:
                time.sleep(2)
                card(adb)
                points = color.findPointColor(307, 401, 101, 211, 171, adb)
                if points > -1:
                    await Points(num, text, adb)
                else:
                    await Zeny(num, text, adb)
                time.sleep(2)
                # 按取消
                adb.tap(258, 452)
                time.sleep(2)

        print(get_now() + " 裝備 : WAITING 300 SEC RECHECK")
        time.sleep(300)

bot.loop.create_task(Do())
bot.run(TOKEN)