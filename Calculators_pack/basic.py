from Calculators_pack import reduce
from Calculators_pack import utils
# 계산기 클래스
# 메소드 = add,subtract,multiply,divide
class Calculator:
    # 모든메소드 공통사항
    # 리턴되는값 자료형 float to str 1개
    # 매개변수 *args float로 변환 가능한 숫자들의 튜플
    # 딕셔너리 **kwargs str(precision) : int, str(return_float) : bool 

    # 덧셈 메소드
    def add(self,*args: float,**kwargs:dict):# 타입 힌팅 추가
        if "return_float" in kwargs.keys() and kwargs["return_float"] is True:
            result=float(sum(args))
        else :
            result=sum(args)
        if "precision" in kwargs.keys():
            round_disit = int(kwargs["precision"])
            # 포맷을사용하여 기존 round만으로는 나타낼수없는경우 ex)5.00을 표현
            return '{:.{}f}'.format(result, round_disit)
        return str(result)
    
    # 뺄셈 메소드
    def subtract(self, *args: float,**kwargs:dict):
        result = reduce(lambda x, y: x - y, args)
        
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return utils.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)

    
    # 곱셈 메소드
    def multiply(self,*args: float,**kwargs:dict):
        result = reduce(lambda x,y: x*y,args)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return utils.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
    
    # 나눗셈 메소드
    def divide(self,*args: float,**kwargs:dict):
        result = reduce(lambda x,y: x/y,args)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return utils.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
