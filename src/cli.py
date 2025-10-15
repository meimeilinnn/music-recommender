# src/cli.py
"""命令列介面"""

import click
from src.data import load_toy_songs
from src.recommend.content_based import recommend_similar


@click.group()
def cli():
    """音樂推薦系統 CLI"""
    pass


@cli.command()
@click.option('--seed', type=int, required=True, help='種子歌曲的 track_id')
@click.option('--k', type=int, default=5, help='推薦歌曲數量')
def demo(seed, k):
    """
    執行推薦 demo
    
    範例: python -m src.cli demo --seed 1 --k 5
    """
    # 載入資料
    click.echo("🔄 Loading songs...")
    songs = load_toy_songs()
    
    # 檢查種子歌曲是否存在
    if seed not in songs['track_id'].values:
        click.echo(f"❌ Error: Song with ID {seed} not found!")
        click.echo(f"Available IDs: {songs['track_id'].tolist()}")
        return
    
    # 取得種子歌曲資訊
    seed_song = songs[songs['track_id'] == seed].iloc[0]
    
    # 執行推薦
    click.echo("🎯 Generating recommendations...")
    recommendations = recommend_similar(songs, seed_id=seed, k=k)
    
    # 顯示結果
    click.echo(f"\n🎵 Seed Song: {seed_song['track_name']} - {seed_song['artist']}")
    click.echo(f"\n📋 Top {k} Similar Songs:\n")
    
    for idx, row in enumerate(recommendations.itertuples(), 1):
        click.echo(f"{idx}. {row.track_name} - {row.artist} (similarity: {row.similarity:.2f})")
    
    click.echo("\n✨ Recommendation complete!\n")


if __name__ == '__main__':
    cli()