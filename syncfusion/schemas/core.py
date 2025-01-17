from __future__ import annotations

from enum import Enum
from typing import Annotated, List, Optional

from pydantic import Field
from pydantic.v1.typing import get_args, get_origin, is_union

from syncfusion.utils import CustomBaseModel


class SyncfusionBaseModel(CustomBaseModel):
    class Config:
        @classmethod
        def prepare_field(cls, field) -> None:
            # check if field is Optional
            if is_union(get_origin(field.outer_type_)) and type(None) in get_args(
                field.outer_type_
            ):
                field.required = False


#### Color


class Color(SyncfusionBaseModel):
    A: Optional[int] = 255
    R: Optional[int] = None
    G: Optional[int] = None
    B: Optional[int] = None
    SystemColor: Optional[str] = None


#### Fill


class FillType(str, Enum):
    AUTOMATIC = "Automatic"
    GRADIENT = "Gradient"
    NONETYPE = "None"  # Renamed to avoid conflict with Python's None
    PATTERN = "Pattern"
    PICTURE = "Picture"
    SOLID = "Solid"
    TEXTURE = "Texture"


class TileMode(str, Enum):
    STRETCH = "Stretch"
    TILE = "Tile"


class PatternFillType(str, Enum):
    CROSS = "Cross"
    DARK_DOWNWARD_DIAGONAL = "DarkDownwardDiagonal"
    DARK_HORIZONTAL = "DarkHorizontal"
    DARK_UPWARD_DIAGONAL = "DarkUpwardDiagonal"
    DARK_VERTICAL = "DarkVertical"
    DASHED_DOWNWARD_DIAGONAL = "DashedDownwardDiagonal"
    DASHED_HORIZONTAL = "DashedHorizontal"
    DASHED_UPWARD_DIAGONAL = "DashedUpwardDiagonal"
    DASHED_VERTICAL = "DashedVertical"
    DIAGONAL_BRICK = "DiagonalBrick"
    DIAGONAL_CROSS = "DiagonalCross"
    DIVOT = "Divot"
    DOTTED_DIAMOND = "DottedDiamond"
    DOTTED_GRID = "DottedGrid"
    DOWNWARD_DIAGONAL = "DownwardDiagonal"
    GRAY_10 = "Gray10"
    GRAY_20 = "Gray20"
    GRAY_25 = "Gray25"
    GRAY_30 = "Gray30"
    GRAY_40 = "Gray40"
    GRAY_5 = "Gray5"
    GRAY_50 = "Gray50"
    GRAY_60 = "Gray60"
    GRAY_70 = "Gray70"
    GRAY_75 = "Gray75"
    GRAY_80 = "Gray80"
    GRAY_90 = "Gray90"
    HORIZONTAL = "Horizontal"
    HORIZONTAL_BRICK = "HorizontalBrick"
    LARGE_CHECKER_BOARD = "LargeCheckerBoard"
    LARGE_CONFETTI = "LargeConfetti"
    LARGE_GRID = "LargeGrid"
    LIGHT_DOWNWARD_DIAGONAL = "LightDownwardDiagonal"
    LIGHT_HORIZONTAL = "LightHorizontal"
    LIGHT_UPWARD_DIAGONAL = "LightUpwardDiagonal"
    LIGHT_VERTICAL = "LightVertical"
    NARROW_HORIZONTAL = "NarrowHorizontal"
    NARROW_VERTICAL = "NarrowVertical"
    OUTLINED_DIAMOND = "OutlinedDiamond"
    PLAID = "Plaid"
    SHINGLE = "Shingle"
    SMALL_CHECKER_BOARD = "SmallCheckerBoard"
    SMALL_CONFETTI = "SmallConfetti"
    SMALL_GRID = "SmallGrid"
    SOLID = "Solid"
    SOLID_DIAMOND = "SolidDiamond"
    SPHERE = "Sphere"
    TRELLIS = "Trellis"
    UPWARD_DIAGONAL = "UpwardDiagonal"
    VERTICAL = "Vertical"
    WAVE = "Wave"
    WEAVE = "Weave"
    WIDE_DOWNWARD_DIAGONAL = "WideDownwardDiagonal"
    WIDE_UPWARD_DIAGONAL = "WideUpwardDiagonal"
    ZIG_ZAG = "ZigZag"


class SolidFill(SyncfusionBaseModel):
    Color: Annotated[Optional[Color], Optional[str], Field(default=None)]  # The color of the solid fill
    Transparency: Optional[int] = 0


class GradientStop(SyncfusionBaseModel):
    Brightness: Optional[float] = None
    Color: Annotated[Optional[Color], Optional[str], Field(default=None)]
    Position: Optional[float] = None
    Transparency: Optional[int] = None


class GradientFill(SyncfusionBaseModel):
    GradientStops: Optional[List[GradientStop]] = None


class PictureFill(SyncfusionBaseModel):
    ImageBytes: Optional[List[str]] = None  # Represents the image as bytes
    TileMode: Annotated[
        Optional[TileMode], Field(default=None)
    ]  # Represents the tile mode of the image
    Transparency: Optional[int] = None  # Represents the transparency of the image


class PatternFill(SyncfusionBaseModel):
    BackColor: Optional[str] = None
    ForeColor: Optional[str] = None
    Pattern: Optional[PatternFillType] = None


class Fill(SyncfusionBaseModel):
    FillType: FillType
    SolidFill: Annotated[
        Optional[SolidFill], Field(default=None)
    ]  # Solid fill instance
    GradientFill: Annotated[
        Optional[GradientFill], Field(default=None)
    ]  # Gradient fill instance
    PatternFill: Annotated[
        Optional[PatternFill], Field(default=None)
    ]  # Pattern fill instance
    PictureFill: Annotated[
        Optional[PictureFill], Field(default=None)
    ]  # Picture fill instance


#### LineFormat


class LineCapStyle(str, Enum):
    FLAT = "Flat"
    NONE = "None"
    ROUND = "Round"
    SQUARE = "Square"


class LineDashStyle(str, Enum):
    DASH = "Dash"  # Specifies the LineDashStyle is dash
    DASH_DOT = "DashDot"  # Specifies the LineDashStyle is dash dot
    DASH_DOT_DOT = "DashDotDot"  # Specifies the LineDashStyle is dash dot dot
    DASH_LONG_DASH = "DashLongDash"  # Specifies the LineDashStyle is dash long dash
    DASH_LONG_DASH_DOT = (
        "DashLongDashDot"  # Specifies the LineDashStyle is dash long dash dot
    )
    DOT = "Dot"  # Specifies the LineDashStyle is dot
    NONE_TYPE = "None"  # Specifies the LineDashStyle is none
    ROUND_DOT = "RoundDot"  # Specifies the LineDashStyle is round dot
    SOLID = "Solid"  # Specifies the LineDashStyle is solid
    SQUARE_DOT = "SquareDot"  # Specifies the LineDashStyle is square dot
    SYSTEM_DASH_DOT = "SystemDashDot"  # Specifies the LineDashStyle is system dash dot


class LineJoinType(str, Enum):
    BEVEL = "Bevel"
    MITER = "Miter"
    NONE = "None"
    ROUND = "Round"


class LineStyle(str, Enum):
    SINGLE = "Single"  # Specifies the LineStyle is single
    THICK_BETWEEN_THIN = (
        "ThickBetweenThin"  # Specifies the LineStyle is thick between thin
    )
    THICK_THIN = "ThickThin"  # Specifies the LineStyle is thick thin
    THIN_THICK = "ThinThick"  # Specifies the LineStyle is thin thick
    THIN_THIN = "ThinThin"  # Specifies the LineStyle is thin thin


class ArrowheadLength(str, Enum):
    LONG = "Long"
    MEDIUM = "Medium"
    NONE = "None"
    SHORT = "Short"


class ArrowheadStyle(str, Enum):
    """Specifies the style of the arrowhead at the end of a line."""

    ARROW = "Arrow"
    ARROW_DIAMOND = "ArrowDiamond"
    ARROW_OPEN = "ArrowOpen"
    ARROW_OVAL = "ArrowOval"
    ARROW_STEALTH = "ArrowStealth"
    NONE = "None"


class ArrowheadWidth(str, Enum):
    """Specifies the width of the arrowhead at the end of a line."""

    MEDIUM = "Medium"
    NARROW = "Narrow"
    NONE = "None"
    WIDE = "Wide"


class LineFormat(SyncfusionBaseModel):
    BeginArrowheadLength: Optional[ArrowheadLength] = None
    BeginArrowheadStyle: Optional[ArrowheadStyle] = None
    BeginArrowheadWidth: Optional[ArrowheadWidth] = None
    CapStyle: Optional[LineCapStyle] = None
    DashStyle: Optional[LineDashStyle] = None
    EndArrowheadLength: Optional[ArrowheadLength] = None
    EndArrowheadStyle: Optional[ArrowheadStyle] = None
    EndArrowheadWidth: Optional[ArrowheadWidth] = None
    Fill: Annotated[Optional[Fill], Field(default=None)]  # Read-only property
    LineJoinType: Annotated[Optional[LineJoinType], Field(default=None)]
    Style: Optional[LineStyle] = None
    Weight: Optional[float] = None  # Line weight in points


#### TextBody


class TextCapsType(str, Enum):
    ALL = "All"  # Specifies the TextCapsType is All
    NONE = "None"  # Specifies the TextCapsType is none
    SMALL = "Small"  # Specifies the TextCapsType is small


class TextUnderlineType(str, Enum):
    DASH = "Dash"  # Specifies the TextUnderlineType is dash
    DASH_DOT_DOT_HEAVY = (
        "DashDotDotHeavy"  # Specifies the TextUnderlineType is dash dot dot heavy
    )
    DASH_DOT_HEAVY = "DashDotHeavy"  # Specifies the TextUnderlineType is dash dot heavy
    DASHED_HEAVY = "DashedHeavy"  # Specifies the TextUnderlineType is dashed heavy
    DASH_LONG = "DashLong"  # Specifies the TextUnderlineType is dash long
    DASH_LONG_HEAVY = (
        "DashLongHeavy"  # Specifies the TextUnderlineType is dash long heavy
    )
    DOT_DASH = "DotDash"  # Specifies the TextUnderlineType is dot dash
    DOT_DOT_DASH = "DotDotDash"  # Specifies the TextUnderlineType is dot dot dash
    DOTTED = "Dotted"  # Specifies the TextUnderlineType is dotted
    DOTTED_HEAVY = "DottedHeavy"  # Specifies the TextUnderlineType is dotted heavy
    DOUBLE = "Double"  # Specifies the TextUnderlineType is double
    HEAVY = "Heavy"  # Specifies the TextUnderlineType is heavy
    NONE = "None"  # Specifies the TextUnderlineType is none
    SINGLE = "Single"  # Specifies the TextUnderlineType is single
    WAVE = "Wave"  # Specifies the TextUnderlineType is wave
    WAVY_DOUBLE = "WavyDouble"  # Specifies the TextUnderlineType is wavy double
    WAVY_HEAVY = "WavyHeavy"  # Specifies the TextUnderlineType is wavy heavy


class Font(SyncfusionBaseModel):
    Bold: Optional[bool] = None  # Indicates if the text is bold
    CapsType: Optional[TextCapsType] = None  # Type of capitalization
    Color: Annotated[Optional[Color], Optional[str], Field(default=None)]  # Default black color
    FontName: Optional[str] = None  # Name of the font
    FontSize: Optional[float] = None  # Size of the font
    HighlightColor: Annotated[Optional[Color], Optional[str], Field(default=None)]  # Highlight color of the text
    Italic: Optional[bool] = None  # Indicates if the text is italic
    LanguageID: Optional[int] = None
    StrikeType: Optional[str] = None  # Type of strikethrough
    Subscript: Optional[bool] = None  # Indicates if the text is subscript
    Superscript: Optional[bool] = None  # Indicates if the text is superscript
    Underline: Optional[TextUnderlineType] = None  # Type of underline


class HorizontalAlignmentType(str, Enum):
    CENTER = "Center"
    DISTRIBUTED = "Distributed"
    JUSTIFY = "Justify"
    LEFT = "Left"
    NONE_TYPE = "None"  # Renamed to avoid conflict with Python's None
    RIGHT = "Right"


class HyperLink(SyncfusionBaseModel):
    Url: str
    ScreenTip: Optional[str] = None


class TextPart(SyncfusionBaseModel):
    Font: Annotated[Optional[Font], Field(default=None)]
    Text: str
    Hyperlink: Annotated[Optional[HyperLink], Field(default=None)]
    UnderlineColor: Optional[Color] = None


class NumberedListStyle(str, Enum):
    ALPHA_LC_PAREN_BOTH = "AlphaLcParenBoth"
    ALPHA_LC_PAREN_RIGHT = "AlphaLcParenRight"
    ALPHA_LC_PERIOD = "AlphaLcPeriod"
    ALPHA_UC_PAREN_BOTH = "AlphaUcParenBoth"
    ALPHA_UC_PAREN_RIGHT = "AlphaUcParenRight"
    ALPHA_UC_PERIOD = "AlphaUcPeriod"
    ARABIC_DB_PERIOD = "ArabicDbPeriod"
    ARABIC_DB_PLAIN = "ArabicDbPlain"
    ARABIC_PAREN_BOTH = "ArabicParenBoth"
    ARABIC_PAREN_RIGHT = "ArabicParenRight"
    ARABIC_PERIOD = "ArabicPeriod"
    ARABIC_PLAIN = "ArabicPlain"
    CIRCLE_NUM_DB_PLAIN = "CircleNumDbPlain"
    CIRCLE_NUM_WD_BLACK_PLAIN = "CircleNumWdBlackPlain"
    CIRCLE_NUM_WD_WHITE_PLAIN = "CircleNumWdWhitePlain"
    HEBREW_ALPHA_DASH = "HebrewAlphaDash"
    HINDI_ALPHA_1_PERIOD = "HindiAlpha1Period"
    HINDI_ALPHA_PERIOD = "HindiAlphaPeriod"
    HINDI_NUM_PAREN_RIGHT = "HindiNumParenRight"
    HINDI_NUM_PERIOD = "HindiNumPeriod"
    ROMAN_LC_PAREN_BOTH = "RomanLcParenBoth"
    ROMAN_LC_PAREN_RIGHT = "RomanLcParenRight"
    ROMAN_LC_PERIOD = "RomanLcPeriod"
    ROMAN_UC_PAREN_BOTH = "RomanUcParenBoth"
    ROMAN_UC_PAREN_RIGHT = "RomanUcParenRight"
    ROMAN_UC_PERIOD = "RomanUcPeriod"
    THAI_ALPHA_PAREN_BOTH = "ThaiAlphaParenBoth"
    THAI_ALPHA_PAREN_RIGHT = "ThaiAlphaParenRight"
    THAI_ALPHA_PERIOD = "ThaiAlphaPeriod"
    THAI_NUM_PAREN_BOTH = "ThaiNumParenBoth"
    THAI_NUM_PAREN_RIGHT = "ThaiNumParenRight"
    THAI_NUM_PERIOD = "ThaiNumPeriod"


class ListType(str, Enum):
    BULLETED = "Bulleted"
    NONE_TYPE = "None"
    NOT_DEFINED = "NotDefined"
    NUMBERED = "Numbered"
    PICTURE = "Picture"


class ListFormat(SyncfusionBaseModel):
    BulletCharacter: Optional[str] = None
    Color: Annotated[Optional[Color | str], Field(default=None)]
    FontName: Optional[str] = None
    NumberStyle: Optional[NumberedListStyle] = None
    Size: Optional[float] = None
    StartValue: Optional[int] = None
    Type: Optional[ListType] = None


class Paragraph(SyncfusionBaseModel):
    FirstLineIndent: Optional[float] = None
    Font: Annotated[Optional[Font], Field(default=None)]
    HorizontalAlignment: Optional[HorizontalAlignmentType] = None
    IndentLevelNumber: Optional[int] = None
    LeftIndent: Optional[float] = None
    LineSpacing: Optional[float] = None
    ListFormat: Annotated[Optional[ListFormat], Field(default=None)]
    SpaceAfter: Optional[float] = None
    SpaceBefore: Optional[float] = None
    Text: Optional[str] = None
    TextParts: Optional[List[TextPart]] = None


class VerticalAlignmentType(Enum):
    BOTTOM = "Bottom"
    MIDDLE = "Middle"
    NONE = "None"
    TOP = "Top"


class TextDirectionType(str, Enum):
    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"
    VERTICAL270 = "Vertical270"
    WORDART_VERTICAL = "WordArtVertical"


class TextBody(SyncfusionBaseModel):
    AnchorCenter: Optional[bool] = (
        None  # Indicates whether to anchor center with vertical alignment
    )
    MarginBottom: Optional[float] = None  # Margin bottom in points
    MarginLeft: Optional[float] = None  # Margin left in points
    MarginRight: Optional[float] = None  # Margin right in points
    MarginTop: Optional[float] = None  # Margin top in points
    Paragraphs: Optional[List[Paragraph]] = None  # Collection of paragraphs
    Text: Optional[str] = None  # Text content of the text body
    TextDirection: Optional[TextDirectionType] = None  # Text direction
    VerticalAlignment: Optional[VerticalAlignmentType] = (
        None  # Vertical alignment of text
    )
    WrapText: Optional[bool] = None  # Set default to True for text wrapping


#### SlideItem


class SlideItemType(str, Enum):
    AUTOSHAPE = "AutoShape"
    CHART = "Chart"
    CONNECTIONSHAPE = "ConnectionShape"
    GROUPSHAPE = "GroupShape"
    OLEOBJECT = "OleObject"
    PICTURE = "Picture"
    PLACEHOLDER = "Placeholder"
    SMARTART = "SmartArt"
    TABLE = "Table"
    UNKNOWN = "Unknown"


class SlideItem(SyncfusionBaseModel):
    Description: Optional[str] = None
    Height: float  # Required, no default
    Hidden: Optional[bool] = None
    Left: float  # Required, no default
    LineFormat: Annotated[Optional[LineFormat], Field(default=None)]
    ShapeName: Optional[str] = None
    SlideItemType: SlideItemType
    Title: Optional[str] = None
    Top: float  # Required, no default
    Width: float  # Required, no default
