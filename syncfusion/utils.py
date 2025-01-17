import json
from enum import Enum

from pydantic import BaseModel

def convert_enum_value(value):
    if isinstance(value, Enum):
        return value.value
    elif isinstance(value, dict):
        return {k: convert_enum_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [convert_enum_value(v) for v in value]
    return value


def pretty_print_pydantic_model(pydantic_model):
    """
    Pretty prints a Pydantic model instance, excluding fields with None values.

    Args:
        pydantic_model: A Pydantic model instance.
    """
    model_dict = pydantic_model.dict(exclude_none=True, by_alias=True)
    model_dict = {k: convert_enum_value(v) for k, v in model_dict.items()}
    pretty_model = json.dumps(model_dict, indent=4)
    return pretty_model


class CustomBaseModel(BaseModel):
    def __repr__(self) -> str:
        pretty_repr = pretty_print_pydantic_model(self)
        return pretty_repr

    class Config:
        protected_namespaces = ()
        coerce_numbers_to_str = True
        validate_default = None
        validate_assignment = False
        validate_return = False
