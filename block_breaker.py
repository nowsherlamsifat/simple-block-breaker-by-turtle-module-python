import turtle,random,sys,time

brick_number=int(input('number of blocks:'))
"""initialize"""
wn=turtle.Screen()
wn.title('pong')
wn.bgcolor('black')
wn.setup(800,600)
wn.tracer(0)

"""paddle A"""
paddle_A=turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape('square')
paddle_A.shapesize(stretch_wid=1,stretch_len=5)
paddle_A.color('red')
paddle_A.penup()
paddle_A.goto(0,-250)

"""ball"""
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('green')
ball.penup()
ball.goto(0,0)
ball_dx=1
ball_dy=1

"""brick"""
brick_box=[]

for i in range(brick_number):
    """creating object"""
    brick=turtle.Turtle()
    brick_box.append(brick)
    
    """setting object"""
    brick_box[i].speed(0)
    brick_box[i].shape('square')
    brick_box[i].shapesize(1,5)
    brick_box[i].color('blue')
    brick_box[i].penup()
    brick_box[i].goto(random.randint(-350,350),random.randint(-200,250))

"""pen"""
score=0
pen=turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0,-290)
pen.write('Score {}'.format(score),align='center',font=('comicsansms',14,'bold'))



"""movment"""
def paddle_A_Right():
    x=paddle_A.xcor()
    if x<341:
        x+=40
    paddle_A.setx(x)
    
def paddle_A_Left():
    x=paddle_A.xcor()
    if x>-341:
        x-=40
    paddle_A.setx(x)
    
wn.listen()
wn.onkeypress(paddle_A_Right,'Right')
wn.onkeypress(paddle_A_Left,'Left')

"""game finish count"""
game_finish=0

"""game_over text"""
def game_over_text():
    game_over=turtle.Turtle()
    game_over.speed(0)
    game_over.color('green')
    game_over.penup()
    game_over.hideturtle()
    game_over.goto(0,0)
    game_over.write(f' YOU GOT {score} POINT',align='center',font=('lucida',30,'bold'))

"""mainloop"""
while True:
    wn.update()
    ball.sety(ball.ycor()-ball_dy)
    ball.setx(ball.xcor()+ball_dx)
    
    if ball.ycor()>290:
        ball_dy*=-1
        
    if ball.xcor()>390:
        ball_dx*=-1
        
    if ball.ycor()<-290:
        # ball.goto(random.randint(-390,390),200)
        ball_dx*=-1
        ball_dy*=-1
        score=0
        pen.clear()
        pen.write('Score {}'.format(score),align='center',font=('comicsansms',14,'bold'))
    
    if ball.xcor()<-390:
        ball_dx*=-1
        
    if ball.ycor()<-240 and ball.ycor()>-250 and ball.xcor()<paddle_A.xcor()+50 and ball.xcor()>paddle_A.xcor()-50:
        ball_dy*=-1 
        score+=1
        pen.clear()
        pen.write('Score {}'.format(score),align='center',font=('comicsansms',14,'bold'))
    
    for i in range(brick_number):
            if ball.ycor()>brick_box[i].ycor()-10 and ball.ycor()<brick_box[i].ycor() and ball.xcor()>brick_box[i].xcor()-50 and ball.xcor()<brick_box[i].xcor()+50:
                ball_dy*=-1
                brick_box[i].setx(1000)
                score+=5
                
                pen.clear()
                pen.write('Score {}'.format(score),align='center',font=('comicsansms',14,'bold'))

                game_finish+=1

    """game over decide"""
    if game_finish==len(brick_box):
        game_over_text()
        time.sleep(5)
        sys.exit()
        
	
