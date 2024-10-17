# nlptutti/asr_metrics.py

from nlptutti.utils import levenshtein_distance, remove_punctuation
from typing import Dict, Tuple

class ASRMetrics:
    """
    음성 인식 결과의 오류율(CER, WER, CRR)을 계산하는 클래스입니다.
    """

    def get_cer(self, reference: str, transcription: str, rm_punctuation: bool = True) -> Dict[str, float]:
        """
        문자 오류율 (CER)을 계산하여 결과를 반환합니다.
        """
        if rm_punctuation:
            reference = remove_punctuation(reference)
            transcription = remove_punctuation(transcription)

        ref_chars = list(reference)
        hyp_chars = list(transcription)

        distance, (substitutions, insertions, deletions) = levenshtein_distance(ref_chars, hyp_chars)
        total_chars = len(ref_chars)
        cer = (substitutions + insertions + deletions) / max(total_chars, 1)

        result = {
            'cer': cer,
            'substitutions': substitutions,
            'deletions': deletions,
            'insertions': insertions,
            'total_chars': total_chars,
        }
        return result

    def get_wer(self, reference: str, transcription: str, rm_punctuation: bool = True) -> Dict[str, float]:
        """
        단어 오류율 (WER)을 계산하여 결과를 반환합니다.
        """
        if rm_punctuation:
            reference = remove_punctuation(reference)
            transcription = remove_punctuation(transcription)

        ref_words = reference.split()
        hyp_words = transcription.split()

        distance, (substitutions, insertions, deletions) = levenshtein_distance(ref_words, hyp_words)
        total_words = len(ref_words)
        wer = (substitutions + insertions + deletions) / max(total_words, 1)

        result = {
            'wer': wer,
            'substitutions': substitutions,
            'deletions': deletions,
            'insertions': insertions,
            'total_words': total_words,
        }
        return result

    def get_crr(self, reference: str, transcription: str, rm_punctuation: bool = True) -> Dict[str, float]:
        """
        문자 인식률 (CRR)을 계산하여 결과를 반환합니다.
        """
        cer_result = self.get_cer(reference, transcription, rm_punctuation)
        total_chars = cer_result['total_chars']
        correct_chars = total_chars - (cer_result['substitutions'] + cer_result['deletions'])
        crr = correct_chars / max(total_chars, 1)

        result = {
            'crr': crr,
            'substitutions': cer_result['substitutions'],
            'deletions': cer_result['deletions'],
            'insertions': cer_result['insertions'],
            'total_chars': total_chars,
            'correct_chars': correct_chars,
        }
        return result
