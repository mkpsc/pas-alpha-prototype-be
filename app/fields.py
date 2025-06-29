from typing import Annotated
from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel

NHSNumber = Annotated[str, Field(pattern=r"^[0-9]{10}$")]


class BaseCamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        validate_by_name = True
