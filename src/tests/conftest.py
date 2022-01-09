import pytest
import os


@pytest.fixture()
def setup():
    """
    前処理でtest_data/outputフォルダを作成し、後処理で削除する
    """
    # 前処理　
    os.makedirs('src/tests/test_data/output', exist_ok=True)

    # テスト実行
    yield setup

    # 後処理
    os.removedirs('src/tests/test_data/output')
