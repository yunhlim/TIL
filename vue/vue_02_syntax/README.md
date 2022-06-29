# [Vue] Vue 문법 [EP 02]

## 📒 Vue.js CDN

### Vue.js CDN 참고 문서

- [시작하기](https://kr.vuejs.org/v2/guide/index.html) 자습서를 따라하며 연습!



### Vue instance

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작한다.
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
        message: '안녕하세요'
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



## 📖 선언적 렌더링

### el

- 어떤 돔 요소에 부착할 것인지
- new를 이용한 인스턴스 생성 때만 사용

### data

- Vue 인스턴스의 데이터 객체
- Vue 인스턴스의 상태 데이터 정의
- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능
- Vue template에서 interpolation으로 접근 가능 => 둘 다 innerText

### methods

- Vue 인스턴스에 추가할 메서드
- 화살표 함수를 메서드를 정의하는데 사용하면 안된다.
  - Vue 함수 객체 내에서 vue 인스턴스를 가리킨다.
  - 화살표 함수에서 this는 window를 가리킨다.

```javascript
var app = new Vue({
  el: '#app',
  data: {
    message: '안녕하세요 Vue!'
  },
  methods: {
    greeting: function () {
      console.log('hello')
    }
  }
})
```

### computed

- (데이터에 의존하는) 계산된 값

- 내부적으로 알아서 실행해놓은 **값**이지 함수로 쓰여지지 않는다.
- 종속된 데이터가 변경될 때만 함수를 실행

- 리턴 값이 무조건 있어야 한다.

- getter - data를 통해 값을 얻는다.

  > method는 데이터를 바꾸는 로직(setter)

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
> computed는 종속된 대상이 변경되지 않는 한 여러 번 호출해도 계산을 다시 하지 않고 계산되어 있던 결과를 반환
>
> methods를 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행
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
>       // data를 바꾸는 로직 위주! (setter 함수들)
>       methods: {
>         reverseMessage() {
>           console.log('method!!')
>           return this.message.split('').reverse().join('')
>         },
>       },
>       // data를 통한 값을 얻음! (getter 함수들)
>       computed: {
>         // (data에 의존하는)계산된 값
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

- computed와 똑같이 주시하고 있다가 콜백 함수를 실행(트리거만 건다.)

- 선언형이 아닌 명령형 프로그래밍 방식

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
          console.log(`${this.num}이 변경되었습니다.`)
        }
      },
    })
  </script>
</body>
</html>

```

### filter

- filter는 장고의 필터와 유사

- 텍스트 형식화를 적용하기 위해 많이 쓴다.

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



## 🎯 Directive (디렉티브)

- v- 접두사가 있는 특수 속성

- 속성 값은 단일 JS 표현식이 됨 (v-for 예외)

- 표현식의 값이 변결될 때 반응적으로 DOM에 적용하는 역할을 함

- 전달인자 `:` : 콜론을 통해 전달인자를 받는다.

  ```vue
  <a v-on:click="function"></a>
  ```

- 수식어 `.` : 점으로 표시, directive를 특별한 방법으로 바인딩

  ```vue
  <form v-on:submit.prevent="function"></form>
  ```

### v-text

- interpolation 문법이 v-text이다.

  ```vue
  <p v-text="message"></p>
  <!-- 같다 -->
  <p>{{ message }}</p>
  ```

> v-html
>
> XSS 공격에 취약할 수 있음
>
> 사용자로부터 입력받은 내용은 v-html **절대** 사용 금지

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

- 조건부 렌더링 중 하나
- 요소는 항상 렌더링 되고 DOM에 남아있음
- 단순히 엘리먼트에 display CSS 속성을 토글

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
- 조건부 렌더링 중 하나
- 조건에 따라 요소를 렌더링

> v-show 와 v-if
>
> 눈에 보이냐 안 보이냐(토클로) show는 hidden으로 만들지만,  if는 렌더링 조차 안한다.
>
> 자주 변경되면 show, 가끔 변경되면 v-if

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

- 속성 바인딩, 클래스 바인딩
- HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당
- **정말 정말 많이 쓰인다.**
- 약어 : `:`(콜론)
  - v-bind:href 와 :href가 같다

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
    <!-- 속성 바인딩 -->
    <img v-bind:src="imageSrc" :alt="altMsg">
    <img :src="imageSrc" alt="altMsg">
    <hr>

    <!-- 클래스 바인딩 -->
    <div :class="{ active: isRed }">
      클래스 바인딩
    </div>

    <h3 :class="[activeRed, myBackground]">
      hello vue
    </h3>
    <hr>

    <!-- 스타일 바인딩 -->
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

- 엘리먼트 또는 템플릿 블록을 여러 번 렌더링
- item in items 구문 사용
- v-for 사용시 반드시 key 속성을 각 요소에 작성
- v-if 보다 v-for의 우선순위가 더 높다.

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

- HTML form 요소의 값과 data를 양방향 바인딩
- 입력에 따라 데이터들을 한 번에 바꿀 수 있다.
- 수식어
  - .lazy : input 대신 change 이벤트 이후에 동기화
  - .number : 문자열을 숫자로 변경
  - .trim : 입력에 대한 trim을 진행(양 공백 제거)

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
    <h2>Input -> Data 단방향</h2>
    <p>{{ msg1 }}</p>
    <input type="text" @input="onInputChange">
    <hr>
    <h2>Input <-> Data 양방향</h2>
    <p>{{ msg2 }}</p>
    <input type="text" v-model="msg2">
    <hr>
    쳌! <input id="box" type="checkbox" v-model="checked">
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

- 엘리먼트에 이벤트 리스너를 연결
- 이벤트 유형은 전달인자로 표시
- 특정 이벤트가 발생했을 때, 주어진 코드가 실행 됨
- 약어 : `@`
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
    <!-- 메서드 핸들러 -->
    <button v-on:click="alertHello">Button</button>
    <button @click="alertHello">Button</button>
    <!-- 기본 동작 방지 -->
    <form action="" @submit.prevent="alertHello">
      <button>GoGo</button>
    </form>

    <!-- 키 별칭을 이용한 키 입력 수식어 -->
    <input type="text" @keyup.enter="log"> 
    <!-- cb 함수에서 특수문법 () -->
    <input type="text" @keyup.enter="log('ssafy')"> 
    
    <p>{{ message }}</p>
    <button @click="changeMessage">change message</button>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      // 값
      data: {
        message: 'Hello Vue',
      },
      // 행동(함수)
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



## 📗 Lifecycle Hook

- 생애주기 - 외부 API에서 초기 데이터 받아올 때 많이 한다.

- 각 Vue 인스턴스는 생성될 때 일련의 초기화 과정을 거친다.

  - created
    - vue 인스턴스가 생겨났을 때(화면이 렌더링되기 전)
  - mounted
    - 생성된 게 화면에 부착

  - updated
    - 순간 순간 반응 할 때

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
      // 외부 API에서 초기 데이터 받아오기
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



