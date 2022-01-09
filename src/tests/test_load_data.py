
import pandas as pd
import os

TEST_DATA_DIR = 'src/tests/test_data'


def test_CSVデータ読み込みサンプル_出力ファイルと期待ファイルが一致する():
    path = f'{TEST_DATA_DIR}/user.csv'
    df = pd.read_csv(path)

    # テストしたい関数実行→CSV出力
    output_path = f'{TEST_DATA_DIR}/user_output.csv'
    df.to_csv(output_path, index=False)

    # 出力を読み込む
    df_output = pd.read_csv(output_path)

    # 差分を見る
    success_path = f'{TEST_DATA_DIR}/success_user.csv'
    df_success = pd.read_csv(success_path)
    assert df_output.equals(df_success)

    # 後処理で出力データを消す
    os.remove(output_path)
