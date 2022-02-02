# [Python] 내장함수(built-in Function)

## divmod()

`divmod(a,b)` a를 b로 나눈 몫과 나머지를 tuple로 변환

## len()

자료형의 길이 반환

## enumerate()

index와 value를 (index,value) tuple로 묶어준다.

set와 dictionary도 임의로 index 매겨 tuple로 묶어준다!

dictionary는 (index, key)로 묶는다.

## map()

`map(function, iterable)`순회가능한 객체의 인수들에 각각 function를 적용시킬 때 사용한다.

정수형이나 실수형 input 여러 개 넣어줄 때 많이 사용한다.

`map(int, input().split())`

## filter()

`filter(function, iterable)`순회 가능한 객체의 인수 중 function를 적용시켰을 때 **True**인 값만 반환한다.

## zip()

`zip(*iterables)` : 같은 인덱스끼리 tuple로 묶어 iterator로 반환한다. 2개를 넘어도 가능하며, 개수가 다르면 짧은 쪽에 맞추어 긴 쪽의 길이를 줄여서 반환한다.

## int(), float()

주의사항 : 문자열을 int와 float을 바꿀 때 바꿀 수 있는 형태인지 확인해야한다.

`int('a'), float('a')`=> 이런건 에러가 뜬다.

`int('1.2')` => 이것도 에러

`int(1.2)` => 이건 자동으로 실수형을 소수점이하를 없애고 정수형으로 바꾼다.