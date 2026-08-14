# 🎬 Movie Recommendation System

A machine learning-based Movie Recommendation System built with **Python, Pandas, and Streamlit**.

The system uses **collaborative filtering** and **Pearson correlation** to identify movies with similar user-rating patterns. An interactive Streamlit web application allows users to select a movie and receive personalized movie recommendations.

---

## 🚀 Features

- 🎬 Movie recommendations based on rating patterns
- ⭐ Collaborative filtering
- 📊 Pearson correlation-based movie similarity
- 👥 User-Movie rating matrix
- 📈 Rating and popularity visualizations
- 🖥️ Interactive Streamlit web application
- 🔢 Configurable number of recommendations
- 🎯 Minimum rating threshold
- 🧩 Modular Python project structure
- 🧪 Unit tests with Pytest

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **Streamlit**
- **Pytest**
- **Jupyter Notebook**

---

## 📊 Dataset

This project uses the **MovieLens 100K dataset** provided by GroupLens.

The dataset contains:

- 100,000 movie ratings
- 1,000 users
- 1,682 movies

### Dataset files used

```text
data/
├── u.data
└── u.item
# 🎬 Movie Recommendation System

* `u.data` — Contains user ratings with:

```text
user_id
movie_id
rating
timestamp
```
* `u.item` — Contains movie information including:

```text
movie_id
title
release_date
IMDb URL
genre information
```

A machine learning-based **Movie Recommendation System** that recommends similar movies based on user ratings. The project uses the **MovieLens dataset**, collaborative filtering, and Pearson correlation to identify movies with similar rating patterns.

The project also includes an interactive **Streamlit web application** where users can select a movie and receive recommendations.


---

## ⚙️ How the Recommendation System Works

The recommendation pipeline follows these steps:

```text
MovieLens Dataset
       │
       ▼
Data Loading
       │
       ▼
Data Preprocessing
       │
       ▼
User-Movie Rating Matrix
       │
       ▼
Pearson Correlation
       │
       ▼
Movie Similarity
       │
       ▼
Filter by Minimum Ratings
       │
       ▼
Top-N Recommendations
       │
       ▼
Streamlit Application
```

### 1. Data Loading

The system loads the original:
u.data
u.item
files using Pandas.

### 2. Merge Movie Information

Ratings are combined with movie titles using movie_id.

### 3. Create User-Movie Matrix

A user-movie matrix is created:

Rows    → Users
Columns → Movies
Values  → Ratings
### 4. Calculate Similarity

Pearson correlation is calculated between the selected movie and other movies.

Movies with similar rating patterns receive higher correlation scores.

### 5. Filter Recommendations

Movies can be filtered based on the minimum number of ratings.

### 6. Generate Top-N Recommendations

The system returns the movies with the highest similarity scores.

---
## 🖥️ Streamlit Application

The project includes an interactive web application.

Run:

streamlit run app.py

The application allows users to:
```text
Select a movie
Choose the number of recommendations
Set the minimum number of ratings
Generate recommendations
View correlation scores
View a similarity chart
```
Example:
```text
🎬 Movie Recommendation System


Select a Movie:
[ Star Wars (1977) ]


Number of Recommendations:
[ 10 ]


Minimum Number of Ratings:
[ 100 ]


        [ 🎯 Recommend Movies ]
```

The application then displays the recommended movies and their similarity scores.

---
## ▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

---

## 🐍 Run Without Streamlit

You can also run the recommendation system from the terminal:

python main.py

---

🧪 Run Tests

Run the unit tests:

pytest

---

## 📈 Example Recommendation

If the user selects:

Star Wars (1977)

the system calculates correlations between Star Wars and other movies.

The application returns results in the format:

Movie                         Correlation    Ratings
----------------------------------------------------
Movie A                       0.74           200
Movie B                       0.68           180
Movie C                       0.64           150

The exact recommendations depend on the MovieLens dataset and selected filtering parameters.

---

## 🧠 Machine Learning Approach

This project uses item-based collaborative filtering.

Instead of recommending movies based on movie descriptions, genres, or keywords, the system analyzes how users have rated different movies.

For example:

Users
 │
 ├── Movie A → ⭐⭐⭐⭐⭐
 ├── Movie B → ⭐⭐⭐⭐
 └── Movie C → ⭐⭐

If many users show similar rating patterns between two movies, those movies can have a higher correlation.

---

## 📊 Visualization

The project includes visualizations such as:

Rating Distribution

Shows how frequently different rating values occur.

Most Rated Movies

Shows movies with the highest number of user ratings.

Recommendation Similarity

The Streamlit application displays correlation scores using a bar chart.

---

## 📁 Module Description
data_loader.py

Responsible for:

Loading u.data
Loading u.item
Handling dataset encoding
Merging ratings with movie titles
preprocessing.py

Responsible for:

Calculating movie statistics
Creating the user-movie matrix
recommender.py

Contains the main recommendation algorithm.

Responsible for:

Calculating Pearson correlation
Filtering movies
Sorting recommendations
Returning Top-N movies
visualization.py

Contains functions for:

Rating distribution
Popular movie visualization
utils.py

Contains reusable helper functions.

app.py

Provides the interactive Streamlit interface.

main.py

Provides a command-line version of the recommendation system.

---

## 🔮 Future Improvements

Possible improvements include:

🎞️ Movie posters
🔎 Movie search functionality
🎭 Genre-based recommendations
🧠 Hybrid recommendation system
🤖 Content-based filtering
⭐ Personalized user recommendations
🌐 Movie metadata API integration
🐳 Docker support
☁️ Cloud deployment
📱 Improved UI/UX
⚡ Recommendation performance optimization


## 📌 Project Highlights

This project demonstrates practical knowledge of:

Machine Learning
Recommendation Systems
Collaborative Filtering
Pearson Correlation
Data Preprocessing
Exploratory Data Analysis
Data Visualization
Python
Pandas
Streamlit
Modular Software Development
Unit Testing

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.


