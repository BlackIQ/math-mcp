# Libs
from typing import Annotated, TypeAlias  # Types

from pydantic import Field  # Pydantic

Number: TypeAlias = Annotated[
    float,
    Field(description="A numeric value"),
]  # Number
