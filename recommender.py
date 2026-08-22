import pandas as pd


class MovieRecommender:

    def __init__(self, movie_matrix, ratings):
        """
        Initialize the recommendation system.
        """
        self.movie_matrix = movie_matrix
        self.ratings = ratings

    def recommend(self, movie_name, min_ratings=100, top_n=10):
        """
        Recommend movies similar to the selected movie.

        Parameters
        ----------
        movie_name : str
            Movie selected by the user.

        min_ratings : int
            Minimum number of ratings required.

        top_n : int
            Number of recommendations.

        Returns
        -------
        pandas.DataFrame
            Recommended movies with correlation scores.
        """

        # Check whether movie exists
        if movie_name not in self.movie_matrix.columns:

            return None

        # Ratings for selected movie
        movie_ratings = (self.movie_matrix[movie_name])

        # Calculate correlation
        similar_movies = (self.movie_matrix.corrwith(movie_ratings))

        # Convert to DataFrame
        correlation_df = pd.DataFrame(similar_movies, columns=["Correlation"])

        # Remove missing correlations
        correlation_df.dropna(inplace=True)

        # Add number of ratings
        correlation_df = correlation_df.join(self.ratings["num_of_ratings"])

        # Filter movies
        correlation_df = correlation_df[correlation_df["num_of_ratings"] >= min_ratings]


        # Sort by similarity
        recommendations = (correlation_df.sort_values("Correlation", ascending=False))

        # Remove selected movie
        recommendations = (recommendations.drop(movie_name, errors="ignore"))

        # Return Top-N
        return recommendations.head(top_n)