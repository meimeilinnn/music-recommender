# 🎵 Music Recommendation System

A content-based music recommendation system that suggests similar songs based on audio features using machine learning algorithms.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Overview

This project implements a **content-based filtering** recommendation system that analyzes audio features (danceability, energy, valence, tempo, acousticness) to find similar songs. Using cosine similarity and feature normalization, the system can recommend songs that match the mood and characteristics of a seed song.

## ✨ Features

- **Content-Based Filtering**: Recommends songs based on audio feature similarity
- **Machine Learning**: Uses scikit-learn's cosine similarity and StandardScaler
- **CLI Interface**: Easy-to-use command-line interface built with Click
- **Modular Architecture**: Clean separation of concerns (data, algorithms, CLI)
- **Extensible Design**: Easy to add new recommendation algorithms

## 🚀 Demo

### Example 1: Happy, Upbeat Songs
```bash
$ python -m src.cli demo --seed 1 --k 5

🎵 Seed Song: Happy - Pharrell Williams

📋 Top 5 Similar Songs:

1. Treasure - Bruno Mars (similarity: 0.78)
2. Get Lucky - Daft Punk (similarity: 0.75)
3. Uptown Funk - Mark Ronson ft. Bruno Mars (similarity: 0.73)
4. Can't Stop The Feeling - Justin Timberlake (similarity: 0.69)
5. 24K Magic - Bruno Mars (similarity: 0.55)

✨ Recommendation complete!
```

### Example 2: Emotional Ballads
```bash
$ python -m src.cli demo --seed 7 --k 3

🎵 Seed Song: Shallow - Lady Gaga & Bradley Cooper

📋 Top 3 Similar Songs:

1. Stay With Me - Sam Smith (similarity: 0.92)
2. Someone Like You - Adele (similarity: 0.85)
3. All of Me - John Legend (similarity: 0.74)

✨ Recommendation complete!
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/meimeilinnn/music-recommender.git
cd music-recommender
```

2. **Create a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Command
```bash
python -m src.cli demo --seed <SONG_ID> --k <NUMBER_OF_RECOMMENDATIONS>
```

### Parameters
- `--seed`: The track ID of the seed song (required)
- `--k`: Number of recommendations to generate (default: 5)

### Available Songs
The current demo includes 10 songs (IDs 1-10):
- **Upbeat/Happy**: Happy (1), Uptown Funk (2), Can't Stop The Feeling (3), Get Lucky (4), 24K Magic (5), Treasure (6)
- **Emotional/Ballads**: Shallow (7), Someone Like You (8), All of Me (9), Stay With Me (10)

### Examples
```bash
# Get 5 similar songs to "Happy"
python -m src.cli demo --seed 1 --k 5

# Get 3 similar songs to "Shallow"
python -m src.cli demo --seed 7 --k 3

# Get 10 recommendations
python -m src.cli demo --seed 2 --k 10
```

## 📊 How It Works

### 1. Feature Extraction
The system analyzes five key audio features:
- **Danceability** (0.0-1.0): How suitable a track is for dancing
- **Energy** (0.0-1.0): Intensity and activity level
- **Valence** (0.0-1.0): Musical positiveness (happy vs sad)
- **Tempo** (BPM): Speed of the track
- **Acousticness** (0.0-1.0): Confidence that the track is acoustic

### 2. Feature Normalization
Using `StandardScaler` from scikit-learn to normalize features to the same scale, ensuring fair comparison across different feature ranges.

### 3. Similarity Calculation
Cosine similarity measures the angle between feature vectors:
```
similarity = cos(θ) = (A · B) / (||A|| × ||B||)
```
Higher values (closer to 1.0) indicate more similar songs.

### 4. Ranking & Recommendation
Songs are ranked by similarity score and the top K results are returned.

## 🏗️ Project Structure
```
music-recommender/
├── src/
│   ├── __init__.py
│   ├── cli.py                    # Command-line interface
│   ├── data.py                   # Data loading and processing
│   └── recommend/
│       ├── __init__.py
│       └── content_based.py      # Content-based filtering algorithm
├── data/
│   ├── raw/
│   │   └── toy_songs.csv         # Sample dataset (10 songs)
│   └── processed/                # Processed data (future use)
├── scripts/                      # Utility scripts
├── notebooks/                    # Jupyter notebooks for exploration
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🧰 Tech Stack

- **Language**: Python 3.8+
- **Data Processing**: pandas, NumPy
- **Machine Learning**: scikit-learn (cosine_similarity, StandardScaler)
- **CLI Framework**: Click
- **Version Control**: Git & GitHub
- **Data Source**: Kaggle (future integration)

## 🔮 Future Enhancements

- [ ] **Real Dataset Integration**: Download and integrate Spotify's audio features dataset via Kaggle API
- [ ] **Collaborative Filtering**: Implement user-based and item-based collaborative filtering
- [ ] **Hybrid Model**: Combine content-based and collaborative filtering
- [ ] **Web Interface**: Build a Flask/FastAPI web app with interactive UI
- [ ] **Playlist Generation**: Create full playlists based on mood or theme
- [ ] **User Ratings**: Allow users to rate recommendations for continuous improvement
- [ ] **Advanced Features**: Add genre, artist similarity, and temporal features
- [ ] **Deployment**: Deploy to cloud platforms (Heroku, AWS, or Google Cloud)
- [ ] **API Endpoint**: Create RESTful API for integration with other apps

## 📚 What I Learned

Through building this project, I gained hands-on experience with:

- **Machine Learning**: Content-based recommendation algorithms, feature engineering, similarity metrics
- **Python Best Practices**: Modular design, type hints, docstrings, PEP 8 style guide
- **Data Science Tools**: pandas for data manipulation, scikit-learn for ML pipelines
- **Software Engineering**: CLI design, error handling, code organization, version control
- **Development Workflow**: Virtual environments, dependency management, Git workflow
- **Documentation**: Writing clear README, code comments, and user guides

## 🎓 Technical Concepts

### Content-Based Filtering
Recommends items similar to those a user liked in the past, based on item features rather than user behavior.

**Advantages**:
- No cold-start problem for new users
- Can recommend niche items
- Transparent recommendations (explainable)

**Limitations**:
- Limited diversity (tends to recommend similar items)
- Requires good feature engineering
- Cannot learn from user community

### Cosine Similarity
Measures similarity between two vectors by calculating the cosine of the angle between them.
```python
from sklearn.metrics.pairwise import cosine_similarity

# Example
features = [[0.8, 0.9, 0.7], [0.75, 0.85, 0.68]]
similarity = cosine_similarity(features)
# Output: similarity score between 0 and 1
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Mei-Ting Lin**

- GitHub: [@meimeilinnn](https://github.com/meimeilinnn)
- LinkedIn: [Mei-Ting Lin](https://www.linkedin.com/in/mei-ting-lin/)
- Email: [meimeilinnn@gmail.com](mailto:meimeilinnn@gmail.com)
## 🙏 Acknowledgments

- Spotify for inspiring music recommendation systems
- Kaggle for providing access to music datasets
- scikit-learn community for excellent ML tools
- Click framework for making CLI development easy

## 📞 Contact

If you have any questions or suggestions, feel free to:
- Open an issue on GitHub
- Contact me via email
- Connect with me on LinkedIn

---

⭐ If you found this project helpful, please consider giving it a star!

Made with ❤️ and Python



