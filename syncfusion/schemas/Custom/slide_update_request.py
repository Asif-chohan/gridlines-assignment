from __future__ import annotations

from typing import Optional

from models import CustomBaseModel


class SlideUpdateRequest(CustomBaseModel):
    PptxBase64String: Optional[str] = None
    PresentationTemplate: Optional[str] = None
    Presentation: Optional[Presentation] = None
