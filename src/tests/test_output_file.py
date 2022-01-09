from module.output_file import fillna_class
from module.output_file_named_import import fillna_class_named_import
import const.const
import pandas as pd
import os


TEST_DATA_DIR = 'src/tests/test_data'


def test_fillna_class_出力ファイルが期待されているものと一致する(monkeypatch):

    # モック
    monkeypatch.setattr(const.const, 'INPUT_DIR', f'{TEST_DATA_DIR}/input')
    monkeypatch.setattr(const.const, 'OUTPUT_DIR', f'{TEST_DATA_DIR}/output')

    # テスト実行
    fillna_class()

    # 検証
    output = pd.read_csv(f'{TEST_DATA_DIR}/output/user.csv')
    expected = pd.read_csv(f'{TEST_DATA_DIR}/expected/user.csv')

    assert output.equals(expected)

    # 後処理で出力データを消す
    os.remove(f'{TEST_DATA_DIR}/output/user.csv')


def test_fillna_class_出力ファイルが期待されているものと一致する_名前付きimportを使用した場合(monkeypatch):

    # モック
    monkeypatch.setattr('module.output_file_named_import.INPUT_DIR', f'{TEST_DATA_DIR}/input')
    monkeypatch.setattr('module.output_file_named_import.OUTPUT_DIR', f'{TEST_DATA_DIR}/output')

    # テスト実行
    fillna_class_named_import()

    # 検証
    output = pd.read_csv(f'{TEST_DATA_DIR}/output/user.csv')
    expected = pd.read_csv(f'{TEST_DATA_DIR}/expected/user.csv')

    assert output.equals(expected)

    # 後処理で出力データを消す
    os.remove(f'{TEST_DATA_DIR}/output/user.csv')
