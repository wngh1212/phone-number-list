# 기능구현 해야하는 부분
# 1. 전화번호/이름을 추가 (구현)
# 2. 찾는기능 (구현)
# 3. 삭제기능 (구현)
# 4. 파일에저장 (구현)
# 5. 수정하는기능(구현)
# 6. 파일에서 데이터 가져오기 (구현...인가?)
# 7. 정보에대한중복제거(구현x)
import csv
humann = {}
while True:
    print('전화번호부')
    menu = input('회원정보 추가(add), 검색(search), 수정(correction), 삭제(del), 목록(list), 종료(exit): ')
    if menu=='add':
        name = input('이름 입력: ')
        phone = input('전화번호 입력: ')
        humann[name] = phone
        print('----------')
        print('-----입력 완료-----')
        print(f'{name}:', phone)
        print('----------')
        
    elif menu=='search':
        name = input('검색할 이름 입력: ')
        phone = humann.get(name, '존재하지 않습니다.')
        print('----------')
        print(f'{name}:', phone)
        print('----------')

    elif menu=='correction':
        name = input('수정할 이름 입력: ')
        if name not in humann.keys(): # humann.keys(): key만 추출하기
            print('----------')
            print('존재하지않은 정보입니다')
            print('----------')
            continue # loop 계속 진행
        else:
            phone = input('새로운 전화번호 입력: ')
            humann[name] = phone
            print('----------')
            print("-----수정 완료-----")
            print(f'{name}:', phone) #formating
            print('----------')

    elif menu=='del':
        name = input('삭제할 이름 입력: ')
        if name not in humann.keys():
            print('----------')
            print('존재하지 않습니다.')
            print('----------')
            continue
        else:
            ask = input("정말로 삭제할까요?(y) or (n): ")
            if ask == 'y':
                del humann[name]
                print('----------')
                print(f"-----{name} 삭제 완료-----")
                print('----------')
            else:
                print('----------')
                print('삭제하지 않았습니다.')
                print('----------')

    elif menu=='list':
        print('----------')
        for k, v in humann.items(): # humann.items(): key, value 추출하기
            print(f'{k}: {v}')
        # f = open("save.csv", "r")
        # reder = csv.reader(f)

        # for human in reder:
        #     print(human)
        print('----------')
        
    elif menu=='exit':
        print('----------')
        print('전화번호부를 종료합니다.')
        print('정보들을 저장합니다')
        print('----------')
        saveflie = open('./save.csv','w') #sava란csv파일을 write한다
        data = humann.items()
        writer = csv.writer(saveflie)
        writer.writerow(data)
        saveflie.close()
        break # loop 끝내기
