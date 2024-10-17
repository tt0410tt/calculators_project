# nlptutti/utils.py

from typing import List, Tuple
import unicodedata

def levenshtein_distance(ref: List[str], hyp: List[str]) -> Tuple[int, Tuple[int, int, int]]:
    """
    레벤슈타인 거리를 계산하고 대체, 삽입, 삭제 연산의 수를 반환합니다.
    """
    m = len(ref)
    n = len(hyp)

    distance_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    op_matrix = [[(0, 0, 0)] * (n + 1) for _ in range(m + 1)]  # (substitutions, insertions, deletions)

    for i in range(m + 1):
        distance_matrix[i][0] = i
        if i > 0:
            op_matrix[i][0] = (0, 0, i)
    for j in range(n + 1):
        distance_matrix[0][j] = j
        if j > 0:
            op_matrix[0][j] = (0, j, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ref[i - 1] == hyp[j - 1]:
                cost = 0
            else:
                cost = 1

            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1] + cost

            min_distance = min(deletion, insertion, substitution)

            distance_matrix[i][j] = min_distance

            if min_distance == substitution:
                subs, ins, dels = op_matrix[i - 1][j - 1]
                if cost == 1:
                    subs += 1
            elif min_distance == insertion:
                subs, ins, dels = op_matrix[i][j - 1]
                ins += 1
            else:  # deletion
                subs, ins, dels = op_matrix[i - 1][j]
                dels += 1

            op_matrix[i][j] = (subs, ins, dels)

    substitutions, insertions, deletions = op_matrix[m][n]
    return distance_matrix[m][n], (substitutions, insertions, deletions)

def remove_punctuation(text: str) -> str:
    """
    문자열에서 구두점을 제거합니다.
    """
    return ''.join(ch for ch in text if unicodedata.category(ch)[0] != 'P')

def get_unicode_code(text: str) -> str:
    """
    유니코드 문자를 '\\uXXXX' 형식으로 변환한 문자열을 반환합니다.
    """
    return ''.join(f'\\u{ord(c):04x}' if ord(c) > 127 else c for c in text)
