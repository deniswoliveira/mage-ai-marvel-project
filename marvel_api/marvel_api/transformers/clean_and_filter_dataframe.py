import pandas as pd
from pandas import DataFrame

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def clean_and_filter_dataframe(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Removes unwanted columns from a DataFrame and cleans the 'description' column by removing apostrophes.

    Args:
        df: The input DataFrame.
        *args: Optional additional arguments.
        **kwargs: Optional additional keyword arguments.

    Returns:
        A new DataFrame with unwanted columns removed and a cleaned 'description' column.
    """
    # List of columns to keep
    keep_cols = ["id", "name", "description", "modified", "thumbnail", "resourceURI"]

    # Drop unwanted columns
    df = df[keep_cols]

    # Clean single quotes column
    df = df.replace(to_replace=r"'", value="", regex=True)

    return df


def generate_input_data() -> pd.DataFrame:
    data = {
        "id": [1, 2, 3],
        "name": ["Spider-Man", "Iron Man", "Captain America"],
        "description": [
            "A high school student named Peter Parker who gains spider-like abilities after being bitten by a radioactive spider.",
            "A wealthy industrialist and ingenious engineer who creates a powered suit of armor to save the world.",
            "A frail, sickly young man who was enhanced to the peak of human perfection by an experimental serum in order to aid the United States' war effort.",
        ],
        "modified": [
            pd.Timestamp("2022-04-10 13:27:00"),
            pd.Timestamp("2022-04-11 10:01:00"),
            pd.Timestamp("2022-04-12 15:43:00"),
        ],
        "thumbnail": ["path1.ext1", "path2.ext2", "path3.ext3"],
        "resourceURI": [
            "http://gateway.marvel.com/v1/public/characters/1011334",
            "http://gateway.marvel.com/v1/public/characters/1009368",
            "http://gateway.marvel.com/v1/public/characters/1009220",
        ],
        "comics": [
            {"id": 1, "name": "comic1"},
            {"id": 2, "name": "comic2"},
            {"id": 3, "name": "comic3"},
        ],
        "series": [
            {"id": 1, "name": "series1"},
            {"id": 2, "name": "series2"},
            {"id": 3, "name": "series3"},
        ],
        "stories": [
            {"id": 1, "name": "story1"},
            {"id": 2, "name": "story2"},
            {"id": 3, "name": "story3"},
        ],
        "events": [
            {"id": 1, "name": "event1"},
            {"id": 2, "name": "event2"},
            {"id": 3, "name": "event3"},
        ],
        "urls": [
            {
                "type": "detail",
                "url": "http://marvel.com/characters/54/spider-man?utm_campaign=apiRef&utm_source=41476e3f62b3ce3a23fa124d45c6fede",
            },
            {
                "type": "wiki",
                "url": "http://marvel.com/universe/Spider-Man_(Peter_Parker)?utm_campaign=apiRef&utm_source=41476e3f62b3ce3a23fa124d45c6fede",
            },
            {
                "type": "comiclink",
                "url": "http://marvel.com/comics/characters/1011334/spider-man?utm_campaign=apiRef&utm_source=41476e3f62b3ce3a23fa124d45c6fede",
            },
        ],
    }

    return pd.DataFrame(data)


def generate_expected_output() -> pd.DataFrame:
    """
    Generates expected output for the test_remove_columns function.

    Returns:
        A pandas DataFrame containing the columns described above, with the exception of the columns
        'comics', 'series', 'stories', 'events', and 'urls'.
    """
    data = {
        "id": [1, 2, 3],
        "name": ["Spider-Man", "Iron Man", "Captain America"],
        "description": [
            "A high school student named Peter Parker who gains spider-like abilities after being bitten by a radioactive spider.",
            "A wealthy industrialist and ingenious engineer who creates a powered suit of armor to save the world.",
            "A frail, sickly young man who was enhanced to the peak of human perfection by an experimental serum in order to aid the United States war effort.",
        ],
        "modified": [
            pd.Timestamp("2022-04-10 13:27:00"),
            pd.Timestamp("2022-04-11 10:01:00"),
            pd.Timestamp("2022-04-12 15:43:00"),
        ],
        "thumbnail": ["path1.ext1", "path2.ext2", "path3.ext3"],
        "resourceURI": [
            "http://gateway.marvel.com/v1/public/characters/1011334",
            "http://gateway.marvel.com/v1/public/characters/1009368",
            "http://gateway.marvel.com/v1/public/characters/1009220",
        ],
    }
    return pd.DataFrame(data)


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
    assert isinstance(output, pd.DataFrame)


@test
def test_clean_and_filter_dataframe(*args) -> None:
    # Generate input data
    input_data = generate_input_data()

    # Generate expected output
    expected_output = generate_expected_output()

    # Call function to get actual output
    actual_output = clean_and_filter_dataframe(input_data)

    # Check that the actual output matches the expected output
    assert actual_output.equals(expected_output), "Output does not match expected output"

    # Check that the actual output has the correct columns
    expected_columns = ["id", "name", "description", "modified", "thumbnail", "resourceURI"]
    assert all(
        column in actual_output.columns for column in expected_columns
    ), f"Columns do not match expected columns: {actual_output.columns}"
