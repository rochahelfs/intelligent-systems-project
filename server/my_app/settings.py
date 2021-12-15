"""Settings file for env variables.
"""

from pydantic import BaseSettings


class Environment(BaseSettings):
    model_path: str
    test_products_path: str


environment = Environment(_env_file=".env")
