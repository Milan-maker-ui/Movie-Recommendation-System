import pandas as pd


def movie_statistics(movie_data):
    """
    Calculate average movie ratings
    and number of ratings.
    """

    ratings_summary = pd.DataFrame(movie_data.groupby("title")["rating"].mean())

    ratings_summary["num_of_ratings"] = (movie_data.groupby("title")["rating"].count())
    return ratings_summary


def create_user_movie_matrix(movie_data):
    """
    Create User-Movie rating matrix.

    Rows    -> Users
    Columns -> Movies
    Values  -> Ratings
    """

    movie_matrix = movie_data.pivot_table(
        index="user_id",
        columns="title",
        values="rating"
    )

    return movie_matrix