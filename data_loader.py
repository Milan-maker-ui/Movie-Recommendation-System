import pandas as pd

def load_data(ratings_path, movies_path):
    """
    Load the original MovieLens 100K dataset.

    Parameters
    ----------
    ratings_path : str
        Path to u.data

    movies_path : str
        Path to u.item

    Returns
    -------
    ratings : pandas.DataFrame
        User ratings.

    movies : pandas.DataFrame
        Movie information.
    """

    # Load u.data
    ratings = pd.read_csv(
        ratings_path,
        sep="\t",
        names=[
            "user_id",
            "movie_id",
            "rating",
            "timestamp"
        ],
        encoding="latin-1"
    )

    # Load u.item
    movie_columns = [
        "movie_id",
        "title",
        "release_date",
        "video_release_date",
        "imdb_url",
        "unknown",
        "action",
        "adventure",
        "animation",
        "children",
        "comedy",
        "crime",
        "documentary",
        "drama",
        "fantasy",
        "film_noir",
        "horror",
        "musical",
        "mystery",
        "romance",
        "sci_fi",
        "thriller",
        "war",
        "western"
    ]

    movies = pd.read_csv(movies_path, sep="|", names=movie_columns, encoding="latin-1")
    return ratings, movies

def merge_data(ratings, movies):
    """
    Merge ratings with movie information.
    """

    movie_data = pd.merge(ratings, movies[["movie_id", "title"]], on="movie_id", how="inner")
    return movie_data