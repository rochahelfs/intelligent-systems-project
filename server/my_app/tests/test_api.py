"""Definition of tests for the api app.
"""

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from my_app.api import api
from my_app.settings import environment
from my_app.schemas import Predictions, ListOfProducts


client = TestClient(api)


@pytest.fixture
def load_products():
    return ListOfProducts.parse_file(environment.test_products_path)


def test_list_of_products_to_dataframe_is_dataframe(load_products: ListOfProducts):
    product_df = load_products.to_dataframe()
    assert isinstance(product_df, pd.DataFrame)


def test_list_of_products_to_dataframe_has_desired_columns(load_products: ListOfProducts):
    product_df = load_products.to_dataframe()
    assert "title" in product_df.columns
    assert "concatenated_tags" in product_df.columns


def test_list_of_products_to_dataframe_has_right_shape(load_products: ListOfProducts):
    product_df = load_products.to_dataframe()
    assert product_df.shape[0] == len(load_products.products)
    assert product_df.shape[1] == 2


def test_api_predict(load_products: ListOfProducts):
    response = client.post("/v0/predict", json=load_products.dict())
    predictions = Predictions.parse_obj(response.json())
    assert response.status_code == 200
    assert len(predictions.categories) == len(load_products.products)


@pytest.mark.parametrize(
    "bad_data",
    [
        pytest.param({},
                     id="Empty data"),
    ],
)
def test_predictions_with_empty_input(bad_data):
    response = client.post("/v0/predict", json=bad_data)
    assert response.status_code == 422


@pytest.mark.parametrize(
    "empty_products",
    [
        pytest.param({"products": []},
                     id="Empty products list"),
    ],
)
def test_predictions_with_empty_products(empty_products):
    response = client.post("/v0/predict", json=empty_products)
    assert response.status_code == 422


@pytest.mark.parametrize(
    "no_title",
    [
        pytest.param(
            {"products": [{"concatenated_tags": "prateleiras decoracao gaveteiros nichos"}]},
            id="Missing title",
        )
    ]
)
def test_predictions_without_title(no_title):
    response = client.post("/v0/predict", json=no_title)
    assert response.status_code == 200


@pytest.mark.parametrize("no_categorized_tags", 
    [
        pytest.param(
            {"products": [{"title": "Painel de Festa Baby Shark 5"}]}, 
            id="Missing tags"
        )
    ]
)
def test_predictions_without_tags(no_categorized_tags):
    response = client.post("/v0/predict", json=no_categorized_tags)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "no_products_key",
    [
        pytest.param(
            {
                "title": "Painel de Festa Baby Shark 5",
                "concatenated_tags": "niver 2 anos baby shark",
            },
            id="Missing Products Key",
        ),
    ],
)
def test_predictions_without_products_key(no_products_key):
    response = client.post("/v0/predict", json=no_products_key)
    assert response.status_code == 422
