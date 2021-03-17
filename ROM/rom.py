import datetime
import time
import sys
import discord
import asyncio
import json
from ColorHandler import adbHandler, colorHandler, textHandler

with open('..\\Setting.json','r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

def searchMem(name):
    user = bot.get_all_members()
    for m in user:
        if m.name == name:
            return m.id

def get_now():
    return time.strftime('%d%b%Y - %p %I:%M:%S', time.localtime())

def isTimeToStart(inputTime):
    hour = datetime.datetime.now().strftime("%#H")
    hour = int(hour)
    inputTime = int(inputTime)
    timeUp = inputTime + 4
    if hour >= inputTime and hour <= timeUp:
        return True
    else:
        return False

def getTheWaittingTime(inputTime):
    hour = datetime.datetime.now().strftime("%H")
    min = datetime.datetime.now().strftime("%#M")
    year = datetime.datetime.now().strftime("%#Y")
    m = datetime.datetime.now().strftime("%#m")
    day = datetime.datetime.now().strftime("%#d")
    iHour = int(hour)
    iMin = int(min)
    iYear = int(year)
    iM = int(m)
    iDay = int(day)
    time = int(inputTime)
    if iHour >= 12 and iHour <= 23 and time == 5:
        a = datetime.datetime(iYear, iM, iDay + 1, time)
    else:
        a = datetime.datetime(iYear, iM, iDay, time)
    b = datetime.datetime(iYear, iM, iDay, iHour, iMin)
    return (a - b).total_seconds()

def getWaittingMin(Min):
    m = 1800 - Min
    return m

# [交易所]ROM BOT
TOKEN = jdata['ROM Bot TOKEN']
bot = discord.Client()

@bot.event
async def on_ready():
    print(f"{bot.user} login.")

async def Do():
    adb = adbHandler()
    # show your em port
    adb.listDevices()

    # input the port
    print("輸入模擬器port")
    UserPort = input()

    # connect
    adb.connect(UserPort)

    # 輸入聽歌時間
    print("輸入幾點去聽歌0-23")
    InputTime = input()

    # 輸入DISCORD ID
    print("輸入DISCORD NAME")
    discordName = input()
    await  asyncio.sleep(3)

    print("開始運行..")
    await asyncio.sleep(3)
    global count
    count = 0
    global exDeleteAccount
    color = colorHandler()
    while adb.isConnect:
        if isTimeToStart(InputTime):
            # Event
            # Skip = color.findPointColor(adb)
            # if Skip > -1:
            #     adb.tap(891, 21)
            # time.sleep(3)

            # open the map#
            while True:
                time.sleep(20)
                Map = color.findColor(868, 8, 887, 14, "ffffff", adb)
                if Map[0] > -1:
                    adb.tap(897, 78)
                    time.sleep(5)
                    break
                else:
                    print("找不到地圖,請回到介面..")
                    time.sleep(20)
                    # check news 3e56ac
                    newsButton = color.findColor(297, 457, 438, 491, "3e56ac",  adb)
                    if newsButton[0] > -1:
                        adb.tap(744, 55)
                    else:
                        adb.tap(479, 461)
                    time.sleep(5)
                    continue

                time.sleep(3)

            while True:
                # 世界
                time.sleep(5)
                adb.tap(540, 363)
                time.sleep(5)
                World = color.findPointColor(49, 56, 45, 71, 153, adb)
                if World > -1:
                    adb.tap(551, 351)
                    time.sleep(5)
                    break
                else:
                    print('按不到世界')
                    time.sleep(5)
                    continue
                time.sleep(5)

            #click the music button
            while True:
                MusicLoation = color.findPointColor(314, 248, 202, 128, 0, adb)
                if MusicLoation > -1:
                    adb.tap(357, 251)
                    break
                else:
                    print("找不到音樂按鍵..")
                    await asyncio.sleep(5)
                    continue
                time.sleep(3)


            # find the way util close the window
            while True:
                closeWindow = color.findMutiPointColor(852, 14, 566, 506, 188, 22, 16, 69, 96, 173, adb)
                if closeWindow[0] > -1:
                    adb.tap(862, 24)
                    await asyncio.sleep(3)
                    break
                else:
                    print("尋路中..")
                    await asyncio.sleep(5)
                    continue
            time.sleep(3)

            # checking the 30min
            # 1.open more
            while True:
                # MoreButton
                MoreButton = color.findPointColor(809, 43, 237, 255, 254, adb)
                if MoreButton > -1:
                    adb.tap(809, 43)
                    time.sleep(3)
                    # settiing
                    if color.findPointColor(718, 300, 236, 255, 254, adb) > -1:
                        break
                    else:
                        adb.tap(809, 43)
                    break
                else:
                    print("尋找主介面更多按鍵中..")
                    time.sleep(5)
                    continue
            time.sleep(3)

            # 2.find the setting button
            while True:
                #e7a273
                SettingButton = color.findPointColor(718, 300, 236, 255, 254, adb)
                #SettingButton = color.findPointColor(718, 300, 236, 255, 254, adb)
                if SettingButton > -1:
                    adb.tap(718, 300)
                    break
                else:
                    print("尋找設置按鍵中..")
                    time.sleep(5)
                    continue
                time.sleep(5)

            time.sleep(3)

            # 3.checking the 30 mins
            text = textHandler()
            MinTime = text.orc(412, 140, 427, 154, "30", adb)
            if MinTime > -1:
                adb.tap(320, 116)
                time.sleep(3)

                # check the cool down account
                print("檢測冷卻帳號..")
                # 左
                cool1 = color.findColor(84, 137, 92, 143, "efbbc1", adb)
                if cool1[0] > -1 and count < 3:
                    count = 1
                    exDeleteAccount = True
                    print("存在正在冷卻帳號..左")
                else:
                    exDeleteAccount = False

                time.sleep(3)

                # 右
                cool2 = color.findColor(185, 135, 195, 142, "efbbc1", adb)
                if cool2[0] > -1 and count < 3:
                    count = 0
                    exDeleteAccount = True
                    print("存在正在冷卻帳號..右")
                else:
                    exDeleteAccount = False

                time.sleep(3)

                # only 2 account
                if count == 0 and exDeleteAccount == False:
                    # 左
                    accOne = color.findPointColor(142, 154, 37, 100, 195, adb)
                    if accOne > -1:
                        adb.tap(121, 122)
                        time.sleep(3)
                        print("第一帳號聽歌完成  進入左帳號")

                        # confirm
                        Confirm = color.findColor(500, 237, 637, 276, "46a60e", adb)
                        if Confirm[0] > -1:
                            adb.tap(534, 267)
                            count += 1
                            time.sleep(10)
                    else:
                        adb.tap(212, 125)
                        time.sleep(3)
                        print("第一帳號聽歌完成 進入右帳號")

                        # confirm
                        Confirm = color.findColor(500, 237, 637, 276, "46a60e", adb)
                        if Confirm[0] > -1:
                            adb.tap(534, 267)
                            count = 3
                            time.sleep(10)

                elif count == 1 and exDeleteAccount == False:
                    # 右
                    adb.tap(212, 125)
                    time.sleep(3)
                    print("第二帳號聽歌完成")

                    # confirm
                    Confirm = color.findColor(500, 237, 637, 276, "46a60e", adb)
                    if Confirm[0] > -1:
                        adb.tap(534, 267)
                        count = 3
                        time.sleep(10)
                elif count == 0 and exDeleteAccount == True:
                    # 3號刪除
                    adb.tap(119, 126)
                    time.sleep(3)
                    print("第一帳號聽歌完成*")

                    # confirm
                    Confirm = color.findColor(500, 237, 637, 276, "46a60e", adb)
                    if Confirm[0] > -1:
                        adb.tap(534, 267)
                        time.sleep(10)
                    count = 3
                elif count == 1 and exDeleteAccount == True:
                    # 2號刪除
                    adb.tap(212, 125)
                    time.sleep(3)
                    print("第一帳號聽歌完成#")

                    # confirm
                    Confirm = color.findColor(500, 237, 637, 276, "46a60e", adb)
                    if Confirm[0] > -1:
                        adb.tap(534, 267)
                        count = 3
                        time.sleep(10)

                else:
                    # send the discord message
                    while True:
                        if bot.is_ready():
                            await bot.get_channel(427400359032520704).send(get_now() + '聽完歌')
                            break

                    await asyncio.sleep(13)
                    sys.exit("完成")
            else:
                # gameMin = findTheNum(383, 1   40, 456, 156, adb)
                waitTime = 900
                adb.tap(591, 75)
                print("聽歌ING...")
                time.sleep(waitTime)
        else:
            gameWaitTime = getTheWaittingTime(InputTime)
            gameWaitTime += 60
            gTime = gameWaitTime / 60
            gHour = 0
            while gTime >= 60:
                gHour += 1
                gTime -= 60
            if gameWaitTime < 0:
                gameWaitTime = 0
                print("請等候", gHour, "小時", int(gTime), "分鐘")
                time.sleep(gameWaitTime)
                continue


bot.loop.create_task(Do())
bot.run(TOKEN)
