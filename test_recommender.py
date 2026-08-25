import pandas as pd
from src.recommender import MovieRecommender


def test_recommender_returns_results():
    movie_matrix = pd.DataFrame(
        {
            "Movie A": [5, 4, 5, 4, 5],
            "Movie B": [5, 4, 5, 4, 5],
            "Movie C": [1, 2, 1, 2, 1]
        }
    )

    ratings = pd.DataFrame(
        {"num_of_ratings": [200, 200, 200]},
        index=["Movie A", "Movie B", "Movie C"]
    )

    recommender = MovieRecommender(movie_matrix, ratings)
    result = recommender.recommend("Movie A", min_ratings=100, top_n=2)

    assert result is not None
    assert len(result) <= 2


def test_movie_not_found():
    movie_matrix = pd.DataFrame({"Movie A": [5, 4, 5],"Movie B": [4, 5, 4]})

    ratings = pd.DataFrame(
        {"num_of_ratings": [100, 100]},
        index=["Movie A", "Movie B"]
    )

    recommender = MovieRecommender(movie_matrix, ratings)
    result = recommender.recommend("Unknown Movie")
    assert result is None