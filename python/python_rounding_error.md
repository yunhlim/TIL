# [Python] 실수 계산 주의! rounding error



실수 연산하면 실제 값과 아주 미세한 오차가 발생한다.

그 이유는 컴퓨터는 2진수로 값을 표현하니 floating point rounding error가 발생한다.

실수 체계의 표현 때문에 미소 오차가 발생하는 것이다.

---

실수 연산과정에서 나오는 rounding error를 없애는 방법은 대표적으로 2가지가 있다.

1. `abs(a-b) <= sys.float_info.epsilon` 방법 사용

2. `math.isclose()`함수 사용 (python 3.5 이상에서만)

   ```python
   import math
   
   math.isclose(a,b)
   ```

