from src.data_loader import load_data, merge_data
from src.preprocessing import (
    movie_statistics,
    create_user_movie_matrix
)
from src.recommender import MovieRecommender
from src.visualization import (
    plot_rating_distribution,
    plot_popular_movies
)


def main():

    print("=" * 60)
    print("MOVIE RECOMMENDATION SYSTEM")
    print("=" * 60)

    # Load Dataset

    print("\nLoading dataset...")

    ratings, movies = load_data("data/u.data","data/Movie_Id_Titles.csv")

    print(f"Ratings loaded: {len(ratings)}")

    print(f"Movies loaded: {len(movies)}")

    # Merge Data

    print("\nPreparing movie data...")

    movie_data = merge_data(ratings, movies)

    # Movie Statistics

    ratings_summary = movie_statistics(movie_data)

    # Visualization

    print("\nGenerating visualizations...")

    plot_rating_distribution(movie_data)

    plot_popular_movies(ratings_summary)

    # User-Movie Matrix

    print("\nCreating User-Movie matrix...")

    movie_matrix = create_user_movie_matrix(movie_data)

    print( f"Matrix shape: {movie_matrix.shape}")

    # Recommendation System

    recommender = MovieRecommender(movie_matrix, ratings_summary)

    # Example Recommendation

    movie_name = "Star Wars (1977)"

    print(f"\nGenerating recommendations for: "f"{movie_name}")

    recommendations = recommender.recommend(
        movie_name=movie_name,
        min_ratings=100,
        top_n=10
    )

    if recommendations is not None:

        print("\nTop Recommendations:")
        print("-" * 60)

        print(recommendations.to_string())

    else:

        print(f"\nMovie '{movie_name}' was not found.")

    print("\n" + "=" * 60)
    print("PROCESS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()