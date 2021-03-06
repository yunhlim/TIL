# [Python] 메소드(method) vs 함수(function)

흔히 메서드라 불리는 것과 함수라 불리는 건 다르다.

함수는 `def 함수명():`로 정의해 ()안에 객체를 담아 사용하는 것이라면

메소드는 **클래스(Class)**라는 개념을 알아야 한다. `인스턴스명.메서드명()`로 사용하며 특정 인스턴스가 가지고 있는 클래스의 메소드를 호출해 사용한다는 차이점이 있다.

따라서 메소드는 **클래스에 정의된 함수**이다. 함수가 메소드를 포함하는 범위라는 걸 알 수 있다.

여기서 우리가 알 수 있는 점은 함수는 오로지 값을 가져와 사용하고 반환한다. 따라서 함수를 사용하면 파라미터의 값은 절대로 변하지 않는다. **함수는 객체로부터 독립적이다.**

하지만 메서드는 인스턴스변수를 바꿀 수 있다는 차이점이 있다. 따라서 **메소드는 객체에 종속적이다.**