jinsu_10 = int(input())
jinsu_2 = ''
while True:
    jinsu_2 = str(jinsu_10 % 2) + jinsu_2
    jinsu_10 = jinsu_10//2
    if jinsu_10 < 2:
        jinsu_2 = str(jinsu_10) + jinsu_2
        break
print(jinsu_2)