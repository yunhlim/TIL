# [Baekjoon] 2615. μ€λͺ©[S2]

## π λ¬Έμ 

https://www.acmicpc.net/problem/2615

---

μ€λͺ©μ΄ κ°λ₯ν κ°μ§μλ₯Ό 4κ°μ§λ‘ μκ°νλ€. λ¬Έμ μμ μ€λͺ©μ΄ λ§λ€μ΄μ‘μ λ μ μΌ μΌμͺ½ λ°©ν₯μ μ’νλ₯Ό μνκ³  μΈλ‘λ‘ μΌμ§μ μ΄λ©΄ μμͺ½ λ°©ν₯μ΄κΈΈ μνλ―λ‘ μ€λ₯Έμͺ½ λ°©ν₯, μλμͺ½ λ°©ν₯, μΌμͺ½ μμͺ½μμ μ€λ₯Έμͺ½ μλμͺ½ λ°©ν₯, μΌμͺ½ μλμͺ½μμ μ€λ₯Έμͺ½ μμͺ½ λ°©ν₯μΌλ‘ 4κ°μ§λ‘ λλμ΄ ν΄κ²°ν΄λ³΄μλ€.

![image-20220125011336074](S2_2615.assets/image-20220125011336074.png)

λ¬Έμ μμ μ£Όμ΄μ§ λ°λνμ λ°©ν₯μ λ€μκ³Ό κ°λ€.

![image-20220125010410496](S2_2615.assets/image-20220125010410496.png)

μΌμͺ½, μμͺ½ λμ (0,0)μΌλ‘ μ‘κ³  λͺ¨λ  μ’νλ₯Ό κ²μν΄ μμμ μΌλ‘ κ°λ₯νμ§ νμΈνλ€. 5κ°λ₯Ό λ§λ€ μ μλ μ’νλ μ μΈνλ€. μλ₯Ό λ€μ΄ (1,16)μ΄ μμμ μΌλ‘ 5κ°λ₯Ό λ§λ€ μ μμΌλ μ μΈνλ€.

μμμ μλ λ°λμ λ°λλμ΄ μμ΄μΌ νλ―λ‘, λ°λλμ΄ μλ 0μ΄ μμΌλ©΄ μ§λκ°λ€. λν μ€λ₯Έμͺ½μΌλ‘ μ°Ύλλ€κ³  κ°μ νλ©΄ μμμ μ λ°λμͺ½μΌλ‘ λκ°μ λμ΄ μμ΄λ κ·Έ λ μμμ μ΄ μλλ μ§λκ°λ€. μ΄ λ μμμ μ λ°λμͺ½μΌλ‘ λ°λλμ λ μ μμ΄ μ΄λ μ‘°κ±΄λ λ°λ‘ μ§μ ν΄μ£Όμ΄μΌ νλ€.

5κ°μ λμ΄ λκ°μΌλ©΄ 6κ° μ΄μμ΄ μλμ¬μ§λμ§λ νμΈνλ€. 5κ°λ§ μ΄λ£¨μ΄μ‘μ λλ‘ λ΅μ μ°ΎμμΌ νλ λ°λν λ°κΉ₯μΌλ‘ λκ°κ² λλ κ²½μ°λ μ‘°κ±΄μμΌλ‘ μ μ΄μ€λ€.

## π μ½λ

```python
input_lst = [0 for i in range(19)]
for i in range(19):
    input_lst[i] = list(map(int, input().split()))

def omok(lst):
    win = 0 # 0μ΄λ©΄ μΉλΆx, 1μ΄λ©΄ κ²μλ μΉλ¦¬, 2μ΄λ©΄ ν°λ μΉλ¦¬
    position = 0
    for i in range(19): # μ΄μ€ for λ¬ΈμΌλ‘ μ€λͺ©μ΄ μμ±λ  μ μλ μμμ μ νλμ© μ ν
        for j in range(15): # μμμ μμ μ€λ₯Έμͺ½μΌλ‘ μ€λͺ©μ΄ μμ±λλμ§ νμΈ
            if lst[i][j] != 0:  # λ°λλμ΄ λμ¬ μμ λ
                if j == 0 or lst[i][j] != lst[i][j-1]:  
                    # λ°λλ μΌμͺ½μ κ°μ΄ μκ±°λ, μμ λλ μμ΄ λ€λ₯΄λ©΄ μμμ μΌλ‘ μ ννλ€.
                    for k in range(1,5): # 5κ°κ° λλν μλμ§ νμΈ
                        if lst[i][j] != lst[i][j+k]:
                            break
                    else:
                        if j == 14 or lst[i][j] != lst[i][j+5]: # μ€λ₯Έμͺ½μΌλ‘ λ λμ μλ¦¬κ° μκ±°λ μ€λ₯Έμͺ½μ λμΈ κ²μ΄ λ€λ₯Έ μμΈμ§ νμΈ.
                            win = lst[i][j]
                            position = (i+1,j+1)

    for i in range(15): # μ΄μ€ for λ¬ΈμΌλ‘ μ€λͺ©μ΄ μμ±λ  μ μλ μμμ μ νλμ© μ ν
        for j in range(19): # μμμ μμ μλμͺ½μΌλ‘ μ€λͺ©μ΄ μμ±λλμ§ νμΈ
            if lst[i][j] != 0:  # λ°λλμ΄ λμ¬ μμ λ
                if i == 0 or lst[i][j] != lst[i-1][j]:
                    # λ°λλ μμͺ½μ κ°μ΄ μκ±°λ, μμ λλ μμ΄ λ€λ₯΄λ©΄ μμμ μΌλ‘ μ ννλ€.
                    for k in range(1,5): # 5κ°κ° λλν μλμ§ νμΈ
                        if lst[i][j] != lst[i+k][j]:
                            break
                    else:
                        if i == 14 or lst[i][j] != lst[i+5][j]: # μλμͺ½μΌλ‘ λ λμ μλ¦¬κ° μκ±°λ μλμͺ½μ λμΈ κ²μ΄ λ€λ₯Έ μμΈμ§ νμΈ.
                            win = lst[i][j]
                            position = (i+1,j+1)

    for i in range(15): # μ΄μ€ for λ¬ΈμΌλ‘ μ€λͺ©μ΄ μμ±λ  μ μλ μμμ μ νλμ© μ ν
        for j in range(15):    # μμμ μμ μ€λ₯Έμλμͺ½μΌλ‘ μ€λͺ©μ΄ μμ±λλμ§ νμΈ
            if lst[i][j] != 0:  # λ°λλμ΄ λμ¬ μμ λ              
                if i == 0 or j == 0 or lst[i][j] != lst[i-1][j-1]: 
                    # λ°λλ μΌμͺ½μ΄λ μμͺ½μ κ°μ΄ μκ±°λ, μμ λλ μμ΄ λ€λ₯΄λ©΄ μμμ μΌλ‘ μ ννλ€.
                    for k in range(1,5): # 5κ°κ° λλν μλμ§ νμΈ
                        if lst[i][j] != lst[i+k][j+k]:
                            break
                    else:
                        if i == 14 or j == 14 or lst[i][j] != lst[i+5][j+5]: # μ€λ₯Έμͺ½, μλμͺ½μΌλ‘ λ λμ μλ¦¬κ° μκ±°λ μ€λ₯Έμλμͺ½μ λμΈ κ²μ΄ λ€λ₯Έ μμΈμ§ νμΈ.
                            win = lst[i][j]
                            position = (i+1,j+1)

    for i in range(18,3,-1): # μ΄μ€ for λ¬ΈμΌλ‘ μ€λͺ©μ΄ μμ±λ  μ μλ μμμ μ νλμ© μ ν
        for j in range(15): # μμμ μμ μ€λ₯Έμμͺ½μΌλ‘ μ€λͺ©μ΄ μμ±λλμ§ νμΈ
            if lst[i][j] != 0:  # λ°λλμ΄ λμ¬ μμ λ
                 if i == 18 or j == 0 or lst[i][j] != lst[i+1][j-1]:
                    # λ°λλ μΌμͺ½μ΄λ μλμͺ½μ κ°μ΄ μκ±°λ, μμ λλ μμ΄ λ€λ₯΄λ©΄ μμμ μΌλ‘ μ ννλ€.
                    for k in range(1,5): # 5κ°κ° λλν μλμ§ νμΈ
                        if lst[i][j] != lst[i-k][j+k]:
                            break
                    else:
                        if i == 4 or j == 14 or lst[i][j] != lst[i-5][j+5]: # μ€λ₯Έμͺ½, μμͺ½μΌλ‘ λ λμ μλ¦¬κ° μκ±°λ μ€λ₯Έμμͺ½μ λμΈ κ²μ΄ λ€λ₯Έ μμΈμ§ νμΈ.
                            win = lst[i][j]
                            position = (i+1,j+1)
    if win == 0:    # μΉλΆκ° λμ§ μμΌλ©΄ 0λ§ μΆλ ₯
        print(win)
        return
    print(win)  # μΉλΆκ° λ¬μΌλ μΉλ¦¬ν λμ μΆλ ₯ν ν μμΉλ₯Ό μΆλ ₯νλ€.
    print(*position)

omok(input_lst)
```

## π κ²°κ³Ό

![image-20220125012047253](S2_2615.assets/image-20220125012047253.png)

μ²μμ λλ¬΄ μ΄λ ΅κ² μ κ·Όν΄μ λͺ μκ°μ ν€λ§€λ€κ° λ°©λ²μ λ°κΏ ν΄κ²°νλ€..π