std = [88, 30, 61, 55, 95]
success = ""
cnt = 0
for score in std:
    cnt += 1
    if score>=60 :
        success = "합격"
    else :
        success = "불합격"
    print(f'{cnt}번 학생은 {score}점으로 {success}입니다.')