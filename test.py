#import는 라이브러리를 불러오는 것 / as는 이 라이브러리 경로를 어떻게 부르면 되는지
import turtle as t # import => turtle 라이브러리를 불러와라. / as => 이 turtle 라이브러리를 t 라고 불러라.

# # import math as
t.shape('turtle')
t.speed(1)

t.color('#234574')
t.pensize(4)

# 이 패턴으로 거북이를 이동시키는 것이 과제
# 모양은 직각을 이루면서 도는 모양이 되어야 한다.
# 거북이는 처음에 오른쪽으로 앞으로 가는 걸로 시작한다.
# i0 => 100
# i1 => 100
# i2 => 120
# i3 => 120
# i4 => 140
# i5 => 140
# i6 => 160
# i7 => 160
# i8 => 180
# i9 => 180
# !!!제일 중요한 것은 패턴을 발견해서 이 것을 코딩으로 표현하는 것이다.!!!
# 패턴을 해석하자면

# for i in range(2):
#     t.forward(100)
#     t.left(90)
    
# for i in range(2):
#     t.forward(120)
#     t.left(90)

# for i in range(2):
#     t.forward(140)
#     t.left(90)

# for i in range(2):
#     t.forward(160)
#     t.left(90)

# for i in range(2):
#     t.forward(180)
#     t.left(90)

# for i in range(2):
#     t.forward(200)
#     t.left(90)

# do=100
# for i in range(1):
#     t.forward(do)
#     print(do)
#     for i in range(30):
#         t.left(90)
#         t.forward(do)
#         do+=20
#         print(do)
# for i in range(30):
#     t.forward(do)


# 최상위 i와 종속된 i는 모습만 같고 다른 개념이다.

# 형식차이? 3,4줄

# x = 100
# for i in range(10):
#     for i in range(2):
#         t.forward(x)
#         t.left(90)
#     x += 20


# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


# x=100
# for i in range(1,11):
#     t.forward(x)
#     t.left(90)  
#     if i % 2 == 0: 
#         x += 20

# !!!2의 배수일 경우 2로 나눴을 때 나머지가 0이 나와야 2의 배수이기 때문에 1 % 2 == 0의 식이 도출된 것이다.


# x=100
# for i in range(10):
#     n = i/2
#     if type(n)== int:
#         x+=20
#     t.forward(x)
#     t.left(90)



# i는 0에서 시작해서 0 => 0.5 => 1 => 1.5 => 2.. 가 된다.
# 내림을 사용한다 치면 0.5는 0이고 1.5는 1이다.
# for i in range(10):
#     t.forward(i//2*20+100)
#     t.left(90)
    
    
    

for k in range(15):
    t.circle(200/1.6**k,90)
# 황금비율 거북이
