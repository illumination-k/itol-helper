import json
import logging
from pathlib import Path
from typing import Dict, Literal, Optional, Union

from ..io import read_ids
from . import ItolDatasetsImpl

logger = logging.getLogger(__name__)

TEMPLATE = """DATASET_STYLE
#Style datasets allow the customization of branch and leaf label colors and styles.
#lines starting with a hash are comments and ignored during parsing
#=================================================================#
#                    MANDATORY SETTINGS                           #
#=================================================================#
#select the separator which is used to delimit the data below (TAB,SPACE or COMMA).This separator must be used throughout this file.
#SEPARATOR TAB
#SEPARATOR SPACE
SEPARATOR COMMA
#label is used in the legend table (can be changed later)
DATASET_LABEL,@label@
#dataset color (can be changed later)
COLOR,#ffff00
#=================================================================#
#                    OPTIONAL SETTINGS                            #
#=================================================================#
#Each dataset can have a legend, which is defined using LEGEND_XXX fields below
#For each row in the legend, there should be one shape, color and label.
#Optionally, you can define an exact legend position using LEGEND_POSITION_X and LEGEND_POSITION_Y. To use automatic legend positioning, do NOT define these values
#Optionally, shape scaling can be present (LEGEND_SHAPE_SCALES). For each shape, you can define a scaling factor between 0 and 1.
#Shape should be a number between 1 and 6, or any protein domain shape definition.
#1: square
#2: circle
#3: star
#4: right pointing triangle
#5: left pointing triangle
#6: checkmark
#LEGEND_TITLE,Dataset legend
#LEGEND_POSITION_X,100
#LEGEND_POSITION_Y,100
#LEGEND_SHAPES,1,2,3
#LEGEND_COLORS,#ff0000,#00ff00,#0000ff
#LEGEND_LABELS,value1,value2,value3
#LEGEND_SHAPE_SCALES,1,1,0.5
#Internal tree nodes can be specified using IDs directly, or using the 'last common ancestor' method described in iTOL help pages
#=================================================================#
#       Actual data follows after the "DATA" keyword              #
#=================================================================#
#the following fields are required for each node:
#ID,TYPE,WHAT,COLOR,WIDTH_OR_SIZE_FACTOR,STYLE,BACKGROUND_COLOR
# TYPE: can be either 'branch' or 'label'. 'branch' will apply customizations to the tree branches, while 'labels' apply to the leaf text labels
# WHAT: can be either 'node' or 'clade', only relevant for internal tree nodes. 'Node' will apply the customization only to a single node, while 'clade' will apply to all child nodes as well.
# COLOR: can be in hexadecimal, RGB or RGBA notation. If RGB or RGBA are used, dataset SEPARATOR cannot be comma.
# WIDTH_OR_SIZE_FACTOR: for type 'branch', specifies the relative branch width, compared to the global branch width setting.
#                       for type 'label', specifies the relative font size, compared to the global font size
# STYLE: for type 'branch', can be either 'normal' or 'dashed'
#        for type 'label', can be one of 'normal', 'bold', 'italic' or 'bold-italic'
# BACKGROUND_COLOR (optional): only relevant for type 'label', specifies the color of the label background. The value is optional.
DATA
#Examples
#a single internal node's branch will be colored red with double branch width and dashed line
#9606|184922,branch,node,#ff0000,2,dashed
#node 9606 will have its label displayed in blue with bold italic font, and with yellow background
#9606,label,node,#0000ff,1,bold-italic,#ffff00
#a clade starting at internal node 2190|2287 will have all its branches colored green
#2190|2287,branch,clade,#00ff00,1,normal
#all leaf labels in a clade will be displayed in red
#2097|1502,label,clade,#ff0000,1,normal
"""

Type = Literal["branch", "label"]
What = Literal["node", "clade"]


def create_data(
    id: str,
    color: str,
    type: Type = "label",
    what: What = "node",
    width_or_size_factor: int = 1,
    style: str = "normal",
    background_color: Optional[str] = None,
) -> str:
    data = f"{id},{type},{what},{color},{str(width_or_size_factor)},{style}"
    if background_color is not None:
        if type != "label":
            logger.warn(
                "background color can set if you set type as label. skip background color."
            )
        else:
            data += f",{background_color}"

    return data


class Colormap:
    def __init__(self, map: Dict[str, str], default_color="black") -> None:
        import re

        self.default_color = default_color
        self.colormap: Dict[re.Pattern, str] = {}
        for k, v in map.items():
            self.colormap.setdefault(re.compile(k), v)

    def get_color(self, value: str) -> str:
        color = self.default_color

        for pat, v in self.colormap.items():
            if pat.match(value) is not None:
                return v

        return color


class StyleGenerator(ItolDatasetsImpl):
    @staticmethod
    def from_path(
        path: Union[Path, str], config_path: Union[Path, str], label: str
    ) -> str:
        with open(config_path) as f:
            config = json.load(f)

            default_color = config.get("default_color", "black")
            map = config.get("colormap", {})

            colormap = Colormap(map=map, default_color=default_color)

        template = [TEMPLATE.replace("@label@", label)]

        ids = read_ids(path)

        for id in ids:
            template.append(create_data(id=id, color=colormap.get_color(id)))

        return "\n".join(template)
