from __future__ import annotations

from enum import Enum
from typing import Annotated, List, Optional

from pydantic import Field

from .core import LineFormat, SlideItem, SyncfusionBaseModel, Fill, TextBody, SlideItemType


class BuiltInTableStyle(str, Enum):
    CUSTOM = "Custom"
    DARK_STYLE_1 = "DarkStyle1"
    DARK_STYLE_1_ACCENT_1 = "DarkStyle1Accent1"
    DARK_STYLE_1_ACCENT_2 = "DarkStyle1Accent2"
    DARK_STYLE_1_ACCENT_3 = "DarkStyle1Accent3"
    DARK_STYLE_1_ACCENT_4 = "DarkStyle1Accent4"
    DARK_STYLE_1_ACCENT_5 = "DarkStyle1Accent5"
    DARK_STYLE_1_ACCENT_6 = "DarkStyle1Accent6"
    DARK_STYLE_2 = "DarkStyle2"
    DARK_STYLE_2_ACCENT_1_ACCENT_2 = "DarkStyle2Accent1Accent2"
    DARK_STYLE_2_ACCENT_3_ACCENT_4 = "DarkStyle2Accent3Accent4"
    DARK_STYLE_2_ACCENT_5_ACCENT_6 = "DarkStyle2Accent5Accent6"
    LIGHT_STYLE_1 = "LightStyle1"
    LIGHT_STYLE_1_ACCENT_1 = "LightStyle1Accent1"
    LIGHT_STYLE_1_ACCENT_2 = "LightStyle1Accent2"
    LIGHT_STYLE_1_ACCENT_3 = "LightStyle1Accent3"
    LIGHT_STYLE_1_ACCENT_4 = "LightStyle1Accent4"
    LIGHT_STYLE_1_ACCENT_5 = "LightStyle1Accent5"
    LIGHT_STYLE_1_ACCENT_6 = "LightStyle1Accent6"
    LIGHT_STYLE_2 = "LightStyle2"
    LIGHT_STYLE_2_ACCENT_1 = "LightStyle2Accent1"
    LIGHT_STYLE_2_ACCENT_2 = "LightStyle2Accent2"
    LIGHT_STYLE_2_ACCENT_3 = "LightStyle2Accent3"
    LIGHT_STYLE_2_ACCENT_4 = "LightStyle2Accent4"
    LIGHT_STYLE_2_ACCENT_5 = "LightStyle2Accent5"
    LIGHT_STYLE_2_ACCENT_6 = "LightStyle2Accent6"
    LIGHT_STYLE_3 = "LightStyle3"
    LIGHT_STYLE_3_ACCENT_1 = "LightStyle3Accent1"
    LIGHT_STYLE_3_ACCENT_2 = "LightStyle3Accent2"
    LIGHT_STYLE_3_ACCENT_3 = "LightStyle3Accent3"
    LIGHT_STYLE_3_ACCENT_4 = "LightStyle3Accent4"
    LIGHT_STYLE_3_ACCENT_5 = "LightStyle3Accent5"
    LIGHT_STYLE_3_ACCENT_6 = "LightStyle3Accent6"
    MEDIUM_STYLE_1 = "MediumStyle1"
    MEDIUM_STYLE_1_ACCENT_1 = "MediumStyle1Accent1"
    MEDIUM_STYLE_1_ACCENT_2 = "MediumStyle1Accent2"
    MEDIUM_STYLE_1_ACCENT_3 = "MediumStyle1Accent3"
    MEDIUM_STYLE_1_ACCENT_4 = "MediumStyle1Accent4"
    MEDIUM_STYLE_1_ACCENT_5 = "MediumStyle1Accent5"
    MEDIUM_STYLE_1_ACCENT_6 = "MediumStyle1Accent6"
    MEDIUM_STYLE_2 = "MediumStyle2"
    MEDIUM_STYLE_2_ACCENT_1 = "MediumStyle2Accent1"
    MEDIUM_STYLE_2_ACCENT_2 = "MediumStyle2Accent2"
    MEDIUM_STYLE_2_ACCENT_3 = "MediumStyle2Accent3"
    MEDIUM_STYLE_2_ACCENT_4 = "MediumStyle2Accent4"
    MEDIUM_STYLE_2_ACCENT_5 = "MediumStyle2Accent5"
    MEDIUM_STYLE_2_ACCENT_6 = "MediumStyle2Accent6"
    MEDIUM_STYLE_3 = "MediumStyle3"
    MEDIUM_STYLE_3_ACCENT_1 = "MediumStyle3Accent1"
    MEDIUM_STYLE_3_ACCENT_2 = "MediumStyle3Accent2"
    MEDIUM_STYLE_3_ACCENT_3 = "MediumStyle3Accent3"
    MEDIUM_STYLE_3_ACCENT_4 = "MediumStyle3Accent4"
    MEDIUM_STYLE_3_ACCENT_5 = "MediumStyle3Accent5"
    MEDIUM_STYLE_3_ACCENT_6 = "MediumStyle3Accent6"
    MEDIUM_STYLE_4 = "MediumStyle4"
    MEDIUM_STYLE_4_ACCENT_1 = "MediumStyle4Accent1"
    MEDIUM_STYLE_4_ACCENT_2 = "MediumStyle4Accent2"
    MEDIUM_STYLE_4_ACCENT_3 = "MediumStyle4Accent3"
    MEDIUM_STYLE_4_ACCENT_4 = "MediumStyle4Accent4"
    MEDIUM_STYLE_4_ACCENT_5 = "MediumStyle4Accent5"
    MEDIUM_STYLE_4_ACCENT_6 = "MediumStyle4Accent6"
    NONE_TYPE = "None"  # Renamed to avoid conflict with Python's None
    NO_STYLE_NO_GRID = "NoStyleNoGrid"
    NO_STYLE_TABLE_GRID = "NoStyleTableGrid"
    THEMED_STYLE_1_ACCENT_1 = "ThemedStyle1Accent1"
    THEMED_STYLE_1_ACCENT_2 = "ThemedStyle1Accent2"
    THEMED_STYLE_1_ACCENT_3 = "ThemedStyle1Accent3"
    THEMED_STYLE_1_ACCENT_4 = "ThemedStyle1Accent4"
    THEMED_STYLE_1_ACCENT_5 = "ThemedStyle1Accent5"
    THEMED_STYLE_1_ACCENT_6 = "ThemedStyle1Accent6"
    THEMED_STYLE_2_ACCENT_1 = "ThemedStyle2Accent1"
    THEMED_STYLE_2_ACCENT_2 = "ThemedStyle2Accent2"
    THEMED_STYLE_2_ACCENT_3 = "ThemedStyle2Accent3"
    THEMED_STYLE_2_ACCENT_4 = "ThemedStyle2Accent4"
    THEMED_STYLE_2_ACCENT_5 = "ThemedStyle2Accent5"
    THEMED_STYLE_2_ACCENT_6 = "ThemedStyle2Accent6"


class TableCellBorders(SyncfusionBaseModel):
    BorderBottom: Optional[LineFormat] = None
    BorderLeft: Optional[LineFormat] = None
    BorderRight: Optional[LineFormat] = None
    BorderUp: Optional[LineFormat] = None
    BorderDiagonalUp: Optional[LineFormat] = None
    BorderDiagonalDown: Optional[LineFormat] = None


class TableCell(SyncfusionBaseModel):
    CellBorders: Optional[TableCellBorders] = None
    ColumnSpan: Optional[int] = None
    ColumnWidth: Optional[float] = None
    Fill: Annotated[Optional[Fill], Field(default=None)]
    IsHorizontalMerge: Optional[bool] = None
    IsVerticalMerge: Optional[bool] = None
    RowSpan: Optional[int] = None
    TextBody: Annotated[Optional[TextBody], Field(default=None)]


class TableRow(SyncfusionBaseModel):
    Height: Optional[float] = None
    Cells: List[TableCell]


class Table(SlideItem):
    SlideItemType: SlideItemType = SlideItemType.TABLE
    BuiltInStyle: Optional[BuiltInTableStyle] = None
    HasBandedColumns: Optional[bool] = None
    HasBandedRows: Optional[bool] = None
    HasFirstColumn: Optional[bool] = None
    HasHeaderRow: Optional[bool] = None
    HasLastColumn: Optional[bool] = None
    HasTotalRow: Optional[bool] = None
    Rows: Optional[List[TableRow]] = None
