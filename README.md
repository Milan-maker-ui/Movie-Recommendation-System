# 🎬 Movie Recommendation System

A machine learning-based **Movie Recommendation System** that recommends similar movies based on user ratings. The project uses the **MovieLens dataset**, collaborative filtering, and Pearson correlation to identify movies with similar rating patterns.

The project also includes an interactive **Streamlit web application** where users can select a movie and receive recommendations.

---

## 🚀 Features

* 🎬 Movie recommendation using collaborative filtering
* 📊 Exploratory Data Analysis
* ⭐ Movie rating analysis
* 👥 User–Movie rating matrix
* 🔗 Movie similarity using Pearson correlation
* 🎯 Top-N movie recommendations
* 📈 Recommendation visualization
* 🖥️ Interactive Streamlit web application
* 🧩 Modular Python project structure

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Streamlit**
* **Jupyter Notebook**

---


## 📊 Dataset

This project uses the **MovieLens 100K dataset**.

The main files used are:

* `u.data` — user movie ratings
* `Movie_Id_Titles.csv` — movie IDs and movie titles

The rating data contains:

```text
user_id
movie_id
rating
timestamp
```

---

## ⚙️ How the Recommendation System Works

The recommendation pipeline follows these steps:

```text
MovieLens Dataset
       ↓
Data Loading
       ↓
Data Preprocessing
       ↓
User–Movie Rating Matrix
       ↓
Movie Correlation
       ↓
Filter Movies by Rating Count
       ↓
Sort by Similarity
       ↓
Top-N Recommendations
```

### 1. Data Loading

The datasets are loaded using Pandas.

### 2. Data Preprocessing

Movie ratings are analyzed to calculate:

* Average movie rating
* Number of ratings per movie

### 3. User–Movie Matrix

A matrix is created where:

```text
Rows    → Users
Columns → Movies
Values  → Ratings
```

### 4. Movie Similarity

The system calculates the correlation between the selected movie and other movies.

Pearson correlation is used to identify movies with similar user-rating patterns.

### 5. Recommendation

Movies with sufficient rating data are filtered and sorted according to their correlation score.

The highest-correlated movies are returned as recommendations.

---

### Example

```text
🎬 Movie Recommendation System

Choose a Movie:
[ Star Wars (1977) ]

Number of Recommendations:
[ 10 ]

Minimum Ratings:
[ 100 ]

[ Recommend Movies ]
```

The application then displays the recommended movies and their similarity scores.

---

# ▶️ Run the Python Version

You can also run the recommendation system without Streamlit:

```bash
python main.py
```

---

# 📈 Example Workflow

For example, if the user selects:

```text
Star Wars (1977)
```

the system analyzes the rating patterns associated with that movie and returns movies with high correlation.

Example output format:

```text
Movie                                Correlation
-------------------------------------------------
Empire Strikes Back                  0.74
Return of the Jedi                   0.68
Raiders of the Lost Ark              0.64
Back to the Future                   0.61
```

*The actual recommendations depend on the dataset and correlation calculations.*

---

# 🔮 Future Improvements

The project can be extended with:

* 🎞️ Movie posters
* 🔎 Movie search/autocomplete
* ⭐ Average rating display
* 🎭 Genre-based recommendations
* 🔥 Hybrid recommendation system
* 🤖 Deep learning recommendation models
* 🌐 Movie metadata APIs
* 📱 Improved Streamlit UI
* ☁️ Cloud deployment
* 🐳 Docker support
* 🧪 Automated testing

---

## 📌 Project Highlights

This project demonstrates practical experience with:

* Machine Learning
* Recommendation Systems
* Collaborative Filtering
* Data Preprocessing
* Exploratory Data Analysis
* Python Programming
* Data Visualization
* Streamlit
* Modular Software Development

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub.
