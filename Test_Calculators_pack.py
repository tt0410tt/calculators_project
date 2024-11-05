import Calculators_pack

if __name__ == '__main__':
    calc=Calculators_pack.Calculator()
    # 테스트 케이스 과제 양식
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
    print(calc.multiply(2, 3, 4))  # 출-력: 24
    print(calc.divide(100, 2, precision=3))  # 출력: 50.000

    # 테스트 케이스 추가 양식
    # 덧셈
    print(calc.add(5, 6, 7, 8, 9, 10, precision=2, return_float=True))  # 45.00
    print(calc.add(5, 6, 7, 8, 9, 10, precision=3))  # 45.000 (정수)

    # 뺄셈
    print(calc.subtract(100, 25, 30, precision=2, return_float=True))  # 45.00
    print(calc.subtract(100, 25, 30, precision=3))  # 45.000 (정수)

    # 곱셈
    print(calc.multiply(2, 3, 4, precision=2, return_float=True))  # 24.00
    print(calc.multiply(2, 3, 4, precision=3))  # 24.000 (정수)

    # 나눗셈
    print(calc.divide(100, 2, precision=2, return_float=True))  # 50.00
    print(calc.divide(100, 2, precision=3))  # 50.000 (정수)
    

    # EngineeringCalculator 클래스 테스트
    calc = Calculators_pack.EngineeringCalculator()
    
    # 테스트 케이스 과제 양식
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(calc.square_root(16, precision=3))  # 출력: 4.000
    print(calc.log(100, precision=4))  # 출력: 2.0000
    print(calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000
    try:
        print(calc.divide(5, 0))
    except ZeroDivisionError as e:
        print(e)  # 출력: "Division by zero is not allowed"

    # 나눗셈 테스트
    print("나눗셈 테스트:")
    print("10 / 2 =", calc.divide(10, 2))  # 예상 결과: '5.0'
    print("10 / 0 =", calc.divide(10, 0))  # 예상 결과: "0으로 나누려고하셨습니다 종료합니다"
    print("10 / 3 (소수점 2자리):", calc.divide(10, 3, precision=2))  # 예상 결과: '3.33'

    print("\n제곱근 테스트:")
    print("√9 =", calc.square_root(9))  # 예상 결과: '3.0'
    print("√2 (소수점 3자리):", calc.square_root(2, precision=3))  # 예상 결과: '1.414'

    print("\n거듭제곱 테스트:")
    print("2^3 =", calc.power(2, 3))  # 예상 결과: '8.0'
    print("5^2 =", calc.power(5, 2))  # 예상 결과: '25.0'
    print("2^3 (소수점 1자리):", calc.power(2, 3, precision=1))  # 예상 결과: '8.0'

    print("\n로그 테스트:")
    print("log₁₀(100) =", calc.log(100, 10))  # 예상 결과: '2.0'
    print("log₂(8) =", calc.log(8, 2))  # 예상 결과: '3.0'
    print("log₂(8) (소수점 2자리):", calc.log(8, 2, precision=2))  # 예상 결과: '3.00'

    print("\n자연 로그 테스트:")
    print("ln(e) =", calc.ln(2.718281828459045, precision=5))  # 예상 결과: '1.00000'

    print("\n사인 함수 테스트:")
    print("sin(0) =", calc.sin(0))  # 예상 결과: '0.0'
    print("sin(90°) =", calc.sin(90, angle_unit='degree'))  # 예상 결과: '1.0'
    print("sin(30°) (소수점 2자리):", calc.sin(30, angle_unit='degree', precision=2))  # 예상 결과: '0.50'

    print("\n코사인 함수 테스트:")
    print("cos(0) =", calc.cos(0))  # 예상 결과: '1.0'
    print("cos(90°) =", calc.cos(90, angle_unit='degree'))  # 예상 결과: '0.0'
    print("cos(60°) (소수점 2자리):", calc.cos(60, angle_unit='degree', precision=2))  # 예상 결과: '0.50'

    print("\n탄젠트 함수 테스트:")
    print("tan(0) =", calc.tan(0))  # 예상 결과: '0.0'
    print("tan(45°) =", calc.tan(45, angle_unit='degree'))  # 예상 결과: '1.0'
    print("tan(60°) (소수점 2자리):", calc.tan(60, angle_unit='degree', precision=2)) # 예상 결과: '1.73'