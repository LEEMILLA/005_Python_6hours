print("나는 %d 살입니다." % 20)
print("나는 %s 를 좋아해요." % "Python")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("빨강", "노랑"))

print("나는{} 살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "노란"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .f ormat(color="빨간", age = 20))

# 방법 4(파이썬 3.6이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")