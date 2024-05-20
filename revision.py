# https://wikidocs.net/2843

# 문제 2-1 다음(Daum)의 주가가 89,000원이고 네이버(Naver)의 주가가 751,000원이라고 가정하고,
# 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때 그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하세요.
def q2_1():
    daumStock = 89000
    naverStock = 751000

    return (daumStock * 100) + (naverStock * 20)

# 문제 2-1에서 구한 주식 총액에서 다음과 네이버의 주가가 각각 5%, 10% 하락한 경우에 손실액을 구하는 프로그램을 작성하세요.
def q2_2(total):
    print("5% 손실시: {}".format(total * 0.95))
    print("10% 손실시: {}".format(total * 0.9))

# 우리나라는 섭씨 온도를 사용하는 반면 미국과 유럽은 화씨 온도를 주로 사용합니다.
# 화씨 온도(F)를 섭씨 온도(C)로 변환할 때는 다음과 같은 공식을 사용합니다.
# 이 공식을 사용해 화씨 온도가 50일 때의 섭씨 온도를 계산해 보세요.
# C = (F-32)/1.8
def q2_3(temp):
    return (temp-32)/1.8

# 화면에 "pizza"를 10번 출력하는 프로그램을 작성하세요.
def q2_4():
    for i in range(0, 10):
        print('{}번째 pizza'.format(i + 1))

# 월요일에 네이버의 주가가 100만 원으로 시작해 3일 연속으로 하한가(-30%)를 기록했을 때 수요일의 종가를 계산해 보세요.
def q2_5():
    price = 1000000
    for i in range(0, 3):
        price = price * 0.7
    return price
# 다음 형식과 같이 이름, 생년월일, 주민등록번호를 출력하는 프로그램을 작성해 보세요.
# 이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210
def q2_6():
    print("이름: {} 생년월일: {} 주민등록번호: {}".format("파이썬", "2014년 12월 12일", "20141212-1623210"))

# s라는 변수에 'Daum KaKao'라는 문자열이 바인딩돼 있다고 했을 때 문자열의 슬라이싱 기능과 연결하기를 이용해 s의 값을 'KaKao Daum'으로 변경해 보세요.
def q2_7():
    s = "Daum KaKao"
    return s[5:] + " " + s[:4]

# a라는 변수에 'hello world'라는 문자열이 바인딩돼 있다고 했을 때 a의 값을 'hi world'로 변경해 보세요
def q2_8():
    a = "hello world"
    a=a.replace("hello", "hi")
    return a

# x라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때 x의 값을 'bcdefa'로 변경해 보세요.
def q2_9():
    x = "abcdef"
    return x[1:] + x[0]

if __name__ == '__main__':
    total = q2_1()
    print("총액: {}".format(total))
    q2_2(total)
    print("변환후: {}".format(q2_3(100)))
    print(q2_5())
    q2_6()
    print(q2_7())
    print(q2_8())
    print(q2_9())

