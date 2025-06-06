from typing import Annotated
from pydantic import Field


NHSNumber = Annotated[str, Field(pattern=r"^[0-9]{10}$")]