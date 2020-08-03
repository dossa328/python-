# 터틀 그래픽을 이용해서 온갖 도형을 그려봅시다
import turtle
import random
# 반복
for i in range(10):
    # 안의 반복
    for j in range(5):
        # 랜덤함수를 통해 0~3 사이의 랜덤 값을 하나 정한다. -> 펜 색을 랜덤으로 하기위함
        col = random.randint(0, 3)
        # if 이하 0~3에 대해 색을 mapping함
        if 0 == col:
            turtle.pencolor("yellow")
        elif 1 == col:
            turtle.pencolor("blue")
        elif 2 == col:
            turtle.pencolor("red")
        elif 3 == col:
            turtle.pencolor("green")
        # 다시 랜덤함수를 통해 0~4사이의 랜덤값을 하나 정한다. -> 색칠할(fill) 색을 정한다
        col = random.randint(0, 4)
        # if 이하 0~4에 대해 색을 mapping함
        if 0 == col:
            turtle.color("red")
        elif 1 == col:
            turtle.color("blue")
        elif 2 == col:
            turtle.color("green")
        elif 3 == col:
            turtle.color("purple")
        elif 4 == col:
            turtle.color("yellow")
        # 또 다시 랜덤 함수를 통해 0~4사이의 랜덤값을 하나 정한다. -> 도형을 어떻게 그릴지, 채워넣을지 말지 정한다.
        # 물론 여기서 조금씩 그린다
        sel = random.randint(0, 4)
        if 0 == sel:
            turtle.forward(random.randint(50, 100))
        elif 1 == sel:
            turtle.right(random.randint(90, 360))
        elif 2 == sel:
            turtle.begin_fill()
            turtle.circle(random.randint(-100, -20))
            turtle.end_fill()
        elif 3 == sel:
            turtle.forward(random.randint(30,50))
        elif 4 == sel:
            turtle.circle(random.randint(20, 100))
    # 다 정해졌다면 a,b의 랜덤 시작 좌표를 받는다. 범위는 -300 ~ 300
    a = float(random.randint(-300, 300))
    b = float(random.randint(-300, 300))
    # 아래 3개의 함수는 a, b 좌표점으로 돌아가는 기능을 함. 그냥 () 라고 쓰면 맨 처음(a,b 설정하기 전)으로 돌아간다.
    # turtle.goto(a, b)
    turtle.setpos(a, b)
    # turtle.setposition(a,b)
