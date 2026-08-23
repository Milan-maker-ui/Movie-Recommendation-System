import os

def create_directory(directory):
    """
    Create a directory if it doesn't exist.
    """
    os.makedirs(directory, exist_ok=True)


def save_dataframe(dataframe, file_path):
    """
    Save a DataFrame as a CSV file.
    """
    directory = os.path.dirname(file_path)
    if directory:
        create_directory(directory)

    dataframe.to_csv(file_path, index=True)