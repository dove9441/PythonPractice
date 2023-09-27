a=int(input())
b=int(input())
print(a*b)
print("곱셈 결과는{0} 입니다.".format(a*b))
# 배운 것: input()함수는 모든 입력을 string으로 받아들임. print에서 바뀌는 부분은 중괄호로 처리 가능하고, 뒤에 .format 붙임.
# 또는 print(int(a)*int(b))