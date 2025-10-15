# src/recommend/content_based.py
"""基於內容的推薦演算法"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


def recommend_similar(songs_df, seed_id, k=5):
    """
    根據種子歌曲推薦相似的歌曲
    
    Args:
        songs_df: 歌曲 DataFrame
        seed_id: 種子歌曲的 track_id
        k: 要推薦的歌曲數量
        
    Returns:
        pd.DataFrame: 推薦的歌曲,包含相似度分數
    """
    # 提取音訊特徵
    feature_columns = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']
    features = songs_df[feature_columns].values
    
    # 標準化特徵 (讓不同尺度的特徵可比較)
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # 計算所有歌曲之間的相似度
    similarity_matrix = cosine_similarity(features_scaled)
    
    # 找到種子歌曲的索引
    seed_idx = songs_df[songs_df['track_id'] == seed_id].index[0]
    
    # 取得種子歌曲與其他所有歌曲的相似度
    similarities = similarity_matrix[seed_idx]
    
    # 排序 (相似度由高到低)
    similar_indices = similarities.argsort()[::-1]
    
    # 排除種子歌曲本身,取前 k 個
    similar_indices = similar_indices[1:k+1]
    
    # 建立推薦結果
    recommendations = songs_df.iloc[similar_indices].copy()
    recommendations['similarity'] = similarities[similar_indices]
    
    return recommendations