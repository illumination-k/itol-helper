import json
import logging
from io import BytesIO, StringIO, TextIOWrapper
from pathlib import Path
from typing import Dict, Pattern, Union

from pydantic import BaseModel
from pydantic.color import Color

logger = logging.getLogger(__name__)


class ColorMap(BaseModel):
    default_color: Color = Color("black")
    map: Dict[Pattern, Color]

    def get_color(self, value: str) -> str:
        logger.debug(f"KEY: {value}")
        default_color = self.default_color.as_hex()

        for pat, color in self.map.items():
            logger.debug(f"pattern: {str(pat)}, value: {color}")
            if pat.match(value) is not None:
                return color.as_hex()

        return default_color


class DatasetConfig(BaseModel):
    colormap: ColorMap
    id_to_name: Dict[str, str]

    @staticmethod
    def load_config(config: Union[TextIOWrapper, StringIO, BytesIO]) -> "DatasetConfig":
        _config = json.load(config)

        # default color is black
        default_color = _config.get("default_color", "#000000")
        id_to_name = _config.get("id_to_name", {})

        _map: dict[str, str] = _config.get("colormap", {})
        map = {k: Color(v) for k, v in _map.items()}
        colormap = ColorMap(map=map, default_color=default_color)

        return DatasetConfig(colormap=colormap, id_to_name=id_to_name)

    @staticmethod
    def from_path(path: Union[str, Path]) -> "DatasetConfig":
        with open(path) as f:
            config = DatasetConfig.load_config(f)

        return config
