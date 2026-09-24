import matplotlib.pyplot as plt

def plot_rating_distribution(movie_data):
    """
    Plot distribution of movie ratings.
    """
    plt.figure(figsize=(8, 5))
    movie_data["rating"].hist(bins=5, edgecolor="black")

    plt.title("Movie Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Ratings")
    plt.tight_layout()
    plt.show()

def plot_popular_movies(ratings_summary,top_n=10):
    """
    Plot the most frequently rated movies.
    """
    top_movies = (ratings_summary.sort_values("num_of_ratings", ascending=False).head(top_n))
    plt.figure(figsize=(10, 6))
    plt.barh(top_movies.index, top_movies["num_of_ratings"])
    plt.title("Top Most Rated Movies")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Movie")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
