import hashlib
from time import time
from unittest.mock import patch
import json

import pandas as pd
import requests
from mage_ai.data_preparation.shared.secrets import get_secret_value

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_characters_from_marvel_api(*args, **kwargs):
    """
    Retrieves character data from the Marvel API and returns it as a
    Pandas DataFrame.

    This function sends requests to the Marvel API with authentication
    parameters and retrieves character data in batches of 100, concatenating
    the results into a single DataFrame. The base URL for the API is
    "https://gateway.marvel.com/v1/public/characters".

    Args:
    *args: positional arguments
    **kwargs: keyword arguments

    Returns:
    pandas.DataFrame: A DataFrame containing the retrieved character data.
    The DataFrame has columns for the character name, ID, description,
    thumbnail image URL, and URLs to further information on the character.
    """
    base_url = "https://gateway.marvel.com/v1/public/characters"
    limit = 100

    offset = 0
    json_response = []

    query = get_query_with_authentication_params(**kwargs)
    query["limit"] = limit
    query["offset"] = offset

    total = requests.get(base_url, params=query).json()["data"]["total"]

    while offset < total:
        query["offset"] = offset
        response = requests.get(base_url, params=query)
        response.raise_for_status()
        results = response.json()["data"]["results"]
        json_response.extend(results)

        offset += limit

    return pd.DataFrame(json_response)


def get_query_with_authentication_params(**kwargs):
    """
    Returns a dictionary with the authentication parameters required to
    access the Marvel API.

    The dictionary contains the following keys:
    - ts: a timestamp of the current time
    - apikey: the public key associated with the Marvel account
    - hash: a hash of the timestamp, the private key, and the public key,
    generated using the MD5 algorithm

    Returns:
    dict: A dictionary containing the authentication parameters
    """
     
    marvel_credentials = json.load(open("/home/secrets/" + kwargs['marvel_credentials']))
    marvel_public_id = marvel_credentials["marvel_public_id"]
    marvel_secret_key = marvel_credentials["marvel_secret_key"]
    timestamp = int(time())
    input_string = str(timestamp) + marvel_secret_key + marvel_public_id
    hash = hashlib.md5(input_string.encode("utf-8")).hexdigest()
    return {"ts": timestamp, "apikey": marvel_public_id, "hash": hash}


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
    assert isinstance(output, pd.DataFrame)


@test
@patch("requests.get")
def test_load_characters_from_marvel_api_success(output, mock_requests, **kwargs):
    # Mock a successful API response
    mock_response = {
        "data": {
            "total": 1,
            "results": [
                {
                    "id": 1,
                    "name": "Spider-Man",
                    "description": "A radioactive spider-bite gave Peter Parker superhuman strength and spider-like abilities.",
                    "thumbnail": {"path": "http://example.com/image", "extension": "jpg"},
                    "urls": [
                        {"type": "wiki", "url": "http://example.com/wiki"},
                        {"type": "comiclink", "url": "http://example.com/comics"},
                    ],
                }
            ],
        }
    }
    mock_requests.return_value.json.return_value = mock_response

    # Call the function and check the result
    result = load_characters_from_marvel_api(**kwargs)
    assert isinstance(result, pd.DataFrame)
    assert result.iloc[0]["name"] == "Spider-Man"
    assert result.iloc[0]["id"] == 1
    assert (
        result.iloc[0]["description"]
        == "A radioactive spider-bite gave Peter Parker superhuman strength and spider-like abilities."
    )
    assert result.iloc[0]["thumbnail"] == {"path": "http://example.com/image", "extension": "jpg"}
    assert result.iloc[0]["urls"][0] == {"type": "wiki", "url": "http://example.com/wiki"}
    assert result.iloc[0]["urls"][1] == {"type": "comiclink", "url": "http://example.com/comics"}
