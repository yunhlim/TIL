# [HTML/CSS] HTML ํ(Table)

## ๐ table ํ๊ทธ ๊ธฐ๋ณธ ๊ตฌ์ฑ

`<thead>`, `<tbody>`, `<tfoot>` ์์๋ก ๊ฐ ๊ตฌ๊ฐ ๋ช์

`<tr>`๋ก ๊ฐ๋ก ์ค์ ๊ตฌ์ฑํ๊ณ , ๋ด๋ถ์๋ `<th>` or `<td>`๋ก ์์ ๊ตฌ์ฑํ๋ค.

>`<thead>` : ํ์ header
>
>- tr > th
>
>`<tbody>` : ํ์ body
>
>- tr > td
>
>`<tfoot>` : ํ์ footer
>
>- tr > td
>
>`<caption>` : ํ์ ์ ๋ชฉ

### ์์ฑ

- colespan์ ์ธ๋ก ์ ๋ณํฉ

- rowspan์ ๊ฐ๋ก ์ ๋ณํฉ

### ๐ Table ์ฝ๋

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

### ๐ ์ ์ฝ๋์ ๊ฒฐ๊ณผ 

![image-20220228211208396](html_table.assets/image-20220228211208396.png)

ํ์๋ `<tr>`์ด๋ค. `<tr>`๊ณผ `<td>`๋ง ์๊ฑฐ๋, `<tr>`๊ณผ `<th>`๋ง ์์ด๋ ํ๋ฅผ ๋ง๋ค ์ ์๋ค.

rowspan์ ์๋์ชฝ์ผ๋ก ์์ญ์ ํ์ฅ์์ผ์ค๋ค. rowspan์ผ๋ก ํ์ฅ์ํจ ๋ค์ ํ์์๋ `<td>`๋ฅผ rowspan์ ๋ง์ถฐ ์ค์ฌ ์ ์ด์ค์ผ ํ๋ค. ์์ฒ๋ผ ํ๋ ๋ ์ ์ผ๋ฉด ํ ์์ผ๋ก ํ๋ ๋ ์ถ๊ฐ๋๋ค.

