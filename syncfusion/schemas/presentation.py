from __future__ import annotations

import logging
from typing import List, Optional

from .core import SyncfusionBaseModel
from .slide import Slide

logger = logging.getLogger(__name__)


class Presentation(SyncfusionBaseModel):
    # BuiltInDocumentProperties: Optional[IBuiltInDocumentProperties] = None
    # CustomDocumentProperties: Optional[ICustomDocumentProperties] = None
    BuiltInDocumentProperties: Optional[dict] = (
        None  # Change dict to actual model if needed
    )
    CustomDocumentProperties: Optional[dict] = (
        None  # Change dict to actual model if needed
    )
    # ChartToImageConverter: Optional[IOfficeChartToImageConverter] = None
    Final: bool = False
    FirstSlideNumber: int = 1
    HasMacros: bool = False
    IsWriteProtected: bool = False
    Slides: List[Slide] = []
    PresentationTemplate: Optional[str] = None
    PptxBase64String: Optional[str] = None

    def __init__(self, **data):
        logger.debug(f"Initializing Presentation with data: {data}")
        try:
            super().__init__(**data)
        except Exception as e:
            logger.error(f"Error initializing Presentation: {str(e)}")
            logger.error(f"Slides data: {data.get('Slides', [])}")
            raise
