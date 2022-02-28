# [HTML/CSS] HTML 표(Table)

## 📌 table 태그 기본 구성

`<thead>`, `<tbody>`, `<tfoot>` 요소로 각 구간 명시

`<tr>`로 가로 줄을 구성하고, 내부에는 `<th>` or `<td>`로 셀을 구성한다.

>`<thead>` : 표의 header
>
>- tr > th
>
>`<tbody>` : 표의 body
>
>- tr > td
>
>`<tfoot>` : 표의 footer
>
>- tr > td
>
>`<caption>` : 표의 제목

### 속성

- colespan은 세로 셀 병합

- rowspan은 가로 셀 병합

### 📒 Table 코드

```html
    <table>
      <!-- thead -->
      <thead>
        <!-- tr th -->
        <tr>
          <th>1</th>
          <th>2</th>
          <th>3</th>
        </tr>
      </thead>
      <!-- tbody -->
      <tbody>
        <!-- tr td -->
        <tr>
          <td>4</td>
          <td rowspan="2">rowspan</td>
          <td>5</td>
        </tr>
        <tr>
          <td>6</td>
          <td>7</td>
          <td>8</td>
        </tr>
      </tbody>
      <!-- tfoot -->
      <tfoot>
        <!-- tr td -->
        <tr>
          <td>9</td>
          <td colspan="2">colspan</td>
        </tr>
      </tfoot>
      <caption>
        caption
      </caption>
    </table>
```

### 🔍 위 코드의 결과 

![image-20220228211208396](html_table.assets/image-20220228211208396.png)

필수는 `<tr>`이다. `<tr>`과 `<td>`만 있거나, `<tr>`과 `<th>`만 있어도 표를 만들 수 있다.

rowspan은 아래쪽으로 영역을 확장시켜준다. rowspan으로 확장시킨 다음 행에서는 `<td>`를 rowspan에 맞춰 줄여 적어줘야 한다. 위처럼 하나 더 적으면 표 옆으로 하나 더 추가된다.

