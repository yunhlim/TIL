# [HTML/CSS] CSS position(위치)

## static

모든 태그의 기본 값이다.(기본 위치)

아래 3가지는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능하다.

## relative

기본 위치 대비 offset(normal flow 유지) 

실제 영역을 먹고 있다. static과 차지하는 공간이 같다.

여러개를 조정할 땐 어렵다.

## absolute

절대 위치(normal flow에서 벗어나 이동) 

static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동한다.

## fixed 

normal flow에서 벗어나 Viewport 기준으로 위치한다.

스크롤 시에도 항상 같은 곳에 위치한다.

---

CSS의 위치를 위처럼 조정하기 어려워 쉽게 조정하기 위하여 Float, Flexbox, Grid 등이 등장하였다.