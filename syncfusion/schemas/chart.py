
from enum import Enum

from syncfusion.utils import CustomBaseModel


class ChartTickMark(Enum):
    TICK_MARK_CROSS = "TickMark_Cross"
    TICK_MARK_INSIDE = "TickMark_Inside"
    TICK_MARK_NONE = "TickMark_None"
    TICK_MARK_OUTSIDE = "TickMark_Outside"


class ChartAxisType(Enum):
    CATEGORY = "Category"
    SERIE = "Serie"
    VALUE = "Value"


class ChartArrowType(Enum):
    ARROW = "Arrow"
    DIAMOND_ARROW = "DiamondArrow"
    NONE = "None"
    OPEN_ARROW = "OpenArrow"
    OVAL_ARROW = "OvalArrow"
    STEALTH_ARROW = "StealthArrow"


class ChartArrowSize(Enum):
    ARROW_L_SIZE_1 = "ArrowLSize1"
    ARROW_L_SIZE_2 = "ArrowLSize2"
    ARROW_L_SIZE_3 = "ArrowLSize3"
    ARROW_L_SIZE_4 = "ArrowLSize4"
    ARROW_L_SIZE_5 = "ArrowLSize5"
    ARROW_L_SIZE_6 = "ArrowLSize6"
    ARROW_L_SIZE_7 = "ArrowLSize7"
    ARROW_L_SIZE_8 = "ArrowLSize8"
    ARROW_L_SIZE_9 = "ArrowLSize9"


class ChartKnownColors(Enum):
    AQUA = "Aqua"
    BLACK = "Black"
    BLACK_CUSTOM = "BlackCustom"
    BLUE = "Blue"
    BLUE_GREY = "Blue_grey"
    BLUE_CUSTOM = "BlueCustom"
    BRIGHT_GREEN = "Bright_green"
    BROWN = "Brown"
    CYAN = "Cyan"
    DARK_BLUE = "Dark_blue"
    DARK_GREEN = "Dark_green"
    DARK_RED = "Dark_red"
    DARK_TEAL = "Dark_teal"
    DARK_YELLOW = "Dark_yellow"
    GOLD = "Gold"
    GREEN = "Green"
    GREY_25_PERCENT = "Grey_25_percent"
    GREY_40_PERCENT = "Grey_40_percent"
    GREY_50_PERCENT = "Grey_50_percent"
    GREY_80_PERCENT = "Grey_80_percent"
    INDIGO = "Indigo"
    LAVENDER = "Lavender"
    LIGHT_BLUE = "Light_blue"
    LIGHT_GREEN = "Light_green"
    LIGHT_ORANGE = "Light_orange"
    LIGHT_TURQUOISE = "Light_turquoise"
    LIGHT_YELLOW = "Light_yellow"
    LIGHT_GREEN_ALT = "LightGreen"
    LIME = "Lime"
    MAGENTA = "Magenta"
    NONE = "None"
    OLIVE_GREEN = "Olive_green"
    ORANGE = "Orange"
    PALE_BLUE = "Pale_blue"
    PINK = "Pink"
    PLUM = "Plum"
    RED = "Red"
    RED_ALT = "Red2"
    ROSE = "Rose"
    SEA_GREEN = "Sea_green"
    SKY_BLUE = "Sky_blue"
    TAN = "Tan"
    TEAL = "Teal"
    TURQUOISE = "Turquoise"
    VIOLET = "Violet"
    WHITE = "White"
    WHITE_CUSTOM = "WhiteCustom"
    YELLOW = "Yellow"
    YELLOW_CUSTOM = "YellowCustom"


class ChartLinePattern(Enum):
    CIRCLE_DOT = "CircleDot"
    DARK_GRAY = "DarkGray"
    DASH = "Dash"
    DASH_DOT = "DashDot"
    DASH_DOT_DOT = "DashDotDot"
    DOT = "Dot"
    LIGHT_GRAY = "LightGray"
    LONG_DASH = "LongDash"
    LONG_DASH_DOT = "LongDashDot"
    LONG_DASH_DOT_DOT = "LongDashDotDot"
    MEDIUM_GRAY = "MediumGray"
    NONE = "None"
    SOLID = "Solid"


class ChartLineWeight(Enum):
    HAIRLINE = "Hairline"
    MEDIUM = "Medium"
    NARROW = "Narrow"
    WIDE = "Wide"


class ChartTickLabelPosition(Enum):
    HIGH = "TickLabelPosition_High"
    LOW = "TickLabelPosition_Low"
    NEXT_TO_AXIS = "TickLabelPosition_NextToAxis"
    NONE = "TickLabelPosition_None"


class ChartUnderline(Enum):
    DASH = "Dash"
    DASH_HEAVY = "DashHeavy"
    DASH_LONG = "DashLong"
    DASH_LONG_HEAVY = "DashLongHeavy"
    DOT_DASH = "DotDash"
    DOT_DASH_HEAVY = "DotDashHeavy"
    DOT_DOT_DASH = "DotDotDash"
    DOT_DOT_DASH_HEAVY = "DotDotDashHeavy"
    DOTTED = "Dotted"
    DOTTED_HEAVY = "DottedHeavy"
    DOUBLE = "Double"
    DOUBLE_ACCOUNTING = "DoubleAccounting"
    HEAVY = "Heavy"
    NONE = "None"
    SINGLE = "Single"
    SINGLE_ACCOUNTING = "SingleAccounting"
    WAVY = "Wavy"
    WAVY_DOUBLE = "WavyDouble"
    WAVY_HEAVY = "WavyHeavy"
    WORDS = "Words"


class ChartFontVerticalAlignment(Enum):
    BASELINE = "Baseline"
    SUBSCRIPT = "Subscript"
    SUPERSCRIPT = "Superscript"


class ChartFillType(Enum):
    GRADIENT = "Gradient"
    PATTERN = "Pattern"
    PICTURE = "Picture"
    SOLID_COLOR = "SolidColor"
    TEXTURE = "Texture"
    UNKNOWN_GRADIENT = "UnknownGradient"


class ChartGradientColor(Enum):
    ONE_COLOR = "OneColor"
    PRESET = "Preset"
    TWO_COLOR = "TwoColor"


class ChartGradientVariants(Enum):
    SHADING_VARIANTS_1 = "ShadingVariants_1"
    SHADING_VARIANTS_2 = "ShadingVariants_2"
    SHADING_VARIANTS_3 = "ShadingVariants_3"
    SHADING_VARIANTS_4 = "ShadingVariants_4"


class ChartGradientStyle(Enum):
    DIAGONAL_DOWN = "DiagonalDown"
    DIAGONAL_UP = "DiagonalUp"
    DIAGONL_DOWN = "Diagonl_Down"
    DIAGONL_UP = "Diagonl_Up"
    FROM_CENTER = "From_Center"
    FROM_CORNER = "From_Corner"
    FROMCENTER = "FromCenter"
    FROMCORNER = "FromCorner"
    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"


class ChartLayoutModes(Enum):
    AUTO = "auto"
    EDGE = "edge"
    FACTOR = "factor"


class ChartLayoutTargets(Enum):
    AUTO = "auto"
    INNER = "inner"
    OUTER = "outer"


class ChartLegendPosition(Enum):
    BOTTOM = "Bottom"  # Legend positioned below the chart.
    CORNER = "Corner"  # Legend positioned in the upper right-hand corner of the chart border.
    LEFT = "Left"  # Legend positioned to the left of the chart.
    NOT_DOCKED = "NotDocked"  # Legend is not docked.
    RIGHT = "Right"  # Legend positioned to the right of the chart.
    TOP = "Top"  # Legend positioned above the chart.


class ChartDisplayUnit(Enum):
    CUSTOM = "Custom"  # Indicates custom units.
    HUNDRED_MILLIONS = "HundredMillions"  # Indicates units of hundreds of millions.
    HUNDREDS = "Hundreds"  # Indicates units of hundreds.
    HUNDRED_THOUSANDS = "HundredThousands"  # Indicates units of hundreds of thousands.
    MILLION_MILLIONS = "MillionMillions"  # Indicates units of millions of millions.
    MILLIONS = "Millions"  # Indicates units of millions.
    NONE = "None"  # Indicates no units are displayed.
    TEN_MILLIONS = "TenMillions"  # Indicates units of tens of millions.
    TEN_THOUSANDS = "TenThousands"  # Indicates units of tens of thousands.
    THOUSAND_MILLIONS = "ThousandMillions"  # Indicates units of thousands of millions.
    THOUSANDS = "Thousands"  # Indicates units of thousands.


class ChartBaseUnit(Enum):
    DAY = "Day"  # Indicates Day units.
    MONTH = "Month"  # Indicates Month units.
    YEAR = "Year"  # Indicates Year units.


class ChartCategoryType(Enum):
    AUTOMATIC = "Automatic"  # Indicates automatic category type.
    CATEGORY = "Category"  # Axis groups data by an arbitrary set of categories.
    TIME = "Time"  # Axis groups data on a time scale.


class ChartDataLabelPosition(Enum):
    ABOVE = "Above"  # Indicates data label positioned above the point.
    AUTOMATIC = "Automatic"  # Indicates default position.
    BELOW = "Below"  # Indicates data label positioned below the point.
    BEST_FIT = "BestFit"  # Indicates the BestFit data label placement option.
    CENTER = "Center"  # Indicates the Center data label placement option.
    INSIDE = "Inside"  # Indicates the Inside data label placement option.
    LEFT = "Left"  # Indicates the Left data label placement option.
    MOVED = "Moved"  # Indicates the Moved data label placement option.
    OUTSIDE = "Outside"  # Indicates the Outside data label placement option.
    OUTSIDE_BASE = (
        "OutsideBase"  # Indicates the OutsideBase data label placement option.
    )
    RIGHT = "Right"  # Indicates the Right data label placement option.


class ChartType(Enum):
    AREA = "Area"  # Indicates the Area chart type.
    AREA_3D = "Area_3D"  # Indicates the Area_3D chart type.
    AREA_STACKED = "Area_Stacked"  # Indicates the Area_Stacked chart type.
    AREA_STACKED_100 = "Area_Stacked_100"  # Indicates the Area_Stacked_100 chart type.
    AREA_STACKED_100_3D = (
        "Area_Stacked_100_3D"  # Indicates the Area_Stacked_100_3D chart type.
    )
    AREA_STACKED_3D = "Area_Stacked_3D"  # Indicates the Area_Stacked_3D chart type.
    BAR_CLUSTERED = "Bar_Clustered"  # Indicates the Bar_Clustered chart type.
    BAR_CLUSTERED_3D = "Bar_Clustered_3D"  # Indicates the Bar_Clustered_3D chart type.
    BAR_STACKED = "Bar_Stacked"  # Indicates the Bar_Stacked chart type.
    BAR_STACKED_100 = "Bar_Stacked_100"  # Indicates the Bar_Stacked_100 chart type.
    BAR_STACKED_100_3D = (
        "Bar_Stacked_100_3D"  # Indicates the Bar_Stacked_100_3D chart type.
    )
    BAR_STACKED_3D = "Bar_Stacked_3D"  # Indicates the Bar_Stacked_3D chart type.
    BOX_AND_WHISKER = "BoxAndWhisker"  # Indicates the BoxAndWhisker chart type.
    BUBBLE = "Bubble"  # Indicates the Bubble chart type.
    BUBBLE_3D = "Bubble_3D"  # Indicates the Bubble_3D chart type.
    COLUMN_3D = "Column_3D"  # Indicates the Column_3D chart type.
    COLUMN_CLUSTERED = "Column_Clustered"  # Indicates the Column_Clustered chart type.
    COLUMN_CLUSTERED_3D = (
        "Column_Clustered_3D"  # Indicates the Column_Clustered_3D chart type.
    )
    COLUMN_STACKED = "Column_Stacked"  # Indicates the Column_Stacked chart type.
    COLUMN_STACKED_100 = (
        "Column_Stacked_100"  # Indicates the Column_Stacked_100 chart type.
    )
    COLUMN_STACKED_100_3D = (
        "Column_Stacked_100_3D"  # Indicates the Column_Stacked_100_3D chart type.
    )
    COLUMN_STACKED_3D = (
        "Column_Stacked_3D"  # Indicates the Column_Stacked_3D chart type.
    )
    COMBINATION_CHART = (
        "Combination_Chart"  # Indicates the chart containing different series types.
    )
    CONE_BAR_CLUSTERED = (
        "Cone_Bar_Clustered"  # Indicates the Cone_Bar_Clustered chart type.
    )
    CONE_BAR_STACKED = "Cone_Bar_Stacked"  # Indicates the Cone_Bar_Stacked chart type.
    CONE_BAR_STACKED_100 = (
        "Cone_Bar_Stacked_100"  # Indicates the Cone_Bar_Stacked_100 chart type.
    )
    CONE_CLUSTERED = "Cone_Clustered"  # Indicates the Cone_Clustered chart type.
    CONE_CLUSTERED_3D = (
        "Cone_Clustered_3D"  # Indicates the Cone_Clustered_3D chart type.
    )
    CONE_STACKED = "Cone_Stacked"  # Indicates the Cone_Stacked chart type.
    CONE_STACKED_100 = "Cone_Stacked_100"  # Indicates the Cone_Stacked_100 chart type.
    CYLINDER_BAR_CLUSTERED = (
        "Cylinder_Bar_Clustered"  # Indicates the Cylinder_Bar_Clustered chart type.
    )
    CYLINDER_BAR_STACKED = (
        "Cylinder_Bar_Stacked"  # Indicates the Cylinder_Bar_Stacked chart type.
    )
    CYLINDER_BAR_STACKED_100 = (
        "Cylinder_Bar_Stacked_100"  # Indicates the Cylinder_Bar_Stacked_100 chart type.
    )
    CYLINDER_CLUSTERED = (
        "Cylinder_Clustered"  # Indicates the Cylinder_Clustered chart type.
    )
    CYLINDER_CLUSTERED_3D = (
        "Cylinder_Clustered_3D"  # Indicates the Cylinder_Clustered_3D chart type.
    )
    CYLINDER_STACKED = "Cylinder_Stacked"  # Indicates the Cylinder_Stacked chart type.
    CYLINDER_STACKED_100 = (
        "Cylinder_Stacked_100"  # Indicates the Cylinder_Stacked_100 chart type.
    )
    DOUGHNUT = "Doughnut"  # Indicates the Doughnut chart type.
    DOUGHNUT_EXPLODED = (
        "Doughnut_Exploded"  # Indicates the Doughnut_Exploded chart type.
    )
    FUNNEL = "Funnel"  # Indicates the Funnel chart type.
    HISTOGRAM = "Histogram"  # Indicates the Histogram chart type.
    LINE = "Line"  # Indicates the Line chart type.
    LINE_3D = "Line_3D"  # Indicates the Line_3D chart type.
    LINE_MARKERS = "Line_Markers"  # Indicates the Line_Markers chart type.
    LINE_MARKERS_STACKED = (
        "Line_Markers_Stacked"  # Indicates the Line_Markers_Stacked chart type.
    )
    LINE_MARKERS_STACKED_100 = (
        "Line_Markers_Stacked_100"  # Indicates the Line_Markers_Stacked_100 chart type.
    )
    LINE_STACKED = "Line_Stacked"  # Indicates the Line_Stacked chart type.
    LINE_STACKED_100 = "Line_Stacked_100"  # Indicates the Line_Stacked_100 chart type.
    PARETO = "Pareto"  # Indicates the Pareto chart type.
    PIE = "Pie"  # Indicates the Pie chart type.
    PIE_3D = "Pie_3D"  # Indicates the Pie_3D chart type.
    PIE_BAR = "Pie_Bar"  # Indicates the Pie_Bar chart type.
    PIE_EXPLODED = "Pie_Exploded"  # Indicates the Pie_Exploded chart type.
    PIE_EXPLODED_3D = "Pie_Exploded_3D"  # Indicates the Pie_Exploded_3D chart type.
    PIE_OF_PIE = "PieOfPie"  # Indicates the PieOfPie chart type.
    PYRAMID_BAR_CLUSTERED = (
        "Pyramid_Bar_Clustered"  # Indicates the Pyramid_Bar_Clustered chart type.
    )
    PYRAMID_BAR_STACKED = (
        "Pyramid_Bar_Stacked"  # Indicates the Pyramid_Bar_Stacked chart type.
    )
    PYRAMID_BAR_STACKED_100 = (
        "Pyramid_Bar_Stacked_100"  # Indicates the Pyramid_Bar_Stacked_100 chart type.
    )
    PYRAMID_CLUSTERED = (
        "Pyramid_Clustered"  # Indicates the Pyramid_Clustered chart type.
    )
    PYRAMID_CLUSTERED_3D = (
        "Pyramid_Clustered_3D"  # Indicates the Pyramid_Clustered_3D chart type.
    )
    PYRAMID_STACKED = "Pyramid_Stacked"  # Indicates the Pyramid_Stacked chart type.
    PYRAMID_STACKED_100 = (
        "Pyramid_Stacked_100"  # Indicates the Pyramid_Stacked_100 chart type.
    )
    RADAR = "Radar"  # Indicates the Radar chart type.
    RADAR_FILLED = "Radar_Filled"  # Indicates the Radar_Filled chart type.
    RADAR_MARKERS = "Radar_Markers"  # Indicates the Radar_Markers chart type.
    SCATTER_LINE = "Scatter_Line"  # Indicates the Scatter_Line chart type.
    SCATTER_LINE_MARKERS = (
        "Scatter_Line_Markers"  # Indicates the Scatter_Line_Markers chart type.
    )
    SCATTER_MARKERS = "Scatter_Markers"  # Indicates the Scatter_Markers chart type.
    SCATTER_SMOOTHED_LINE = (
        "Scatter_SmoothedLine"  # Indicates the Scatter_SmoothedLine chart type.
    )
    SCATTER_SMOOTHED_LINE_MARKERS = "Scatter_SmoothedLine_Markers"  # Indicates the Scatter_SmoothedLine_Markers chart type.
    STOCK_HIGH_LOW_CLOSE = (
        "Stock_HighLowClose"  # Indicates the Stock_HighLowClose chart type.
    )
    STOCK_OPEN_HIGH_LOW_CLOSE = (
        "Stock_OpenHighLowClose"  # Indicates the Stock_OpenHighLowClose chart type.
    )
    STOCK_VOLUME_HIGH_LOW_CLOSE = (
        "Stock_VolumeHighLowClose"  # Indicates the Stock_VolumeHighLowClose chart type.
    )
    STOCK_VOLUME_OPEN_HIGH_LOW_CLOSE = "Stock_VolumeOpenHighLowClose"  # Indicates the Stock_VolumeOpenHighLowClose chart type.
    SUNBURST = "SunBurst"  # Indicates the SunBurst chart type.
    SURFACE_3D = "Surface_3D"  # Indicates the Surface_3D chart type.
    SURFACE_CONTOUR = "Surface_Contour"  # Indicates the Surface_Contour chart type.
    SURFACE_NO_COLOR_3D = (
        "Surface_NoColor_3D"  # Indicates the Surface_NoColor_3D chart type.
    )
    TREEMAP = "TreeMap"  # Indicates the TreeMap chart type.
    WATERFALL = "Waterfall"  # Indicates the Waterfall chart type.
    XY_SCATTER = "XYScatter"  # Indicates the XYScatter chart type.
    XY_SCATTER_LINES = "XYScatter_Lines"  # Indicates the XYScatter_Lines chart type.
    XY_SCATTER_LINES_NO_MARKERS = (
        "XYScatter_LinesNoMarkers"  # Indicates the XYScatter_LinesNoMarkers chart type.
    )


class ChartBorder(CustomBaseModel):
    AutoFormat: Optional[bool] = None
    BeginArrowSize: Optional[ChartArrowSize] = None
    BeginArrowType: Optional[ChartArrowType] = None
    ColorIndex: Optional[ChartKnownColors] = None
    EndArrowSize: Optional[ChartArrowSize] = None
    EndArrowType: Optional[ChartArrowType] = None
    IsAutoLineColor: Optional[bool] = None
    LineColor: Optional[str] = None
    LinePattern: Optional[ChartLinePattern] = None
    LineWeight: Optional[ChartLineWeight] = None
    Transparency: Optional[float] = None


class ChartFill(CustomBaseModel):
    BackColor: Optional[str] = None
    BackColorIndex: Optional[ChartKnownColors] = None
    FillType: Optional[ChartFillType] = None
    ForeColor: Optional[str] = None
    ForeColorIndex: Optional[ChartKnownColors] = None
    GradientColorType: Optional[ChartGradientColor] = None
    GradientDegree: Optional[float] = None
    GradientStyle: Optional[ChartGradientStyle] = None
    GradientVariant: Optional[ChartGradientVariants] = None
    Picture: Optional[str] = None
    PictureName: Optional[str] = None
    Pattern: Optional[str] = None
    PresetGradientType: Optional[str] = None
    Transparency: Optional[float] = None
    TransparencyColor: Optional[float] = None
    TransparencyFrom: Optional[float] = None
    TransparencyTo: Optional[float] = None
    Visible: Optional[bool] = None


class ChartFillBorder(CustomBaseModel):
    Fill: Optional[ChartFill] = None
    LineProperties: Optional[ChartBorder] = None


class ChartGridLine(ChartFillBorder):
    Border: Optional[ChartBorder] = None


class ChartFont(CustomBaseModel):
    Bold: Optional[bool] = None
    Color: Optional[ChartKnownColors] = None
    FontName: Optional[str] = None
    Italic: Optional[bool] = None
    MacOSOutlineFont: Optional[bool] = None
    MacOSShadow: Optional[bool] = None
    RGBColor: Optional[str] = None
    Size: Optional[float] = None
    Strikethrough: Optional[bool] = None
    Subscript: Optional[bool] = None
    Superscript: Optional[bool] = None
    Underline: Optional[ChartUnderline] = None
    VerticalAlignment: Optional[ChartFontVerticalAlignment] = None


class ChartManualLayout(CustomBaseModel):
    Height: Optional[float] = None
    Top: Optional[float] = None
    Left: Optional[float] = None
    Width: Optional[float] = None
    HeightMode: Optional[ChartLayoutModes] = None
    TopMode: Optional[ChartLayoutModes] = None
    LeftMode: Optional[ChartLayoutModes] = None
    WidthMode: Optional[ChartLayoutModes] = None
    LayoutTarget: Optional[ChartLayoutTargets] = None


class ChartLayout(CustomBaseModel):
    Height: Optional[float] = None
    Top: Optional[float] = None
    Left: Optional[float] = None
    Width: Optional[float] = None
    HeightMode: Optional[ChartLayoutModes] = None
    TopMode: Optional[ChartLayoutModes] = None
    LeftMode: Optional[ChartLayoutModes] = None
    WidthMode: Optional[ChartLayoutModes] = None
    ManualLayout: Optional[ChartManualLayout] = None
    LayoutTarget: Optional[ChartLayoutTargets] = None


class ChartFrameFormat(ChartFillBorder):
    Border: Optional[ChartBorder] = None
    IsBorderCornersRound: Optional[bool] = None
    Layout: Optional[ChartLayout] = None


class ChartTextArea(ChartFont):
    FrameFormat: Optional[ChartFrameFormat] = None
    Layout: Optional[ChartLayout] = None
    Text: Optional[str] = None
    TextRotationAngle: Optional[int] = None


class ChartAxis(CustomBaseModel):
    AutoTickLabelSpacing: Optional[bool] = None
    Border: Optional[ChartBorder] = None
    Font: Optional[ChartFont] = None
    HasMajorGridLines: Optional[bool] = None
    HasMinorGridLines: Optional[bool] = None
    MajorGridLines: Optional[ChartGridLine] = None
    MinorGridLines: Optional[ChartGridLine] = None
    MajorTickMark: Optional[ChartTickMark] = None
    MinorTickMark: Optional[ChartTickMark] = None
    NumberFormat: Optional[str] = None
    ReversePlotOrder: Optional[bool] = None
    TextRotationAngle: Optional[int] = None
    TickLabelPosition: Optional[ChartTickLabelPosition] = None
    Title: Optional[str] = None
    TitleArea: Optional[ChartTextArea] = None
    Visible: Optional[bool] = None


class ChartValueAxis(ChartAxis):
    CrossesAt: Optional[float] = None
    DisplayUnit: Optional[ChartDisplayUnit] = None
    DisplayUnitCustom: Optional[float] = None
    DisplayUnitLabel: Optional[ChartTextArea] = None
    HasDisplayUnitLabel: Optional[bool] = None
    IsAutoCross: Optional[bool] = None
    IsAutoMajor: Optional[bool] = None
    IsAutoMax: Optional[bool] = None
    IsAutoMin: Optional[bool] = None
    IsAutoMinor: Optional[bool] = None
    IsLogScale: Optional[bool] = None
    IsMaxCross: Optional[bool] = None
    LogBase: Optional[float] = None
    MajorUnit: Optional[float] = None
    MaximumValue: Optional[float] = None
    MinimumValue: Optional[float] = None
    MinorUnit: Optional[float] = None


class ChartDataRange(CustomBaseModel):
    FirstColumn: Optional[int] = None
    FirstRow: Optional[int] = None
    LastColumn: Optional[int] = None
    LastRow: Optional[int] = None


class ChartCategoryAxis(ChartValueAxis):
    AutoTickLabelSpacing: Optional[bool] = None
    BaseUnit: Optional[ChartBaseUnit] = None
    BaseUnitIsAuto: Optional[bool] = None
    BinWidth: Optional[float] = None
    CategoryLabels: Optional[ChartDataRange] = None
    CategoryType: Optional[ChartCategoryType] = None
    HasAutomaticBins: Optional[bool] = None
    IsBetween: Optional[bool] = None
    IsBinningByCategory: Optional[bool] = None
    MajorUnitScale: Optional[ChartBaseUnit] = None
    MinorUnitScale: Optional[ChartBaseUnit] = None
    NoMultiLevelLabel: Optional[bool] = None
    NumberOfBins: Optional[int] = None
    Offset: Optional[int] = None
    OverflowBinValue: Optional[float] = None
    TickLabelSpacing: Optional[int] = None
    TickMarkSpacing: Optional[int] = None
    UnderflowBinValue: Optional[float] = None


class ChartSeriesAxis(ChartAxis):
    LabelFrequency: Optional[int] = None
    TickLabelSpacing: Optional[int] = None
    TickMarkSpacing: Optional[int] = None


class ChartLegendEntry(CustomBaseModel):
    IsDeleted: Optional[bool] = None
    IsFormatted: Optional[bool] = None
    TextArea: Optional[ChartTextArea] = None


class ChartLegend(CustomBaseModel):
    FrameFormat: Optional[ChartFrameFormat] = None
    IncludeInLayout: Optional[bool] = None
    IsVerticalLegend: Optional[bool] = None
    Layout: Optional[ChartLayout] = None
    TextArea: Optional[ChartTextArea] = None
    Position: Optional[ChartLegendPosition] = None
    LegendEntries: List[ChartLegendEntry] = []
    X: Optional[int] = None
    Y: Optional[int] = None


class ChartSerieDataFormat(ChartFillBorder):
    pass


class ChartDataLabels(ChartTextArea, ChartFont):
    Delimiter: Optional[str] = None
    IsBubbleSize: Optional[bool] = None
    IsCategoryName: Optional[bool] = None
    IsLegendKey: Optional[bool] = None
    IsPercentage: Optional[bool] = None
    IsSeriesName: Optional[bool] = None
    IsValue: Optional[bool] = None
    IsValueFromCells: Optional[bool] = None
    NumberFormat: Optional[str] = None
    Position: Optional[ChartDataLabelPosition] = None
    ShowLeaderLines: Optional[bool] = None
    ValueFromCellsRange: Optional[ChartDataRange] = None


class ChartDataPoint(CustomBaseModel):
    DataFormat: Optional[ChartSerieDataFormat] = None
    DataLabels: Optional[ChartDataLabels] = None
    SetAsTotal: Optional[bool] = None
    IsDefaultmarkertype: Optional[bool] = None


class ChartSerie(CustomBaseModel):
    Bubbles: Optional[ChartDataRange] = None
    CategoryLabels: ChartDataRange
    DataPoints: Optional[List[ChartDataPoint]] = None
    DefaultDataPoint: Optional[ChartDataPoint] = None
    IsFiltered: Optional[bool] = None
    Name: str
    SerieFormat: Optional[ChartSerieDataFormat] = None
    SerieType: ChartType
    UsePrimaryAxis: Optional[bool] = None
    Values: ChartDataRange


class Chart(CustomBaseModel):
    AutoScaling: Optional[bool] = None
    ChartArea: Optional[ChartFrameFormat] = None
    ChartData: List[List[str]]
    ChartTitle: Optional[str] = ""
    ChartTitleArea: Optional[ChartTextArea] = None
    HasDataTable: Optional[bool] = None
    HasLegend: Optional[bool] = None
    HasPlotArea: Optional[bool] = None
    Height: float
    Top: float
    Left: float
    HeightPercent: Optional[int] = None
    Legend: Optional[ChartLegend] = None
    PlotArea: Optional[ChartFrameFormat] = None
    PlotVisibleOnly: Optional[bool] = None
    PrimaryCategoryAxis: Optional[ChartCategoryAxis] = None
    PrimarySerieAxis: Optional[ChartSeriesAxis] = None
    PrimaryValueAxis: Optional[ChartValueAxis] = None
    RightAngleAxes: Optional[bool] = None
    Series: List[ChartSerie]
    SecondaryCategoryAxis: Optional[ChartCategoryAxis] = None
    SecondaryValueAxis: Optional[ChartValueAxis] = None
    Width: float
    XPos: Optional[float] = None
    YPos: Optional[float] = None
