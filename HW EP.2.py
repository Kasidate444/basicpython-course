import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า

def Triangle():
    '''วาดสามเหลี่ยม'''
    for i in range(3):
        tao.forward(100)
        tao.left(120)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(150,150)
Triangle()
