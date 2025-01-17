import turtle
import time
import random 

WIDTH, HEIGHT = 500, 500
COLORS = ["red","green", "yellow", "black","pink", "cyan", "blue","orange", "purple","brown"]

def get_number_of_racers():
    racers =0
    while True:
        try: 
            racers =int(input(" Enter the numbers: (2~10): "))
            if 2 <= racers <=10:
                return racers
            else:
                print("Need to between 2 to 10.")
                continue   #這必須存在，因為下面還有程式馬，如果沒有這行，程式會結束
        except:
            print("Need to be numeric...Try again!")
            continue
        return

def race(colors):
    turtles = creat_turtle(colors)
    while True:
        for racer in turtles:
            distance =random.randrange(1,20)
            racer.forward(distance)
            x , y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]



def creat_turtle(colors):
    turtles =[]
    space_between = WIDTH // (len(colors)+1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * space_between,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles



def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')



racers = get_number_of_racers()  #如果想列印出東西，必須先將這個存入變數
init_turtle()


random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
time.sleep(3)

#要把烏龜跑的縣拿掉
#要做一些變化 例如讓烏龜永遠跑不到終點

