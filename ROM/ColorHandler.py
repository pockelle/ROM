from PIL import Image
import math
from ppadb.client import Client as AdbClient
import subprocess
import pytesseract
import cv2
import sys

class adbHandler:
    isConnect = False
    device = None

    def connect(self, UserPort):
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.device("127.0.0.1:" + UserPort)
        if device is None:
            # print("找不到模擬器")
            self.isConnect = False
            sys.exit("找不到模擬器")
        else:
            # print("找到模擬器")
            self.device = device
            self.isConnect = True

    def screenCut(self):
        if self.isConnect is True:
            result = self.device.screencap()
            with open("screen.png", "wb") as fp:
                fp.write(result)
            return Image.open('screen.png')

    def listDevices(self):
        try:
            deviceInfo = subprocess.check_output("adb devices -l", shell=True).decode("UTF-8")
            print(deviceInfo)
        except:
            print("模擬器adb.exe 發生問題")

    def tap(self, x, y):
        self.device.input_tap(x, y)

    def swipe(self, x1, y1, x2, y2, speed):
        self.device.input_swipe(x1, y1, x2, y2, speed)

    def text(self, text):
        self.device.input_text(text)

    def getDevice(self):
        return self.device

    def tapKey(self, keyCode):
        self.device.input_keyevent(keycode=keyCode)

class colorHandler:

    def findColor(self, x1, y1, x2, y2, color, device):
        img = device.screenCut()
        i = 1
        j = 1
        s1 = 0
        s2 = 0
        result = 0
        break_flag = False
        ColorHex = tuple(int(color[k:k + 2], 16) for k in (0, 2, 4))

        if (x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0):
            width = img.size[0]
            height = img.size[1]
        else:
            s1 = x1
            s2 = y1
            width = x2
            height = y2
            # CheckTheTime(img,x1,x2,y1,y2)

        for i in range(s1, width):
            for j in range(s2, height):
                data = img.getpixel((i, j))
                if (data[0] == ColorHex[0] and data[1] == ColorHex[1] and data[2] == ColorHex[2]):
                    result = 1
                    # print("圖片存在像素！")
                    return 0, i, j

        if (result == 0):
            return -1, 0, 0
            # print("圖片不存在像素！")

    def findMutiColor(self, x1, y1, x2, y2, aR, aG, aB, bR, bG, bB, device):
        img = device.screenCut()
        i = 1
        j = 1
        s1 = 0
        s2 = 0
        intX = 0
        intY = 0
        intX2 = 0
        intY2 = 0
        isAExist = False
        isBExist = False

        if (x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0):
            width = img.size[0]
            height = img.size[1]
        else:
            s1 = x1
            s2 = y1
            width = x2
            height = y2

        for i in range(s1, width):
            for j in range(s2, height):
                Color = (img.getpixel((i, j)))

                if Color[0] == aR and Color[1] == aG and Color[2] == aB and isAExist == False:
                    # A Color Exist
                    isAExist = True
                    intX = i
                    intY = j
                elif Color[0] == bR and Color[1] == bG and Color[2] == bB and isBExist == False:
                    # B Color Exist
                    isBExist = True
                    intX2 = i
                    intY2 = j
                if isAExist is True and isBExist is True:
                    return 0, intX, intY, intX2, intY2

        if isAExist is False or isBExist is False:
            return -1, 0, 0, 0, 0

    def findPointColor(self, x, y, colorR, colorG, colorB, device):
        img = device.screenCut()
        color = img.getpixel((x, y))
        if colorR == color[0] and colorG == color[1] and colorB == color[2]:
            return 0
        elif self.colorCompare(colorR, colorB, colorG, color[0], color[1], color[2], 70):
            return 0
        else:
            return -1

    def findMutiPointColor(self, x1, y1, x2, y2, aR, aG, aB, bR, bG, bB, device):
        img = device.screenCut()
        aColor = img.getpixel((x1, y1))
        bColor = img.getpixel((x2, y2))
        if (aR == aColor[0] and aG == aColor[1] and aB == aColor[2]) and (
                bR == bColor[0] and bG == bColor[1] and bB == bColor[2]):
            return 0, x1, y1, x2, y2
        elif self.colorCompare(aR, aB, aG, aColor[0], aColor[1], aColor[2], 70) and self.colorCompare(bR, bG, bB, bColor[0], bColor[1], bColor[2], 70):
            return 0, x1, y1, x2, y2
        else:
            return -1, 0, 0, 0, 0

    def colorCompare(self, ar, ag, ab, br, bg, bb, colorSim):
        #distance = 70
        absR = ar - br
        absG = ag - bg
        absB = ab - bb
        if math.sqrt(absR * absR + absG * absG + absB * absB) < colorSim:
            return True
        else:
            return False

    def findBagItemColor(self, aR, aG, aB, bR, bG, bB, device):
        pass


class textHandler:

    def orc(self, x1, y1, x2, y2, InputText, device):
        img = device.screenCut()
        # pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'

        if (x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0):
            width = img.size[0]
            height = img.size[1]
            CutImg = cv2.imread("screen.png")
            CropImg = CutImg[0:height, 0:width]
            text = pytesseract.image_to_string(CropImg, lang="chi_tra+eng")
        else:
            CutImg = cv2.imread("screen.png")
            CropImg = CutImg[y1:y2, x1:x2]
            text = pytesseract.image_to_string(CropImg, lang="chi_tra+eng")
        if (text.splitlines()[0] == InputText):
            return 0
        else:
            return -1

    def findTheNum(self, x1, y1, x2, y2, device: adbHandler):
        device.screenCut()
        CutImg = cv2.imread("screen.png")
        CropImg = CutImg[y1:y2, x1:x2]
        text = pytesseract.image_to_string(CropImg, lang='chi_tra+eng')
        return text


    def toboxs(self, device):
        device.screenCut()
        CutImg = cv2.imread("screen.png")
        text = pytesseract.image_to_boxes(CutImg, lang="chi_tra+eng")
        return text
