import turtle
class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
    
    def __drawHead(self):
        if Face.isHappy(self) == True:
            fillhead = "yellow"
        else:
            fillhead = "red"
        turtle.setposition(0,-50)
        turtle.fillcolor(fillhead)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    def __drawEyes(self):
        if Face.isDarkEyes(self) == True:
            filleyes = "black"
        else:
            filleyes = "blue"
        turtle.pu()
        turtle.setposition(-25,75)
        turtle.pd()
        turtle.fillcolor(filleyes)
        turtle.begin_fill()
        turtle.circle(10)
        turtle.pu()
        turtle.forward(50)
        turtle.pd()
        turtle.circle(10)
        turtle.end_fill()

    def __drawMouth(self):
        if Face.isSmile(self) == True:
            num = 50
            angle = -25
        else:
            num = -50
            angle = 25
        turtle.pu()
        turtle.setposition(-30,-5)
        turtle.pd()
        turtle.pencolor("black")
        turtle.pensize(2)
        turtle.setheading(angle)
        turtle.circle(80,num)
        turtle.pu()

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile
    def isHappy(self):
        return self.__happy
    def isDarkEyes(self):
        return self.__darkEyes
    def changeMouth(self):
        self.__smile = False
        self.draw_face()
    def changeEmotion(self):
        self.__happy = False
        self.draw_face()
    def changeEyes(self):
        self.__darkEyes = False
        self.draw_face()

def main():
    face = Face()
    face.draw_face()
    done = False
    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else  "happy"
        eyes = "blue" if face.isDarkEyes else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")
        menu = eval(input("Enter a selection: "))
        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes
        else:
            break
main()
print("Thanks for Playing")
turtle.hideturtle()
turtle.done()


