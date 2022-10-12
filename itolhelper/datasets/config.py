import json
import logging
from io import BytesIO, StringIO, TextIOWrapper
from pathlib import Path
from typing import Dict, Optional, Pattern, Union

from pydantic import BaseModel

logger = logging.getLogger(__name__)

class ColorMap(BaseModel):
    default_color: str = "black"
    map: Dict[Pattern, str]

    def get_color(self, value: str) -> str:
        logger.debug(f"KEY: {value}")
        color = self.default_color

        for pat, v in self.map.items():
            logger.debug(f"pattern: {str(pat)}, value: {v}")
            if pat.match(value) is not None:
                return v

        return color


class DatasetConfig(BaseModel):
    colormap: ColorMap
    id_to_name: Dict[str, str]

    @staticmethod
    def load_config(config: Union[TextIOWrapper, StringIO, BytesIO]) -> "DatasetConfig":
        _config = json.load(config)

        default_color = _config.get("default_color", "black")
        map = _config.get("colormap", {})
        id_to_name = _config.get("id_to_name", {})

        colormap = ColorMap(map=map, default_color=default_color)

        return DatasetConfig(colormap=colormap, id_to_name=id_to_name)

    @staticmethod
    def from_path(path: Union[str, Path]) -> "DatasetConfig":
        with open(path) as f:
            config = DatasetConfig.load_config(f)

        return config
