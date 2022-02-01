# [Python] 패키지

모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

패키지 : 특정 기능과 관련된 여러 모듈의 집합, 패키지 안에는 또 다른 서브 패키지를 포함

import로 모듈과 패키지를 불러옴

ex). `import random`

컴퓨터 공학에서 *은 모든이란 뜻으로 많이 쓰인다!!

exl). `import module` -> `from module import *` 

이러면 module안의 모든 걸 불러온다.

---

파이썬 패키지 관리자(pip) 명령어

- 패키지 설치 `pip install` 	

  패키지 설치, 버전 명시해서 설치 가능

- 패키지 삭제 `pip uninstall`

- 패키지 목록 `pip list` , `pip show SomePackage`

- 패키지 목록 문서화!:

  `pip freeze > requirements.txt` 

  `pip install -r requirements.txt`

  패키지 버전을 동일하게 맞출 때 패키지 버전을 문서화시켜서 공유하기 위해 사용한다, 패키지 배포에 도움~!

---

패키지에는 `__init__.py`모듈을 만들어 패키지로 인식한다.

파이썬 3.3부터는 파일이 없어도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성

---

패키지의 모임이 라이브러리