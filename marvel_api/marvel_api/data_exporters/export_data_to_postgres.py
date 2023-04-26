from os import path

from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Exports a DataFrame to a Postgres database.

    Args:
        df (pandas.DataFrame): The DataFrame to export.
        **kwargs: Additional arguments that specify the schema name and table name to export data to.

    Returns:
        None
    """
    schema_name = kwargs["schema_name"]
    table_name = kwargs["table_name"]
    config_path = path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,
            if_exists="replace",
        )
