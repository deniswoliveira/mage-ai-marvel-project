from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: DataFrame, **kwargs) -> None:
    """
    Exports a DataFrame to an S3 bucket using the credentials and settings
    specified in the 'default' profile of the io_config.yaml file in the
    repository. The exported DataFrame will be stored in the specified S3
    bucket as an object with the given object key.

    Args:
        df (pandas.DataFrame): The DataFrame to export to S3.
        **kwargs: Additional arguments that specify the bucket name and object
            key to store the DataFrame as.

    Returns:
        None
    """    
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    marvel_credentials = json.load(open("/home/secrets/" + kwargs['s3_marvel_api_conf']))
    bucket_name = marvel_credentials['bucket_name']
    object_key = marvel_credentials['object_key']

    S3.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
    )
