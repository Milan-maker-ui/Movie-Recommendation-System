import streamlit as st
from src.data_loader import load_data, merge_data
from src.preprocessing import movie_statistics,create_user_movie_matrix
from src.recommender import MovieRecommender

# Page Configuration

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Load and Prepare Data

@st.cache_data
def load_movie_system():

    ratings, movies = load_data("data/u.data", "data/u.item")
    movie_data = merge_data(ratings, movies)
    ratings_summary = movie_statistics(movie_data)
    movie_matrix = create_user_movie_matrix(movie_data)
    recommender = MovieRecommender(movie_matrix, ratings_summary)
    movie_list = sorted(movie_matrix.columns.tolist())

    return recommender, movie_list

# Load System

try:

    recommender, movie_list = load_movie_system()

except FileNotFoundError:

    st.error(
        """
        Dataset files were not found.

        Please make sure these files exist:
        data/u.data
        data/u.item
        """
    )

    st.stop()

# Application UI

st.title("🎬 Movie Recommendation System")

st.markdown(
    """
    ### Discover movies you may like

    Select a movie below and the system will recommend
    similar movies based on user rating patterns.
    """
)


st.divider()

# Sidebar

st.sidebar.header("⚙️ Recommendation Settings")

selected_movie = st.sidebar.selectbox("Select a Movie", movie_list)
top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=5,
    max_value=20,
    value=10
)

min_ratings = st.sidebar.slider(
    "Minimum Number of Ratings",
    min_value=20,
    max_value=300,
    value=100
)

# Recommendation Button

if st.button("🎯 Recommend Movies", type="primary"):

    recommendations = recommender.recommend(
        movie_name=selected_movie,
        min_ratings=min_ratings,
        top_n=top_n
    )

    if recommendations is None or recommendations.empty:
        st.warning(
            "No recommendations were found. "
            "Try reducing the minimum number of ratings."
        )

    else:
        st.success(f"Recommendations for **{selected_movie}**")
        st.subheader("🍿 Recommended Movies")
        display_data = recommendations.reset_index()
        display_data.columns = [
            "Movie",
            "Correlation",
            "Number of Ratings"
        ]

        display_data["Correlation"] = (display_data["Correlation"].round(3))
        st.dataframe(display_data, use_container_width=True, hide_index=True)
        st.subheader("📊 Movie Similarity")
        chart_data = display_data.set_index("Movie")["Correlation"]

        st.bar_chart(chart_data)

# Information Section

st.divider()
st.subheader("ℹ️ About the Project")
st.write(
    """
    This Movie Recommendation System uses collaborative
    filtering to identify movies with similar user-rating
    patterns.

    Pearson correlation is used to calculate the similarity
    between movies.
    """
)

st.subheader("🛠️ Technologies")
st.write(
    """
    Python • Pandas • NumPy • Scikit-learn •
    Matplotlib • Streamlit
    """
)