from typing import Optional

from syncfusion.utils import CustomBaseModel


class Comment(CustomBaseModel):
    AuthorName: str
    Initials: str
    Text: str
    Left: float
    Top: float
    DateTime: Optional[int] = None
