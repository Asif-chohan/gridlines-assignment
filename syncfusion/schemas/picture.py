from __future__ import annotations

from typing import Annotated, Optional

from pydantic import Field

from .core import SlideItem, SlideItemType, SyncfusionBaseModel


class Crop(SyncfusionBaseModel):
    OffsetX: Optional[float] = None
    OffsetY: Optional[float] = None
    Width: Optional[float] = None
    Height: Optional[float] = None
    ContainerLeft: Optional[float] = None
    ContainerTop: Optional[float] = None
    ContainerWidth: Optional[float] = None
    ContainerHeight: Optional[float] = None


class Picture(SlideItem):
    SlideItemType: SlideItemType = SlideItemType.PICTURE
    Crop: Annotated[Optional[Crop], Field(default=None)]
    ImageData: str
    FallbackImageData: Optional[str] = None
