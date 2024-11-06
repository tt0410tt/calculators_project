이 패키지는 공학용 계산기를 python으로 구현한것이며 다음의 조건을 최대한 지키면서 제작 및 변경되어졌습니다.

# 폴더 트리구조
.
├── Calculators_pack  
│   ├── basic.py  
│   ├── engineering.py  
│   ├── __init__.py  
│   └── utils.py  
├── .gitignore  
├──  LICENSE.txt  
├── readme.md  
└── Test_Calculators_pack.py  

# 문제 1: 기본 계산기 클래스 구현

`Calculator` 클래스를 만드세요. 이 클래스는 기본적인 산술 연산을 제공해야 합니다.

요구사항:

1. 다음 메서드를 구현하세요:
    - `add(*args, **kwargs)`: 덧셈
    - `subtract(*args, **kwargs)`: 뺄셈
    - `multiply(*args, **kwargs)`: 곱셈
    - `divide(*args, **kwargs)`: 나눗셈
    
2. 각 메서드는 위치 인자(`args`)와 키워드 인자(`*kwargs`)를 받아야 합니다.

3. `*kwargs`에는 다음 키를 사용할 수 있어야 합니다:
    - `precision`: 결과의 소수점 자릿수 지정 (기본값: None, 즉 반올림하지 않음)
    - `return_float`: True일 경우 항상 float 타입 반환, False일 경우 가능하면 int 반환 (기본값: False)
4. 0으로 나누기 등의 에러 상황을 적절히 처리해야 합니다.


# 문제 2: 공학용 계산기 클래스 구현

`Calculator` 클래스를 상속받아 `EngineeringCalculator` 클래스를 만드세요. 이 클래스는 기본 계산기의 기능을 모두 포함하면서 추가적인 공학 계산 기능을 제공해야 합니다.

요구사항:

1. `Calculator` 클래스의 모든 메서드를 상속받으세요.
2. 다음 새로운 메서드를 추가하세요:
    - `square_root(x, **kwargs)`: 제곱근
    - `power(x, y, **kwargs)`: 거듭제곱
    - `log(x, base=10, **kwargs)`: 로그 (기본값은 상용로그)
    - `ln(x, **kwargs)`: 자연로그
    - `sin(x, **kwargs)`: 사인
    - `cos(x, **kwargs)`: 코사인
    - `tan(x, **kwargs)`: 탄젠트
3. 모든 메서드는 `*kwargs`를 통해 `precision`과 `return_float` 인자를 받아야 합니다.
4. `divide` 메서드를 오버라이드하여, 0으로 나누려고 할 때 사용자 정의 예외 `DivisionByZeroError`를 발생시키세요.
5. 각 삼각함수 메서드에 `angle_unit` 키워드 인자를 추가하여 'degree' 또는 'radian' 단위로 입력을 받을 수 있게 하세요. 기본값은 'radian'으로 설정하세요.  

추가 과제:

1. 타입 힌팅을 사용하여 모든 메서드와 함수의 입력 및 출력 타입을 명시하세요.
2. 두 계산기 클래스에 대한 간단한 문서화를 작성하세요. (클래스, 메서드, 예외 등)


# 문제 3: 계산기 모듈 만들기

앞서 만든 `Calculator`와 `EngineeringCalculator` 클래스를 사용하여 `calculator.py` 모듈을 만드세요.

요구사항:

1. `calculator.py` 파일을 생성하고 앞서 구현한 두 클래스를 이 파일에 포함시키세요.
2. 모듈 레벨에서 간단한 사용 예시를 포함하는 문서화 문자열(docstring)을 추가하세요.
3. `if __name__ == '__main__'` 블록을 사용하여 모듈이 직접 실행될 때 간단한 데모를 실행하도록 구현하세요. 이 데모는 각 계산기의 주요 기능을 보여주어야 합니다.
4. 모듈 내에 `__all__` 변수를 정의하여 외부에서 import * 를 사용할 때 노출될 이름들을 명시하세요.


# 문제 4: 계산기 패키지 만들기

앞서 만든 계산기 모듈을 확장하여 `calculator` 패키지를 만드세요.

요구사항:

1. `calculator` 디렉토리를 만들고 그 안에 다음 파일들을 생성하세요:
    - `__init__.py`
    - `basic.py` (기본 계산기 클래스 포함)
    - `engineering.py` (공학용 계산기 클래스 포함)
    - `utils.py` (공통으로 사용되는 유틸리티 함수 포함)
2. `__init__.py`에서 필요한 클래스와 함수를 import하여 패키지 레벨에서 사용할 수 있게 만드세요.
3. `utils.py`에 다음 함수를 구현하세요:
    - `round_result(value, precision)`: 결과값을 지정된 정밀도로 반올림하는 함수
    - `convert_to_radians(angle, unit)`: 각도를 라디안으로 변환하는 함수
4. 각 모듈(`basic.py`, `engineering.py`, `utils.py`)에 적절한 문서화를 추가하세요.
5. 패키지의 루트 디렉토리에 `README.md` 파일을 생성하고, 패키지의 사용법과 예시를 포함한 기본적인 문서를 작성하세요.

# 추가 과제:

1. GitHub에 올릴 수 있는 형식으로 프로젝트를 구성하세요. 이는 다음을 포함해야 합니다:
    - 자세한 [README.md](http://readme.md/) 파일
    - LICENSE 파일
    - requirements.txt (필요한 경우)
    - [setup.py](http://setup.py/) 또는 pyproject.toml 파일 (패키지 설치를 위해)
    - .gitignore 파일
    - 테스트 디렉토리와 테스트 코드

# 추가 과제 : git올리기
# 추가 과제 : 도커 활용해보기