
from typing import Optional, Dict, List
from pydantic import BaseModel


class request_model(BaseModel):
    template: str

    class Config:
        schema_extra = {
            "template": "ejemplo",
        }