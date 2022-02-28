# [HTML/CSS] CSS 선택자, 결합자, CSS 상속

## 선택자

### 📚 선택자 연습 서비스

링크 : https://flukeout.github.io/

### 전체 선택자

- 전체를 고를 땐 `*`를 사용한다.

```css
<style>
    * {
        color: red;
    }
</style>
```

### 요소 선택자

- 요소는 그냥 이름을 붙인다.

``` css
<style>
    h2 {
        color: red;
    }
</style>
```

### 클래스(class) 선택자

- 클래스는 앞에 `.`을 붙여 사용한다.

```css
<style>
    .box {
        color: red;
    }
</style>
```

### 아이디(id) 선택자

- id는 `#`을 붙인다.

```css
<style>
    #red {
        color: red;
    }
</style>
```

### 속성(attribute) 선택자

요소[속성이름]으로 사용한다. 속성이 있는 모든 요소를 선택한다.

```css
<style>
    a[target] {
        color: red;
    }
</style>
```

## 결합자(Combinators)

### 자손 결합자

- selectorA selectorB {}

- selectorA **하위의 모든** selectorB 요소 선택

```css
div span {
    color: red;
}
```

### 자식 결합자

- selectorA > selectorB {}

- selectorA **바로 아래**의 selectorB 요소 선택

```css
div > span {
    color: red;
}
```

### 일반 형제 결합자

- selectorA ~ selectorB {}
- selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소 모두 선택

```css
div ~ span {
    color: red;
}
```

### 인접 형제 결합자

- selectorA + selectorB {}
- selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소 선택

```css
div + span {
    color: red;
}
```

### 추가적인 선택자 정리

>`부모요소 특정요소:<>` {}
>
>자식 요소의 모든 형제요소를 다 센다.
>
>`:first-child` 자식요소 중 맨 앞 요소
>
>`:only-child` 자식요소가 하나인 것 선택
>
>`:last-child` 자식요소 중 맨 마지막 요소
>
>---
>
>`:nth-child()` 자식요소 중 맨 앞부터 세서 요소 선택
>
>`:nth-last-child()` 자식요소 중 뒤부터 세서 선택
>
>---
>
>---
>
>자식 요소 중 특정 요소만 센다.
>
>`:first-of-type` 특정자식요소 중 맨 앞 요소
>
>`:only-of-type` 특정자식요소 중 자식요소가 하나인 것 선택
>
>`:last-of-type` 특정자식요소 중 맨 마지막 요소
>
>---
>
>`:nth-of-type()` 특정자식요소 중 앞부터 세서 요소 선택
>
>- `(odd), (even)`을 붙여 짝수나 홀수개를 고를 수 있다.
>
>`:nth-last-of-type()` 특정자신요소 중 뒤부터 세서 선택
>
>`:nth-of-type(An+B)` B부터 시작해서 A만큼 건너서 고른다.
>
>---
>
>`:empty` 안에 아무것도 없는 요소를 선택
>
>`:not(X)`요소들 중 X가 있는 걸 제외한 나머지를 선택

## CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
- 상속되는 것과 상속되지 않는 것이 있으니 확인하고 사용한다.

> Text 관련 요소 등은 상속
>
> Box model이나 position 관련 요소는 상속 X