# [HTML/CSS] CSS 선택자 우선순위

![image-20220213165302123](css_priority.assets/image-20220213165302123.png)

참조 : https://specifishity.com/ 

우선순위 : important > 인라인 > id > class, 속성, 수도(추상)클래스(:) > element(tag), 수도element(::) > *

---

!important: 가장 우선순위가 높다. 우선순위를 강제로 높이므로 되도록 쓰지 않도록 하자.(사용시 주의)

그 다음으로는 inline 참조가 있는 것이 높다.

id, class, tag는 **올림픽 메달** 순위 산정방식을 생각해보면 쉽다.

id 개수가 많은 순서 > class 개수가 많은 순서 > tag 개수가 많은 순서대로 적용된다.

금은동의 개수가 같다면 가장 아래에 적힌 선택자가 지정된다.

