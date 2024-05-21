# https://wikidocs.net/3037
from operator import itemgetter

# 2015년 9월 초의 네이버 종가는 표 3.2와 같습니다.
# 09/07의 종가를 리스트의 첫 번째 항목으로 입력해서 naver_closing_price라는 이름의 리스트를 만들어보세요.
#표 3.2 네이버 종가

# 날짜    요일  종가
# 09/11  금	 488,500
# 09/10  목	 500,500
# 09/09  수	 501,000
# 09/08  화	 461,500
# 09/07  월	 474,500
def q3_1():
    return [
        {"date": "09/11", "week": "금", "price": 488500},
        {"date": "09/10", "week": "목", "price": 500500},
        {"date": "09/09", "week": "수", "price": 501000},
        {"date": "09/08", "week": "화", "price": 461500},
        {"date": "09/07", "week": "월", "price": 474500},
    ]

# 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에 종가를 기준으로 가장 높았던 가격을 출력하세요.
# (힌트: 리스트에서 최댓값을 찾는 함수는 max()이고, 화면에 출력하는 함수는 print()입니다.)
def q3_2(naverClosingPrice):
    myList = list(map(lambda x: x['price'], naverClosingPrice))
    print('q3_2 result: ', max(myList))

# 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에 종가를 기준으로 가장 낮았던 가격을 출력하세요.
# (힌트: 리스트에서 최솟값을 찾는 함수는 min()이고, 화면에 출력하는 함수는 print()입니다.)
def q3_3(naverClosingPrice):
    myList = list(map(lambda x: x['price'], naverClosingPrice))
    print('q3_3 result: ', min(myList))

# 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에서 가장 종가가
# 높았던 요일과 가장 종가가 낮았던 요일의 가격 차를 화면에 출력하세요..
def q3_4(naverClosingPrice):
    minObj = min(naverClosingPrice, key=itemgetter('price'))
    maxObj = max(naverClosingPrice, key=itemgetter('price'))

    print('q3_4 result 가장 높았던 요일: {}, 가장 낮차던 요일: {}, 가격차: {}'.format(maxObj['week'], minObj['week'], maxObj['price'] - minObj['price']))

# 문제 3-1에서 만든 naver_closing_price를 이용해 수요일의 종가를 화면에 출력하세요.
def q3_5(naverClosingPrice):
    print('q3_5 result: ', list(filter(lambda obj: obj['week'] == '수', naverClosingPrice))[0]['price'])

# 문제 3-1의 표 3.2를 이용해 날짜를 딕셔너리의 키 값으로,
# 종가를 딕셔너리의 값으로 사용해 naver_closing_price2라는 딕셔너리를 만드세요.
def q3_6(naverClosingPrice):
    list = []
    for obj in naverClosingPrice:
        obj2 = {obj['date'] : obj['price']}
        list.append(obj2)
    return list

# 문제 3-6에서 만든 naver_closing_price2 딕셔너리를 이용해 09/09일의 종가를 출력하세요.
def q3_7(naverClosingPrice2):
    for obj in naverClosingPrice2:
        for key, value in obj.items():
            if key == '09/09':
                print('q3_7 result: ', value)


if __name__ == '__main__':
    naverClosingPrice = q3_1()
    print('q3_1 result', naverClosingPrice)
    q3_2(naverClosingPrice)
    q3_3(naverClosingPrice)
    q3_4(naverClosingPrice)
    q3_5(naverClosingPrice)
    naverClosingPrice2 = q3_6(naverClosingPrice)
    print('q3_6 result', naverClosingPrice2)
    q3_7(naverClosingPrice2)
