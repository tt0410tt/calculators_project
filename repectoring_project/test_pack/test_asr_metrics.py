# test_pack/test_asr_metrics.py

import unittest
from nlptutti.asr_metrics import ASRMetrics

class TestASRMetrics(unittest.TestCase):
    """
    ASRMetrics 클래스의 메서드를 테스트하는 클래스입니다.
    """

    def setUp(self):
        self.metrics = ASRMetrics()
        self.test_cases_cer = [
            {
                'reference': '아키택트',
                'transcription': '아키택쳐',
                'expected_cer': 0.25,
                'description': '한글 단어 CER 테스트'
            },
            {
                'reference': '제이 차 세계 대전은 인류 역사상 가장 많은 인명 피해와 재산 피해를 남긴 전쟁이었다',
                'transcription': '제이차 세계대전은 인류 역사상 가장많은 인명피해와 재산피해를 남긴 전쟁이었다',
                'expected_cer': 0.0,
                'description': '한글 문장 CER 테스트'
            },
            # 추가 테스트 케이스
        ]
        self.test_cases_wer = [
            {
                'reference': '대한민국은 주권 국가 입니다.',
                'transcription': '대한민국은 주권국가 입니다.',
                'expected_wer': 0.5,
                'description': '한글 문장 WER 테스트'
            },
            # 추가 테스트 케이스
        ]

    def test_get_cer(self):
        """
        get_cer 메서드의 여러 케이스를 테스트합니다.
        """
        for case in self.test_cases_cer:
            with self.subTest(case['description']):
                result = self.metrics.get_cer(case['reference'], case['transcription'])
                self.assertAlmostEqual(result['cer'], case['expected_cer'], places=2)

    def test_get_wer(self):
        """
        get_wer 메서드의 여러 케이스를 테스트합니다.
        """
        for case in self.test_cases_wer:
            with self.subTest(case['description']):
                result = self.metrics.get_wer(case['reference'], case['transcription'])
                self.assertAlmostEqual(result['wer'], case['expected_wer'], places=2)

    def test_get_crr(self):
        """
        get_crr 메서드의 여러 케이스를 테스트합니다.
        """
        case = {
            'reference': '또 다른 방법으로, 데이터를 읽는 작업과 쓰는 작업을 분리합니다!',
            'transcription': '또 다른 방법으로 데이터를 읽는 작업과 쓰는 작업을 분리합니다.',
            'expected_crr': 1.0,
            'description': '한글 문장 CRR 테스트'
        }
        result = self.metrics.get_crr(case['reference'], case['transcription'])
        self.assertAlmostEqual(result['crr'], case['expected_crr'], places=2)

if __name__ == '__main__':
    unittest.main()
