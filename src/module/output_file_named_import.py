import pandas as pd
from const.const import INPUT_DIR, OUTPUT_DIR


def fillna_class_named_import():
    """
    classの欠損値を埋める
    （from...importしている場合）
    """
    df = pd.read_csv(f'{INPUT_DIR}/user.csv')

    # 欠損値埋め
    df = df.fillna({'class': 0})
    df = df.astype({'class': 'int'})
    
    df.to_csv(f'{OUTPUT_DIR}/user.csv', index=False)
