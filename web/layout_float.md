# [HTML/CSS] Float 레이아웃

박스를 제외한 나머지 인라인요소들이 박스 주변을 wrapping하도록 설정

기본 레이아웃으로는 감싸는 배치가 어려웠다.(사진을 양쪽 끝에 배치하는 경우)

이런 걸 해결하기 위해 **Float**(둥둥 떠있다)이 등장했다.

## Float 속성

none: 기본값

left: 요소를 왼쪽으로 띄움

- float: left(right);를 주는 순간 공간을 왼쪽만 차지하게된다. 둥둥떠있는것처럼

right: 요소를 오른쪽으로 띄움

**float는 모든 요소에 시킬 수 있다.**

## Clearing Float

자식요소가 Float이면 부모요소의 높이가 0으로 처리가 된다. 아무것도 안 들어있는걸로 본다.

해결하기위해 부모에게 .clearfix를 해준다.

```css
.clearfix::after {
	content: "";
	display: block;
	clear: both;
}
```

clearing하여 부모에 clearfix의 높이를 지정해준다.

매번 clearing을 필수적으로 하여 부모요소에게 clear 속성을 부여해주어야한다.

---

Flexbox, Grid의 등장으로 사용도가 낮아졌다.

그렇지만 아직까지도 활용하고 있는 방법이다.