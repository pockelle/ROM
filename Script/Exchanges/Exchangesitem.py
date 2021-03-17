import time
import discord
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
        await bot.get_channel(814102824233205791).send(get_now() + "\n""裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
        # 英靈團 ID
        await bot.get_channel(814755925499183124).send(get_now() + "\n""裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
        # 交易所 7Days ID
        await bot.get_channel(815253957886607371).send(get_now() + "\n""裝備 : " + item + "\n""消耗積分 : " + POINTS + HOT_ITEM)
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
        # # await bot.get_channel( #ID ).send(get_now() + "\n" "裝備 : " + item + "\n""Zeny : " + ZENY)
        # 向西 ID
        await bot.get_channel(814102824233205791).send(get_now() + "\n""裝備 : " + item + "\n""Zeny : " + ZENY + HOT_ITEM)
        # 英靈團 ID
        await bot.get_channel(814755925499183124).send(get_now() + "\n""裝備 : " + item + "\n""Zeny : " + ZENY + HOT_ITEM)
        # 交易所 7Days ID
        await bot.get_channel(815253957886607371).send(get_now() + "\n""裝備 : " + item + "\n""Zeny : " + ZENY + HOT_ITEM)
        # 中BBB
        # await bot.get_channel(427400359032520704).send(get_now() + "\n" "裝備 : " + item + "\n""Zeny : " + ZENY +"\n" + HOT_ITEM)

# [交易所]ROM BOT
TOKEN = jdata['ROM Bot TOKEN']

bot = discord.Client()

@bot.event
async def on_ready():
    print(f"{bot.user} login.")

async def Do():
    adb = adbHandler()
    UserPort = '5577'

    # connect
    adb.connect(UserPort)

    print("開始運行..")
    color = colorHandler()
    text = textHandler()

    # For Loop 裝備
    onlyme = ('獻祭之書', '束縛之約')
    item = jdata['Open_input_item']

    while adb.isConnect:
        # onlyme left
        for index, num in enumerate(onlyme):
            # click search
            adb.tap(189, 121)
            time.sleep(5)

            # find item
            adb.tap(414, 137)
            time.sleep(4)

            # input item
            os.system(
                "adb -s 127.0.0.1:" + UserPort + " shell am broadcast -a ADB_INPUT_B64 --es msg '" + to_64(num) + "'")
            time.sleep(5)

            # click yellow serch
            for x in range(2):
                adb.tap(707, 136)
                time.sleep(3)

            # Tap Left side
            adb.tap(468, 206)
            time.sleep(5)

            # 有沒有粉紅波利
            noitem = color.findPointColor(558, 323, 242, 189, 171, adb)
            if noitem > -1:
                # print('NOITEM')
                continue
            else:
                # 精練 ↑
                for x in range(2):
                    adb.tap(628, 67)
                    time.sleep(1)

            time.sleep(1)

            # high light top item
            adb.tap(410, 146)
            time.sleep(3)

            # tab to buy
            adb.tap(804, 487)
            time.sleep(3)

            # check +15
            # check +10 - +15 (X1 , Y1 , X2, Y2 )(276, 64, 305, 83)
            Fiveteen = text.orc(276, 64, 305, 83, "+15", adb)
            if Fiveteen > -1:
                print("+15" + num)
                # Note Discord
                price = text.findTheNum(316, 383, 441, 409, adb)
                ZENY = str(price[:-1])
                hot = text.findhot(530, 110, 729, 138, adb)
                HOT_ITEM = str(hot[:-2])
                await bot.wait_until_ready()
                if bot.is_ready():
                    await bot.get_channel(427400359032520704).send(
                        get_now() + "\n" "裝備 : " + num + "\n""Zeny : " + ZENY + HOT_ITEM)

                time.sleep(2)

            # 按取消
            adb.tap(258, 452)
            time.sleep(2)
        # onlyme right
        for index, num in enumerate(onlyme):
            # click search
            adb.tap(189, 121)
            time.sleep(5)

            # find item
            adb.tap(414, 137)
            time.sleep(4)

            # input item
            os.system(
                "adb -s 127.0.0.1:" + UserPort + " shell am broadcast -a ADB_INPUT_B64 --es msg '" + to_64(num) + "'")
            time.sleep(5)

            # click yellow serch
            for x in range(2):
                adb.tap(707, 136)
                time.sleep(3)

            # Tap right side
            adb.tap(639, 207)
            time.sleep(2)
            tureback = color.findPointColor(770, 490, 255, 158, 25, adb)
            if tureback > -1:
                time.sleep(1)
            else:
                adb.tap(733, 91)
                time.sleep(1)

            # 有沒有粉紅波利
            noitem = color.findPointColor(558, 323, 242, 189, 171, adb)
            if noitem > -1:
                # print('NOITEM')
                continue
            else:
                # 精練 ↑
                for x in range(2):
                    adb.tap(628, 67)
                    time.sleep(1)

            time.sleep(1)

            # high light top item
            adb.tap(410, 146)
            time.sleep(3)

            # tab to buy
            adb.tap(804, 487)
            time.sleep(3)

            # check +15
            # check +10 - +15 (X1 , Y1 , X2, Y2 )(276, 64, 305, 83)
            Fiveteen = text.orc(276, 64, 305, 83, "+15", adb)
            if Fiveteen > -1:
                print("+15" + num)
                # Note Discord
                price = text.findTheNum(316, 383, 441, 409, adb)
                ZENY = str(price[:-1])
                hot = text.findhot(530, 110, 729, 138, adb)
                HOT_ITEM = str(hot[:-2])
                await bot.wait_until_ready()
                if bot.is_ready():
                    await bot.get_channel(427400359032520704).send(
                        get_now() + "\n" "裝備 : " + num + "\n""Zeny : " + ZENY + HOT_ITEM)

                time.sleep(2)
            # 按取消
            adb.tap(258, 452)
            time.sleep(2)

        # left side
        for index, num in enumerate(item):
            # click search
            adb.tap(189, 121)
            time.sleep(5)

            # find item
            adb.tap(414, 137)
            time.sleep(4)

            # input item
            os.system(
                "adb -s 127.0.0.1:" + UserPort + " shell am broadcast -a ADB_INPUT_B64 --es msg '" + to_64(num) + "'")
            time.sleep(5)

            # click yellow serch
            for x in range(2):
                adb.tap(707, 136)
                time.sleep(3)

            # Tap Left side
            adb.tap(468, 206)
            time.sleep(2)

            # 有沒有粉紅波利
            noitem = color.findPointColor(558, 323, 242, 189, 171, adb)
            if noitem > -1:
                # print('NOITEM')
                continue
            else:
                # 精練 ↑
                for x in range(2):
                    adb.tap(628, 67)
                    time.sleep(1)

            time.sleep(1)

            # high light top item
            adb.tap(410, 146)
            time.sleep(3)

            # tab to buy
            adb.tap(804, 487)
            time.sleep(3)

            # check +15
            # check +10 - +15 (X1 , Y1 , X2, Y2 )(276, 64, 305, 83)
            if num == ('納戶特基格的斗篷'):
                Fiveteen = text.orc(275, 64, 300, 81, "+15", adb)
                if Fiveteen > -1:
                    print("+15" + num)
                    # Note Discord
                    await Zeny("+15" + num, text, adb)
            else:
                Fiveteen = text.orc(276, 64, 305, 83, "+15", adb)
                if Fiveteen > -1:
                    print("+15" + num)
                    # Note Discord
                    await Zeny("+15" + num, text, adb)

                    time.sleep(2)

            # 按取消
            adb.tap(258, 452)
            time.sleep(2)
        # right side
        for index, num in enumerate(item):
            # click search
            adb.tap(189, 121)
            time.sleep(5)

            # find item
            adb.tap(414, 137)
            time.sleep(4)

            # input item
            os.system(
                "adb -s 127.0.0.1:" + UserPort + " shell am broadcast -a ADB_INPUT_B64 --es msg '" + to_64(num) + "'")
            time.sleep(5)

            # click yellow serch
            for x in range(2):
                adb.tap(707, 136)
                time.sleep(3)

            # Tap right side
            adb.tap(639, 207)
            time.sleep(2)
            tureback = color.findPointColor(770, 490, 255, 158, 25, adb)
            if tureback > -1:
                time.sleep(1)
            else:
                adb.tap(733, 91)
                time.sleep(1)

            # 有沒有粉紅波利
            noitem = color.findPointColor(558, 323, 242, 189, 171, adb)
            if noitem > -1:
                # print('NOITEM')
                continue
            else:
                # 精練 ↑
                for x in range(2):
                    adb.tap(628, 67)
                    time.sleep(1)

            time.sleep(1)

            # high light top item
            adb.tap(410, 146)
            time.sleep(3)

            # tab to buy
            adb.tap(804, 487)
            time.sleep(3)

            # check +15
            # check +10 - +15 (X1 , Y1 , X2, Y2 )(276, 64, 305, 83)
            if num == ('納戶特基格的斗篷'):
                Fiveteen = text.orc(275, 64, 300, 81, "+15", adb)
                if Fiveteen > -1:
                    print("+15" + num)
                    # Note Discord
                    await Zeny("+15" + num, text, adb)
            else:
                Fiveteen = text.orc(276, 64, 305, 83, "+15", adb)
                if Fiveteen > -1:
                    print("+15" + num)
                    # Note Discord
                    await Zeny("+15" + num, text, adb)

                time.sleep(2)

            # 按取消
            adb.tap(258, 452)
            time.sleep(2)

        print(get_now() + " 裝備 : WAITING 600 SEC RECHECK")
        time.sleep(600)

bot.loop.create_task(Do())
bot.run(TOKEN)