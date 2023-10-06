# 유아로부터 구구단을 출력할 최대 단수를 입력받음
def result(dan):
    result = dan
    for dan in range(1, dan + 1):
        print(f"--------{dan} 단--------")
        for i in range(1, dan+1):
            result = dan * i
            print(dan, "x", i, "=", dan * i)
        print()
dan = int(input("몇 단까지 출력할까요?: "))

result(dan)