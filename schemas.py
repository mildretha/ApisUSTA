from pydantic import BaseModel
from typing import Optional


class InputSchema(BaseModel):

    year: int
    industry_aggregation_nzsioc: str
    industry_code_nzsioc: str
    industry_name_nzsioc: str
    variable_code: str
    variable_name: str
    value: Optional[float]


class OutputSchema(BaseModel):

    year: int
    industry_name_nzsioc: str
    variable_name: str
    value: Optional[float]