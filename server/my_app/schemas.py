"""Request and response schemas for the FastAPI app.
"""

import pandas as pd
from pydantic import BaseModel, conlist
from typing import Optional

# Request
class Product(BaseModel):
    title: Optional[str] = ''
    concatenated_tags: Optional[str] = ''


class ListOfProducts(BaseModel):
    products: conlist(Product, min_items=1)

    def to_dataframe(self) -> pd.DataFrame:
        products = self.dict()["products"]
        dataframe = pd.DataFrame(products)
        return dataframe


# Response
class Predictions(BaseModel):
    categories: conlist(str, min_items=1)
