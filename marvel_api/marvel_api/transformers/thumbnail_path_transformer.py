from typing import Any, Optional

import pandas as pd
from pandas import DataFrame

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def process_thumbnail_data(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Adds a new column to the input DataFrame that contains the full path to the thumbnail image for each row.

    Args:
        df: The input DataFrame.
        *args: Optional additional arguments.
        **kwargs: Optional additional keyword arguments.

    Returns:
        A new DataFrame with an additional column that contains the full path to the thumbnail image for each row.
    """
    df["thumbnail"] = df.apply(join_path_extension, axis=1)
    return df


def join_path_extension(row: pd.Series) -> Optional[str]:
    """
    Combines the 'path' and 'extension' columns of the 'thumbnail' column in a row of a DataFrame.

    Args:
        row: A pandas Series representing a row of a DataFrame.

    Returns:
        A string that contains the full path to the thumbnail image for the row, or None if either the path or extension is missing.
    """
    if "thumbnail" in row and "path" in row["thumbnail"] and "extension" in row["thumbnail"]:
        return row["thumbnail"]["path"] + "." + row["thumbnail"]["extension"]
    else:
        return None


@test
def test_output(output, *args) -> None:
    """
    Tests that the output of the transformer function matches the expected output.

    Args:
        output: The actual output of the transformer function.
        expected_output: The expected output of the transformer function.
    """
    assert output is not None, "The output is undefined"
    assert isinstance(output, pd.DataFrame)


@test
def test_process_thumbnail_data(output: Any) -> None:
    """
    Tests the process_thumbnail_data function.

    Args:
        output: A pytest fixture that sets up the test environment.
    """
    input_data = pd.DataFrame(
        {
            "thumbnail": [
                {"path": "path1", "extension": "ext1"},
                {"path": "path2", "extension": "ext2"},
                {"path": "path3", "extension": "ext3"},
            ]
        }
    )

    expected_output = pd.DataFrame({"thumbnail": ["path1.ext1", "path2.ext2", "path3.ext3"]})

    # Ensure that the function produces the expected output
    output = process_thumbnail_data(input_data)

    assert output.equals(expected_output)

    # Ensure that the function handles unexpected input values correctly
    input_data = pd.DataFrame({"thumbnail": [{}]})
    expected_output = pd.DataFrame({"thumbnail": [None]})
    output = process_thumbnail_data(input_data)
    assert output.equals(expected_output)
