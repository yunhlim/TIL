# [Vue] Vue ๋ฌธ๋ฒ [EP 02]

## ๐ Vue.js CDN

### Vue.js CDN ์ฐธ๊ณ  ๋ฌธ์

- [์์ํ๊ธฐ](https://kr.vuejs.org/v2/guide/index.html) ์์ต์๋ฅผ ๋ฐ๋ผํ๋ฉฐ ์ฐ์ต!



### Vue instance

- ๋ชจ๋  Vue ์ฑ์ Vue ํจ์๋ก ์ ์ธ์คํด์ค๋ฅผ ๋ง๋๋ ๊ฒ๋ถํฐ ์์ํ๋ค.
- Vue Instance == Vue Component

```vue
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    {{ message }}
    {{ greeting() }}
  </div>

  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: '์๋ํ์ธ์'
      },
      methods: {
        greeting: function () {
          const newMessage = this.message + '!!!!'
          console.log(newMessage)
          return newMessage
        }
      }
    })
  </script>
</body>
</html>

```



## ๐ ์ ์ธ์  ๋ ๋๋ง

### el

- ์ด๋ค ๋ ์์์ ๋ถ์ฐฉํ  ๊ฒ์ธ์ง
- new๋ฅผ ์ด์ฉํ ์ธ์คํด์ค ์์ฑ ๋๋ง ์ฌ์ฉ

### data

- Vue ์ธ์คํด์ค์ ๋ฐ์ดํฐ ๊ฐ์ฒด
- Vue ์ธ์คํด์ค์ ์ํ ๋ฐ์ดํฐ ์ ์
- Vue ๊ฐ์ฒด ๋ด ๋ค๋ฅธ ํจ์์์ this ํค์๋๋ฅผ ํตํด ์ ๊ทผ ๊ฐ๋ฅ
- Vue template์์ interpolation์ผ๋ก ์ ๊ทผ ๊ฐ๋ฅ => ๋ ๋ค innerText

### methods

- Vue ์ธ์คํด์ค์ ์ถ๊ฐํ  ๋ฉ์๋
- ํ์ดํ ํจ์๋ฅผ ๋ฉ์๋๋ฅผ ์ ์ํ๋๋ฐ ์ฌ์ฉํ๋ฉด ์๋๋ค.
  - Vue ํจ์ ๊ฐ์ฒด ๋ด์์ vue ์ธ์คํด์ค๋ฅผ ๊ฐ๋ฆฌํจ๋ค.
  - ํ์ดํ ํจ์์์ this๋ window๋ฅผ ๊ฐ๋ฆฌํจ๋ค.

```javascript
var app = new Vue({
  el: '#app',
  data: {
    message: '์๋ํ์ธ์ Vue!'
  },
  methods: {
    greeting: function () {
      console.log('hello')
    }
  }
})
```

### computed

- (๋ฐ์ดํฐ์ ์์กดํ๋) ๊ณ์ฐ๋ ๊ฐ

- ๋ด๋ถ์ ์ผ๋ก ์์์ ์คํํด๋์ **๊ฐ**์ด์ง ํจ์๋ก ์ฐ์ฌ์ง์ง ์๋๋ค.
- ์ข์๋ ๋ฐ์ดํฐ๊ฐ ๋ณ๊ฒฝ๋  ๋๋ง ํจ์๋ฅผ ์คํ

- ๋ฆฌํด ๊ฐ์ด ๋ฌด์กฐ๊ฑด ์์ด์ผ ํ๋ค.

- getter - data๋ฅผ ํตํด ๊ฐ์ ์ป๋๋ค.

  > method๋ ๋ฐ์ดํฐ๋ฅผ ๋ฐ๊พธ๋ ๋ก์ง(setter)

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <input v-model="r" type="text">
    <p>{{ r }}</p>
    <p>{{ area }}</p>
    <p>{{ perim }}</p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        r: 2,
      },
      computed: {
        area: function () {
          return this.r ** 2 * 3.14
        },
        perim: function () {
          return this.r * 2 * 3.14
        }
      }
     
    })
  </script>
</body>
</html>

```

> **computed & methods**
>
> computed๋ ์ข์๋ ๋์์ด ๋ณ๊ฒฝ๋์ง ์๋ ํ ์ฌ๋ฌ ๋ฒ ํธ์ถํด๋ ๊ณ์ฐ์ ๋ค์ ํ์ง ์๊ณ  ๊ณ์ฐ๋์ด ์๋ ๊ฒฐ๊ณผ๋ฅผ ๋ฐํ
>
> methods๋ฅผ ํธ์ถํ๋ฉด ๋ ๋๋ง์ ๋ค์ ํ  ๋๋ง๋ค ํญ์ ํจ์๋ฅผ ์คํ
>
> ```vue
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <meta http-equiv="X-UA-Compatible" content="IE=edge">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <title>Document</title>
> </head>
> <body>
>   <div id="app">
>     <div>
>       <input type="text" v-model="message">
>     </div>
>     {{ other }}
>     <p>Original: <strong>{{ message }}</strong></p>
>     <p>Reverse by Method: <strong>{{ reverseMessage() }}</strong></p>
>     <p>Reverse by Computed: <strong>{{ reversedMessage }}</strong></p>
>     
>   </div>
>   
>   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
>   <script>
>     const app = new Vue({
>       el: '#app',
>       data: {
>         sessionid: 'asdf',
>         message: 'Original',
>         other: 'asdf'
>       },
>       // data๋ฅผ ๋ฐ๊พธ๋ ๋ก์ง ์์ฃผ! (setter ํจ์๋ค)
>       methods: {
>         reverseMessage() {
>           console.log('method!!')
>           return this.message.split('').reverse().join('')
>         },
>       },
>       // data๋ฅผ ํตํ ๊ฐ์ ์ป์! (getter ํจ์๋ค)
>       computed: {
>         // (data์ ์์กดํ๋)๊ณ์ฐ๋ ๊ฐ
>         reversedMessage() {
>           console.log('computed!!')
>           return this.message.split('').reverse().join('')
>         },
>         isLoggedIn() {
>           return this.sessionid ? true : false
>         }
>       }
>     })
>   </script>
> </body>
> </html>
> ```

### watch

- computed์ ๋๊ฐ์ด ์ฃผ์ํ๊ณ  ์๋ค๊ฐ ์ฝ๋ฐฑ ํจ์๋ฅผ ์คํ(ํธ๋ฆฌ๊ฑฐ๋ง ๊ฑด๋ค.)

- ์ ์ธํ์ด ์๋ ๋ช๋ นํ ํ๋ก๊ทธ๋๋ฐ ๋ฐฉ์

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>{{ num }}</p>
    <button @click="num += 1">add 1</button>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        num: 2,
      },
      watch: {
        num: function () {
          console.log(`${this.num}์ด ๋ณ๊ฒฝ๋์์ต๋๋ค.`)
        }
      },
    })
  </script>
</body>
</html>

```

### filter

- filter๋ ์ฅ๊ณ ์ ํํฐ์ ์ ์ฌ

- ํ์คํธ ํ์ํ๋ฅผ ์ ์ฉํ๊ธฐ ์ํด ๋ง์ด ์ด๋ค.

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    {{ numbers | getOddNumbers | getUnderTen }}
    {{ getOddAndUnderTen }}
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      },
      filters: {
        getOddNumbers(array) {
          return array.filter(num => num % 2)
        },
        getUnderTen(array) {
          return array.filter(num => num < 10)
        }
      },
      // w/ computed
      computed: {
        getOddAndUnderTen() {
          return this.numbers.filter(num => num % 2 && num < 10)
        }
      }
    })
  </script>
</body>
</html>

```



## ๐ฏ Directive (๋๋ ํฐ๋ธ)

- v- ์ ๋์ฌ๊ฐ ์๋ ํน์ ์์ฑ

- ์์ฑ ๊ฐ์ ๋จ์ผ JS ํํ์์ด ๋จ (v-for ์์ธ)

- ํํ์์ ๊ฐ์ด ๋ณ๊ฒฐ๋  ๋ ๋ฐ์์ ์ผ๋ก DOM์ ์ ์ฉํ๋ ์ญํ ์ ํจ

- ์ ๋ฌ์ธ์ `:` : ์ฝ๋ก ์ ํตํด ์ ๋ฌ์ธ์๋ฅผ ๋ฐ๋๋ค.

  ```vue
  <a v-on:click="function"></a>
  ```

- ์์์ด `.` : ์ ์ผ๋ก ํ์, directive๋ฅผ ํน๋ณํ ๋ฐฉ๋ฒ์ผ๋ก ๋ฐ์ธ๋ฉ

  ```vue
  <form v-on:submit.prevent="function"></form>
  ```

### v-text

- interpolation ๋ฌธ๋ฒ์ด v-text์ด๋ค.

  ```vue
  <p v-text="message"></p>
  <!-- ๊ฐ๋ค -->
  <p>{{ message }}</p>
  ```

> v-html
>
> XSS ๊ณต๊ฒฉ์ ์ทจ์ฝํ  ์ ์์
>
> ์ฌ์ฉ์๋ก๋ถํฐ ์๋ ฅ๋ฐ์ ๋ด์ฉ์ v-html **์ ๋** ์ฌ์ฉ ๊ธ์ง

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>{{ message }}</p>
    <p v-text="message"></p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'Hello'
      }
    })
  </script>
</body>
</html>

```

### v-show

- ์กฐ๊ฑด๋ถ ๋ ๋๋ง ์ค ํ๋
- ์์๋ ํญ์ ๋ ๋๋ง ๋๊ณ  DOM์ ๋จ์์์
- ๋จ์ํ ์๋ฆฌ๋จผํธ์ display CSS ์์ฑ์ ํ ๊ธ

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p v-show="isTrue">TRUE</p>
    <p v-show="isFalse">FALSE</p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        isTrue: true,
        isFalse: false,
      }
    })
  </script>
</body>
</html>
```

### v-if

- v-if, v-else-if, v-else
- ์กฐ๊ฑด๋ถ ๋ ๋๋ง ์ค ํ๋
- ์กฐ๊ฑด์ ๋ฐ๋ผ ์์๋ฅผ ๋ ๋๋ง

> v-show ์ v-if
>
> ๋์ ๋ณด์ด๋ ์ ๋ณด์ด๋(ํ ํด๋ก) show๋ hidden์ผ๋ก ๋ง๋ค์ง๋ง,  if๋ ๋ ๋๋ง ์กฐ์ฐจ ์ํ๋ค.
>
> ์์ฃผ ๋ณ๊ฒฝ๋๋ฉด show, ๊ฐ๋ ๋ณ๊ฒฝ๋๋ฉด v-if

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
  <div id="app">
    <p v-if="seen">seen is TRUE</p>

    <p v-if="myType === 'A'">A</p>
    <p v-else-if="myType === 'B'">B</p>
    <p v-else-if="myType === 'C'">C</p>
    <p v-else>NOT A/B/C</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        seen: false,
        myType: 'A',
      }
    })
  </script>
</body>
</html>
```

### v-bind

- ์์ฑ ๋ฐ์ธ๋ฉ, ํด๋์ค ๋ฐ์ธ๋ฉ
- HTML ์์์ ์์ฑ์ Vue์ ์ํ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ผ๋ก ํ ๋น
- **์ ๋ง ์ ๋ง ๋ง์ด ์ฐ์ธ๋ค.**
- ์ฝ์ด : `:`(์ฝ๋ก )
  - v-bind:href ์ :href๊ฐ ๊ฐ๋ค

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .active {
      color: red;
    }

    .my-background-color {
      background-color: yellow;
    }
  </style>
</head>
<body>
  <div id="app">
    <!-- ์์ฑ ๋ฐ์ธ๋ฉ -->
    <img v-bind:src="imageSrc" :alt="altMsg">
    <img :src="imageSrc" alt="altMsg">
    <hr>

    <!-- ํด๋์ค ๋ฐ์ธ๋ฉ -->
    <div :class="{ active: isRed }">
      ํด๋์ค ๋ฐ์ธ๋ฉ
    </div>

    <h3 :class="[activeRed, myBackground]">
      hello vue
    </h3>
    <hr>

    <!-- ์คํ์ผ ๋ฐ์ธ๋ฉ -->
    <p :style="{ fontSize: fontSize + 'px' }">
      this is paragraph
    </p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        fontSize: 16,
        altMsg: 'this is image',
        imageSrc: 'https://picsum.photos/200/300/',
        isRed: true,
        activeRed: 'active',
        myBackground: 'my-background-color',
      }
    })
    const myName = 'asdf'
  </script>
</body>
</html>
```

### v-for

- ์๋ฆฌ๋จผํธ ๋๋ ํํ๋ฆฟ ๋ธ๋ก์ ์ฌ๋ฌ ๋ฒ ๋ ๋๋ง
- item in items ๊ตฌ๋ฌธ ์ฌ์ฉ
- v-for ์ฌ์ฉ์ ๋ฐ๋์ key ์์ฑ์ ๊ฐ ์์์ ์์ฑ
- v-if ๋ณด๋ค v-for์ ์ฐ์ ์์๊ฐ ๋ ๋๋ค.

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <h2>String</h2>
      <div v-for="char in myStr">
        {{ char }}
      </div>
    <h2>Array</h2>
    <div v-for="fruit in fruits">
      {{ fruit }}
    </div>
    <div v-for="(fruit, idx) in fruits" :key="idx">
      {{ idx }} => {{ fruit }} 
    </div>
    
    <div v-for="todo in todos" :key="`todo-${todo.id}`">
      <p>{{ todo.title }} => {{ todo.completed }}</p>
    </div>

    <h2>Object</h2>
    <div v-for="value in myObj">
      {{ value }}
    </div>
    <div v-for="(value, key) in myObj">
      {{ key }} => {{ value }}
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        myStr: 'Hello World!',
        fruits: ['apple', 'banana', 'coconut'],
        todos: [
          { id: 1, title: 'todo1', completed: true },
          { id: 2, title: 'todo2', completed: false },
          { id: 3, title: 'todo3', completed: true },
        ],
        myObj: {
          name: 'kim',
          age: 100,
        }
      }
    }) 
  </script>
</body>
</html>
```

### v-model

- HTML form ์์์ ๊ฐ๊ณผ data๋ฅผ ์๋ฐฉํฅ ๋ฐ์ธ๋ฉ
- ์๋ ฅ์ ๋ฐ๋ผ ๋ฐ์ดํฐ๋ค์ ํ ๋ฒ์ ๋ฐ๊ฟ ์ ์๋ค.
- ์์์ด
  - .lazy : input ๋์  change ์ด๋ฒคํธ ์ดํ์ ๋๊ธฐํ
  - .number : ๋ฌธ์์ด์ ์ซ์๋ก ๋ณ๊ฒฝ
  - .trim : ์๋ ฅ์ ๋ํ trim์ ์งํ(์ ๊ณต๋ฐฑ ์ ๊ฑฐ)

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <h2>Input -> Data ๋จ๋ฐฉํฅ</h2>
    <p>{{ msg1 }}</p>
    <input type="text" @input="onInputChange">
    <hr>
    <h2>Input <-> Data ์๋ฐฉํฅ</h2>
    <p>{{ msg2 }}</p>
    <input type="text" v-model="msg2">
    <hr>
    ์ณ! <input id="box" type="checkbox" v-model="checked">
    <label for="box">{{ checked }}</label>


  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        msg1: '111',
        msg2: '222',
        checked: true,
      },
      methods: {
        onInputChange (event) {
          this.msg1 = event.target.value
        }
      },

    })
  </script>
</body>
</html>
```

### v-on

- ์๋ฆฌ๋จผํธ์ ์ด๋ฒคํธ ๋ฆฌ์ค๋๋ฅผ ์ฐ๊ฒฐ
- ์ด๋ฒคํธ ์ ํ์ ์ ๋ฌ์ธ์๋ก ํ์
- ํน์  ์ด๋ฒคํธ๊ฐ ๋ฐ์ํ์ ๋, ์ฃผ์ด์ง ์ฝ๋๊ฐ ์คํ ๋จ
- ์ฝ์ด : `@`
  - v-on:click => @click

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <!-- ๋ฉ์๋ ํธ๋ค๋ฌ -->
    <button v-on:click="alertHello">Button</button>
    <button @click="alertHello">Button</button>
    <!-- ๊ธฐ๋ณธ ๋์ ๋ฐฉ์ง -->
    <form action="" @submit.prevent="alertHello">
      <button>GoGo</button>
    </form>

    <!-- ํค ๋ณ์นญ์ ์ด์ฉํ ํค ์๋ ฅ ์์์ด -->
    <input type="text" @keyup.enter="log"> 
    <!-- cb ํจ์์์ ํน์๋ฌธ๋ฒ () -->
    <input type="text" @keyup.enter="log('ssafy')"> 
    
    <p>{{ message }}</p>
    <button @click="changeMessage">change message</button>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      // ๊ฐ
      data: {
        message: 'Hello Vue',
      },
      // ํ๋(ํจ์)
      methods: {
        alertHello: function () {
          alert('hello')
        },
        log: function (something) {
          console.log(something)
        },
        changeMessage() {
          this.message = 'New message!!!'
        },
      }

    })
  </script>
</body>
</html>
```



## ๐ Lifecycle Hook

- ์์ ์ฃผ๊ธฐ - ์ธ๋ถ API์์ ์ด๊ธฐ ๋ฐ์ดํฐ ๋ฐ์์ฌ ๋ ๋ง์ด ํ๋ค.

- ๊ฐ Vue ์ธ์คํด์ค๋ ์์ฑ๋  ๋ ์ผ๋ จ์ ์ด๊ธฐํ ๊ณผ์ ์ ๊ฑฐ์น๋ค.

  - created
    - vue ์ธ์คํด์ค๊ฐ ์๊ฒจ๋ฌ์ ๋(ํ๋ฉด์ด ๋ ๋๋ง๋๊ธฐ ์ )
  - mounted
    - ์์ฑ๋ ๊ฒ ํ๋ฉด์ ๋ถ์ฐฉ

  - updated
    - ์๊ฐ ์๊ฐ ๋ฐ์ ํ  ๋

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <img v-if="imgSrc" :src="imgSrc" alt="sample img">
    <button @click="getImg">GetDog</button>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const API_URL = 'https://dog.ceo/api/breeds/image/random'
    const app = new Vue({
      el: '#app',
      data: {
        imgSrc: '',
      },
      methods: {
        getImg: function () {
          axios.get(API_URL)
            .then(response => {
              this.imgSrc = response.data.message
            })
        }
      },
      // ์ธ๋ถ API์์ ์ด๊ธฐ ๋ฐ์ดํฐ ๋ฐ์์ค๊ธฐ
      created: function () {
        this.getImg()
        //console.log('created!')
      },
      // mounted: function () {
      //   console.log('mounted!')
      // },
      // updated: function () {
      //   console.log('updated!')
      // }
    })
  </script>
</body>
</html>
```



