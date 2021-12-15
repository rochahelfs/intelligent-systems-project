"""A api app definition using FastAPI.
"""

import json
import cloudpickle

from fastapi import FastAPI, Response

from my_app.schemas import Predictions, ListOfProducts
from my_app.settings import environment


api = FastAPI()

with open(environment.model_path, "rb") as model_file:
    model = cloudpickle.load(model_file)


@api.post("/v0/predict", response_model=Predictions)
def predict(response: Response, products: ListOfProducts):
    df = products.to_dataframe()
    preds = {"categories": list(model.predict(df))}
    response.headers["predictions"] = json.dumps(preds)
    return preds
