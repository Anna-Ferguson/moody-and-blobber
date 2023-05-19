import time

class Blobber:
    def __init__(self, name, color, radius, height):
        self.__radius = radius
        self.__height = height 
        self.__color = color
        self.__name = name
    def feedblobber(self, feednum):
        feednum = int(input("Enter the amount you wish to feed your Blobber: "))
        self.__radius += feednum
        self.__height += feednum
    def blobberSpeak(self, vitals):
        print("My name is " + self.__name + " I am " + self.__color)
        print("My current happiness level is " + vitals)
    def getradius(self):
        return self.__radius
    def getheight(self):
        return self.__height

    def vitalsOK(self):
        volume = (Blobber.getradius**2) * Blobber.getheight * 3.14
        x= 100
        while x >0:
            v = volume - .2
            time.sleep(1)

        percent = v/volume
        return percent
    
    def blobberOK(self):
        if 90 <= Blobber.vitalsOK <=110:
            life = True
        else:
            life = False

    #accessors
    def getname(self):
        return self.__name

    def getcolor(self):
        return self.__color

    #mutators
    
    def setname(self, name):
        self.__name = name

    def setcolor(self, color):
        self.__color = color

    def displayName(blobber):
        print("Your Blobber's name is " + blobber.getname())
    def changeName(blobber, name):
        name = input("Enter Blobber's new name: ")
        blobber.setname(name)
        blobber.displayName(blobber)
    def displayColor(blobber):
        print("Your Blobber's color is " + blobber.getcolor())
    def changeColor(blobber):
        color = input("Enter Blobber's new color: ")
        blobber.setcolor(color)
        blobber.displayColor(blobber)
    def feedBlobber(blobber):
        food = eval(input("Enter amount to you feed your Blobber: "))
        blobber.feedblobber(food)
    def blobberSpeak(blobber):
        print(blobber.blobberSpeak())