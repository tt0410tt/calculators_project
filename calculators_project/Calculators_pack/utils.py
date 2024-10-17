from Calculators_pack import math
class util:
    # 결과값을 지정된 정밀도로 반올림해서 문자열로 리턴하는 함수
    # 특이사항 리턴값이 str, 뒷자리를 반올림하고 표시할수 없으면 추가를 위함
    def round_result(value:float,precision:int)-> str:
        round(value,precision)
        return '{:.{}f}'.format(float(value), precision)
    
    # 각도 및 라디안을 라디안으로 변환해서 float로 리턴하는 함수
    def convert_to_radians(angle : float, uint : str = "radian") -> float:
        if uint == "dgree":
            return float(math.radians(angle))
        return float(angle)