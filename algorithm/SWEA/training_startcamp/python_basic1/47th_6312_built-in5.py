def mul(*nums):
  mul_result = 1
  if tuple(map(int,nums)) != nums:
      print("에러발생")
      return 0
  for num in nums:
      mul_result *= num
  print(mul_result)

mul(1,2,'4',3)
