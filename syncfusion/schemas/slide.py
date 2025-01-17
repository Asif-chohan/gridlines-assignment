from __future__ import annotations

from enum import Enum
from typing import Annotated, List, Optional

from pydantic import Field

from .chart import Chart
from .comment import Comment
from .core import Fill, SyncfusionBaseModel, TextBody  # noqa: F401
from .picture import Picture
from .shape import Shape
from .table import Table


class SlideSizeType(str, Enum):
    CUSTOM = "Custom"
    ON_SCREEN = "OnScreen"
    LETTER_PAPER = "LetterPaper"
    A4_PAPER = "A4Paper"
    SLIDE_35MM = "Slide35mm"
    OVERHEAD = "Overhead"
    BANNER = "Banner"
    LEDGER_PAPER = "LedgerPaper"
    A3_PAPER = "A3Paper"
    B4_ISO_PAPER = "B4IsoPaper"
    B5_ISO_PAPER = "B5IsoPaper"
    B4_JIS_PAPER = "B4JisPaper"
    B5_JIS_PAPER = "B5JisPaper"
    HAGAKI_CARD = "HagakiCard"


class SlideOrientation(str, Enum):
    LANDSCAPE = "Landscape"
    PORTRAIT = "Portrait"


class SlideSize(SyncfusionBaseModel):
    Height: float = 540.0
    Width: float = 720.0
    SlideOrientation: SlideOrientation = SlideOrientation.LANDSCAPE
    Type: SlideSizeType = SlideSizeType.CUSTOM


class Background(SyncfusionBaseModel):
    Fill: Annotated[
        Optional[Fill], Field(default=None)
    ]  # Represents fill formatting properties


class HeaderFooter(SyncfusionBaseModel):
    Format: Optional[DateTimeFormatType] = None
    Text: Optional[str] = None
    Visible: bool = False


class HeadersFooters(SyncfusionBaseModel):
    DateAndTime: Optional[HeaderFooter] = None
    Footer: Optional[HeaderFooter] = None
    Header: Optional[HeaderFooter] = None
    SlideNumber: Optional[HeaderFooter] = None


class BaseSlide(SyncfusionBaseModel):
    Background: Annotated[Optional[Background], Field(default=None)]
    Charts: Optional[List[Chart]] = []  # List of charts on the slide
    Name: Optional[str] = None
    HeadersFooters: Annotated[Optional[HeadersFooters], Field(default=None)]
    Pictures: Optional[List[Picture]] = []  # List of pictures on the slide
    Shapes: Optional[List[Shape]] = []  # List of shapes on the slide
    SlideSize: Annotated[Optional[SlideSize], Field(default=None)]
    Tables: Optional[List[Table]] = []  # List of tables on the slide


class SlideLayoutType(Enum):
    BLANK = "Blank"
    COMPARISON = "Comparison"
    CONTENT_WITH_CAPTION = "ContentWithCaption"
    CUSTOM = "Custom"
    PICTURE_WITH_CAPTION = "PictureWithCaption"
    SECTION_HEADER = "SectionHeader"
    TITLE = "Title"
    TITLE_AND_CONTENT = "TitleAndContent"
    TITLE_AND_VERTICAL_TEXT = "TitleAndVerticalText"
    TITLE_ONLY = "TitleOnly"
    TWO_CONTENT = "TwoContent"
    VERTICAL_TITLE_AND_TEXT = "VerticalTitleAndText"


class NotesSlide(BaseSlide):
    NotesTextBody: Optional[TextBody] = None


class DateTimeFormatType(str, Enum):
    DATE_TIME_DDDD_MMMM_DD_YYYY = "DateTimeddddMMMMddyyyy"
    DATE_TIME_D_MMMM_YYYY = "DateTimedMMMMyyyy"
    DATE_TIME_D_MMM_YY = "DateTimedMMMyy"
    DATE_TIME_H_MM = "DateTimeHmm"
    DATE_TIME_H_MM_AMPM = "DateTimehmmAMPM"
    DATE_TIME_H_MM_SS = "DateTimeHmmss"
    DATE_TIME_H_MM_SS_AMPM = "DateTimehmmssAMPM"
    DATE_TIME_M_D_YY = "DateTimeMdyy"
    DATE_TIME_MM_DD_YY_H_MM_AMPM = "DateTimeMMddyyhmmAMPM"
    DATE_TIME_MM_DD_YY_H_MM_SS_AMPM = "DateTimeMMddyyhmmssAMPM"
    DATE_TIME_MMMM_D_YYYY = "DateTimeMMMMdyyyy"
    DATE_TIME_MMMM_YY = "DateTimeMMMMyy"
    DATE_TIME_MMM_YY = "DateTimeMMMyy"
    NONE = "None"


class Slide(BaseSlide):
    SlideTemplate: Optional[str] = None
    Comments: List[Comment] = []
    LayoutType: Optional[SlideLayoutType] = SlideLayoutType.BLANK
    NotesSlide: Annotated[Optional[NotesSlide], Field(default=None)]
    SlideID: int = 0
    SlideNumber: int = 0
    Visible: bool = True


Slide.model_rebuild()
