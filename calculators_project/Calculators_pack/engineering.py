import Calculators_pack
from Calculators_pack.utils import util
class EngineeringCalculator(Calculators_pack.basic.Calculator):

    # 나눗셈 (오버라이딩)
    def divide(self,*args : float,**kwargs: dict):
        try:    
            result = Calculators_pack.reduce(lambda x,y: x/y,args)
        except ZeroDivisionError as e:
            return "0으로 나누려고하셨습니다 종료합니다"
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except Exception as e:
            pass
        return str(result)
        
    # 제곱근
    def square_root(self,x : float, **kwargs:dict):
        result = x**(1/2)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
    
    # 거듭제곱
    def power(self,x: float, y: int, **kwargs:dict):
        result = x**y
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
        
    # 로그
    def log(self,x: float, base:float=10, **kwargs:dict):
        result = Calculators_pack.math.log(x,base)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
    
    # 자연 로그
    def ln(self,x:float, **kwargs:dict): 
        result=self.log(x,Calculators_pack.math.e,kwargs=kwargs)
        return str(result)
    
    # 사인함수
    def sin(self,x:float, **kwargs:dict):
        try :
            if kwargs["angle_unit"]=="degree":
                x=Calculators_pack.math.radians(x)   
        except :
            pass
        result = Calculators_pack.math.sin(x)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
    
    # 코사인함수
    def cos(self,x:float, **kwargs:dict):
        try :
            if kwargs["angle_unit"]=="degree":
                x=Calculators_pack.math.radians(x)   
        except :
            pass
        result = Calculators_pack.math.cos(x)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
    
    # 탄젠트
    def tan(self,x:float, **kwargs:dict):
        try :
            if kwargs["angle_unit"]=="degree":
                x=Calculators_pack.math.radians(x)   
        except :
            pass
        result = Calculators_pack.math.tan(x)
        try:
            if kwargs["return_float"] is True:
                result = float(result)
        except Exception as e:
            pass
        try :
            return util.round_result(result,kwargs["precision"])
        except:
            pass
        return str(result)
