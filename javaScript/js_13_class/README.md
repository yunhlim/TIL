# [JavaScript] 클래스 [EP 13]

## 📚 클래스(Class)

> ES6에 객체 대신에 클래스를 정의하는 방식이 추가되었다.
> 1개의 클래스로 여러 객체를 만들 수 있다.

다른 언어의 클래스와 같다.

- 클래스 안에는 데이터가 없으며 메모리가 올라가지 않는다.
- 객체는 클래스의 인스턴스로 객체 안에 데이터가 있으며, 메모리가 올라간다.



프로퍼티는 클래스와 객체에 추가되는 변수

메소드는 클래스와 객체 추가되는 함수



## ⚙ 생성자 (Constructor)

- ES6

- 객체를 생성할 때 인자를 프로퍼티에 전달하여 생성한다.
- 즉, 객체를 만들 때 필요한 데이터를 전달하여 생성한다.

```javascript
class Person {
  constructor() {
      this.name = 'Max';
  }
  
  printMyName() {
      console.log(this.name);
  }
}
const person = new Person();
person.printMyName();
```



## 👪 상속

생성자 함수 안에 `super()` 메소드를 추가해야 한다.

`extends`로 상속한다.

```javascript
class Human {
    constructor() {
        this.gender = 'male';
    }
    
    printGender() {
        console.log(this.gender);
    }
}

class Person extends Human {
  constructor() {
      super();
      this.name = 'Max';
  }
  
  printMyName() {
      console.log(this.name);
  }
}
const person = new Person();
person.printMyName();
person.printGender();
```



### 생성자와 메서드의 최신 구문

- 생성자 함수보다 더 최신 구문 ES7

- 인자를 전달 할 필요없는 프로퍼티들은 contructor 밖에 선언해도 된다.

```javascript
class Person {
    name = 'Max';
}
```



- 메서드도 최신 구문은 화살표 함수를 사용하는 것이다.

- myMethod = () => {...}

- this 키워드를 사용하지 않는다는 장점!!

```javascript
  class Human {
    gender = 'male';
    
    printGender = () => {
      console.log(this.gender);
    }
  }

  class Person extends Human {

    name = 'Max';
    gender = 'female';
    
    
    printMyName = () => {
      console.log(this.name);
    }
  }
  const person = new Person();
  person.printMyName();
  person.printGender();
```

