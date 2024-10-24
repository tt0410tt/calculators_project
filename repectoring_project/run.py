# run.py

from test_pack import test_class

def main():
    tester = test_class()

    # 긴 케이스에 대한 CER 테스트 실행
    print("긴 케이스에 대한 CER 테스트를 실행합니다...\n")
    tester.test_long_cer_case(
        refs=tester.long_case['refs'],
        refs_v=tester.long_case['refs_v'],
        refs_c=tester.long_case['refs_c'],
        preds_vrew=tester.long_case['preds_vrew'],
        preds_transcribe=tester.long_case['preds_transcribe'],
        preds_clova=tester.long_case['preds_clova']
    )

    # 짧은 케이스에 대한 오류율 테스트 실행
    print("\n짧은 케이스에 대한 오류율 테스트를 실행합니다...\n")
    for case in tester.shorts_case:
        name = case['name']
        refs = case['refs']
        preds = case['preds']
        metric = ''
        if 'cer' in name:
            metric = 'cer'
        elif 'wer' in name:
            metric = 'wer'
        elif 'crr' in name:
            metric = 'crr'
        else:
            print(f"알 수 없는 테스트 케이스: {name}")
            continue

        print(f"{name} 실행 중...")
        tester.test_shorts_er_case(refs, preds, metric)

if __name__ == '__main__':
    main()
