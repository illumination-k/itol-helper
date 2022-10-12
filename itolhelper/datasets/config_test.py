import json
import re
import tempfile
from io import StringIO

from .config import DatasetConfig

colormap_config = """
{   
    "default_color": "black",
    "colormap": {
        "^Mp": "black",
        "^Pp": "green",
        "\\\d+": "sky"
    }
}
"""


def test_load_colormap_config():
    config = DatasetConfig.load_config(StringIO(colormap_config))
    assert re.compile("^Mp") in config.colormap.map
    assert re.compile("^Pp") in config.colormap.map
    assert re.compile("\\d+") in config.colormap.map

    assert config.colormap.get_color("Mp1g11000") == "black"
    assert config.colormap.get_color("Pp3c10_25160V3.1.p") == "green"
    assert config.colormap.get_color("11200") == "sky"


# Check read from path
def test_from_path():
    temp = tempfile.mktemp()
    with open(temp, "w") as w:
        w.write(colormap_config)

    DatasetConfig.from_path(temp)


id_to_name_config = json.dumps(
    {
        "id_to_name": {
            "Mp3g23300": "MpBNB",
        }
    }
)


def test_load_id_to_name_config():
    config = DatasetConfig.load_config(StringIO(id_to_name_config))
    assert config.id_to_name.get("Mp3g23300") == "MpBNB"
