# run.py

from nlptutti import ASRMetrics

def main():
    metrics = ASRMetrics()

    print("음성 인식 오류율 계산 프로그램입니다.")
    reference = input("참조 문장을 입력하세요: ")
    transcription = input("변환된 문장을 입력하세요: ")

    cer_result = metrics.get_cer(reference, transcription)
    wer_result = metrics.get_wer(reference, transcription)
    crr_result = metrics.get_crr(reference, transcription)

    print("\n[결과]")
    print(f"CER (문자 오류율): {cer_result['cer'] * 100:.2f}%")
    print(f" - 대체 횟수: {cer_result['substitutions']}")
    print(f" - 삭제 횟수: {cer_result['deletions']}")
    print(f" - 삽입 횟수: {cer_result['insertions']}")

    print(f"\nWER (단어 오류율): {wer_result['wer'] * 100:.2f}%")
    print(f" - 대체 횟수: {wer_result['substitutions']}")
    print(f" - 삭제 횟수: {wer_result['deletions']}")
    print(f" - 삽입 횟수: {wer_result['insertions']}")

    print(f"\nCRR (문자 인식률): {crr_result['crr'] * 100:.2f}%")
    print(f" - 정확하게 인식한 문자 수: {crr_result['correct_chars']}/{crr_result['total_chars']}")

if __name__ == '__main__':
    main()
