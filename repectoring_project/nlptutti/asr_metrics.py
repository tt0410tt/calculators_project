from typing import Any, Dict, List, Tuple
import jiwer
from collections import OrderedDict

class ASRMetrics:
    """
    음성 인식 결과의 오류율(CER, WER, CRR)을 계산하는 클래스입니다.
    """

    def __init__(self):
        pass

    def levenshtein(self, u: List[Any], v: List[Any]) -> Tuple[int, Tuple[int, int, int]]:
        """
        레벤슈타인 거리를 계산하고 대체, 삽입, 삭제 연산의 수를 반환합니다.
        """
        prev = None
        curr = [0] + list(range(1, len(v) + 1))
        # 연산: (대체, 삽입, 삭제)
        prev_ops = None
        curr_ops = [(0, 0, i) for i in range(len(v) + 1)]
        for x in range(1, len(u) + 1):
            prev, curr = curr, [x] + ([None] * len(v))
            prev_ops, curr_ops = curr_ops, [(0, x, 0)] + ([None] * len(v))
            for y in range(1, len(v) + 1):
                delcost = prev[y] + 1
                addcost = curr[y - 1] + 1
                subcost = prev[y - 1] + int(u[x - 1] != v[y - 1])
                curr[y] = min(subcost, delcost, addcost)
                if curr[y] == subcost:
                    (n_s, n_d, n_i) = prev_ops[y - 1]
                    curr_ops[y] = (n_s + int(u[x - 1] != v[y - 1]), n_d, n_i)
                elif curr[y] == delcost:
                    (n_s, n_d, n_i) = prev_ops[y]
                    curr_ops[y] = (n_s, n_d + 1, n_i)
                else:
                    (n_s, n_d, n_i) = curr_ops[y - 1]
                    curr_ops[y] = (n_s, n_d, n_i + 1)
        return curr[len(v)], curr_ops[len(v)]

    def _measure_er(self, reference: str, transcription: str, level: str) -> Tuple[int, int, int, int]:
        """
        오류율 계산에 필요한 대체, 삭제, 삽입, 일치의 수를 반환합니다.
        """
        ref_list = [reference]
        hyp_list = [transcription]

        total_s, total_i, total_d, total_n = 0, 0, 0, 0

        for n in range(len(ref_list)):
            if level == 'char':
                ref_tokens = list(ref_list[n])
                hyp_tokens = list(hyp_list[n])
            elif level == 'word':
                ref_tokens = ref_list[n].split()
                hyp_tokens = hyp_list[n].split()
            else:
                raise ValueError("Invalid level specified. Choose 'char' or 'word'.")

            _, (s, i, d) = self.levenshtein(hyp_tokens, ref_tokens)
            total_s += s
            total_i += i
            total_d += d
            total_n += len(ref_tokens)

        substitutions = total_s
        deletions = total_d
        insertions = total_i
        hits = total_n - (substitutions + deletions)

        return hits, substitutions, deletions, insertions

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
        hits, substitutions, deletions, insertions = self._measure_er(refs, trans, level)

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
    