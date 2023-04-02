print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

# 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not (5>10))


#애완동물을 소개해주세요
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집" + animal + "의 이름은 연탄이에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))


# 이것은 하나의 문장
''' 이렇게 하면 여러 문작이 주석처리 됩니다'''
# ctrl + /  를 해도 주석처리가 된답니다.


station = {"사당", "신도림", "인천공항"}
print(station + "행 열차가 들어오고 있습니다.")


print(abs(-5)) #5
print(pow(4, 2)) # 4 & 2 = 4*4 = 16
print(max(5, 12)) # max = 12
print(min(5, 12)) # min = 5
print(round(3.24)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림.4
print(sqrt(16)) # 제곱근

