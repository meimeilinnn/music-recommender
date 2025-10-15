# src/data.py
"""資料載入與處理模組"""

import pandas as pd
from pathlib import Path

def load_toy_songs():
    """
    載入測試用的歌曲資料
    
    Returns:
        pd.DataFrame: 包含歌曲資訊和音訊特徵的 DataFrame
    """
    # 找到專案根目錄
    project_root = Path(__file__).parent.parent
    csv_path = project_root / "data" / "raw" / "toy_songs.csv"
    
    # 讀取 CSV
    songs = pd.read_csv(csv_path)
    
    return songs


def get_audio_features(df):
    """
    提取音訊特徵欄位
    
    Args:
        df: 歌曲 DataFrame
        
    Returns:
        pd.DataFrame: 只包含音訊特徵的 DataFrame
    """
    feature_columns = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']
    return df[feature_columns]