
import pandas as pd
import const.const


def fillna_class():
    """
    classの欠損値を埋める
    """
    df = pd.read_csv(f'{const.const.INPUT_DIR}/user.csv')

    # 欠損値埋め
    df = df.fillna({'class': 0})
    df = df.astype({'class': 'int'})
    
    df.to_csv(f'{const.const.OUTPUT_DIR}/user.csv', index=False)
    
