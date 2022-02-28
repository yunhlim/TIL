# [HTML/CSS] 박스 모델(Box model)

## 📌 Normal Flow

HTML의 흐름. 왼쪽 위부터 채우며 inline은 왼쪽에서 오른쪽으로 채우고 Block은 위에서 아래로 채운다.

## 📌 Box model

모든 HTML 요소는 box(네모) 형태로 되어있음

### display 속성

- 요소를 어떻게 표시할지를 선택

>display: block => 블록으로 바꿔준다.
>
>display: inline => 상하 여백은 line-height
>
>display: none => 공간이 사라지고 텍스트만 표시

### visibility 속성

- 요소를 보이게 할지 숨길지를 선택

>visibility: visible => default 값으로 요소가 그대로 보인다.
>
>visibility: hidden => 공간을 차지하긴 하는데 투명하게 보이지 않음.

### 인라인은 왜 너비 높이 마진 탑 바텀을 못 주는것일까??

>너비랑 높이를 지정하면 인라인의 의미가 없기 때문이다.
>
>마진 탑 바텀을 가지면 블록이랑 같아진다.
>

### 하나의 박스는 네 부분(영역)으로 이루어짐

![image-20220213215514099](css_box_model.assets/image-20220213215514099.png)

>content - 글이나 이미지 등 요소의 실제 내용
>
>padding - 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지는 padding까지 적용
>
>border - 테두리 선을 나타내는 영역
>
>margin - 테두리 바깥의 외부 여백, 배경색을 지정할 수 없다.

#### margin의 속성

- margin-top

- margin-right

- margin-bottom

- margin-left

**시계방향으로 생각한다 !!**

>margin: 10px; 위 오른쪽 아래 왼쪽 전부 다
>
>margin: 10px 20px; 위 10px 오른쪽 20px 바라보고 있는 쪽과 같게 채운다.
>
>margin: 10px 20px 30px; 위 오른쪽 아래 채우고 왼쪽은 오른쪽과 같게 채운다.
>
>margin: 10px 20px 30px 40px; 위 오른쪽 아래 왼쪽 순서대로
>
>margin: 10px auto; 위아래 10px씩 여백, 수평 가운데 정렬 
>
>margin-right: auto; margin-left: auto; left랑 right 같이 사용해서 auto 시켜도 수평 가운데 정렬
>
>margin-right: auto; 오른쪽으로 마진을 꽉 채운다! (왼쪽 정렬)
>
>margin-left: auto; 왼쪽으로 마진을 꽉 채운다! (오른쪽 정렬)

#### text align

- margin의 정렬과 차이는 블록을 정렬하느냐, 인라인 요소만 정렬하느냐의 차이이다.

>text-align: center; 인라인 요소(상속되는 요소)만 가운데로 보낸다.(블록은 안 된다.)
>
>text-align: left; 인라인 요소만 왼쪽으로 보낸다. (왼쪽 정렬)
>
>text-align: right; 인라인 요소만 오른쪽으로 보낸다. (오른쪽 정렬)

#### border 속성

- border-width => 테두리 두께

- border-style => 점선(dashed, solid)이나 그런 선 style

- border-color => 테두리 색

- border: 2px solid black; => 위 3가지를 한꺼번에 표현

#### box-sizing

box-sizing : border-box => default는 content-box로 box의 width를 **border box**로 맞출지 **content box**로 맞출지 선택할 수 있다.

