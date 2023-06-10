from typing import Optional, List
from pydantic import BaseModel


class SamplePostRequest(BaseModel):
    a: int
    b: str
    c: List[int]
    f: Optional[str]
