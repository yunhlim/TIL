T = int(input())    # 테스트 케이스 개수 T
a_b_lst = []    # a,b를 리스트에 담을 빈 배열
for i in range(T):  # [a,b]를 담은 2차원 리스트를 만든다.
    a_b_lst.append(list(map(int,input().split())))

def last_num(a, b): # 마지막 숫자를 수행해주는 프로그램
    result = 1  # 한번 곱할 때마다 바꿔줄 1의 자리 수
    for _ in range(b):    # b-1번 a를 곱해주며 % 연산자를 사용해 1의 자리만 남긴다
        result = (result * a) % 10
    return result

for i in range(T):  # [a,b] 가 T개 있으니 for문으로 순회
    print(last_num(*a_b_lst[i]))    # 입력받은 [a,b]리스트를 언팩 연산자를 활용해 입력으로 넣어 실행한다.














