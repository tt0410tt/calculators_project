from typing import Any, Dict, List, Tuple
import jiwer
from collections import OrderedDict
from nlptutti import utils

class ASRMetrics:
    """
    음성 인식 결과의 오류율(CER, WER, CRR)을 계산하는 클래스입니다.
    """
    def get_er(self, reference: str, transcription: str, metric: str, rm_punctuation: bool = True) -> Dict[str, Any]:
        """
        오류율(CER, WER, CRR)을 계산하여 결과를 반환합니다.

        :param reference: 참조 문자열
        :param transcription: 변환된 문자열
        :param metric: 'cer', 'wer', 'crr' 중 하나
        :param rm_punctuation: True이면 구두점을 제거합니다.
        :return: 오류율과 세부 정보를 포함한 딕셔너리
        """
        
        if metric not in ['cer', 'wer', 'crr']:
            raise ValueError("Invalid metric specified. Choose 'cer', 'wer', or 'crr'.")

        # CER과 CRR의 경우 공백 제거
        if metric in ['cer', 'crr']:
            refs = jiwer.RemoveWhiteSpace(replace_by_space=False)(reference)
            trans = jiwer.RemoveWhiteSpace(replace_by_space=False)(transcription)
        else:
            refs = reference
            trans = transcription

        # 구두점 제거
        if rm_punctuation:
            refs = jiwer.RemovePunctuation()(refs)
            trans = jiwer.RemovePunctuation()(trans)
        else:
            pass  # 이미 refs와 trans에 할당됨

        # 문자 수준 또는 단어 수준 결정
        if metric in ['cer', 'crr']:
            level = 'char'
        else:
            level = 'word'

        # 오류 측정
        hits, substitutions, deletions, insertions = utils.measure_er(self,refs, trans, level)

        incorrect = substitutions + deletions + insertions
        total = substitutions + deletions + hits + insertions

        # 오류율 계산
        if total > 0:
            er = incorrect / total
        else:
            er = 0

        if metric == 'crr':
            er = round(1 - er, 2)

        result = OrderedDict()
        result = {
            metric: er,
            'substitutions': substitutions,
            'deletions': deletions,
            'insertions': insertions,
            'hits': hits,
            'total': total,
        }
        return result
    