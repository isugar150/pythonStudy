#  https://wikidocs.net/2841

if __name__ == '__main__':
    monday_end_price = 10000 - (10000 * 0.3)
    tuesday_end_price = monday_end_price - (monday_end_price * 0.3)
    print(tuesday_end_price)
    print(id(tuesday_end_price))  # 메모리 주소

    mystring = 'hello world'
    print(len(mystring))
    print(mystring[:5])
    print(mystring[6:])
    print(mystring[6:-1])

    my_jusik = "naver daum"
    print(my_jusik.split(' '))

    daum = "Daum"
    kakao = "KAKAO"
    print(daum + ' ' + kakao)

    type(70000)


