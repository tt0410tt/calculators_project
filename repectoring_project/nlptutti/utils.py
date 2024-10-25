# nlptutti/utils.py

from typing import List, Tuple
import unicodedata

def levenshtein(self, u: str, v: str) -> Tuple[int, Tuple[int, int, int]]:
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

def remove_punctuation(text: str) -> str:
    """
    문자열에서 구두점을 제거합니다.
    """
    return ''.join(ch for ch in text if unicodedata.category(ch)[0] != 'P')

def measure_er(self, reference: str, transcription: str, level: str) -> Tuple[int, int, int, int]:
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

            _, (s, i, d) = levenshtein(self,hyp_tokens, ref_tokens)
            total_s += s
            total_i += i
            total_d += d
            total_n += len(ref_tokens)

        substitutions = total_s
        deletions = total_d
        insertions = total_i
        hits = total_n - (substitutions + deletions)

        return hits, substitutions, deletions, insertions
"""
def get_unicode_code(text: str) -> str:
    
    #유니코드 문자를 '\\uXXXX' 형식으로 변환한 문자열을 반환합니다.
    
    return ''.join(f'\\u{ord(c):04x}' if ord(c) > 127 else c for c in text)
"""