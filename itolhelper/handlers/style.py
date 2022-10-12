import argparse
import logging

from itolhelper.datasets.config import DatasetConfig
from itolhelper.datasets.style import generate_style
from itolhelper.io import read_ids

logger = logging.getLogger(__name__)


def style(args: argparse.Namespace):
    ids = read_ids(args.ids)
    logger.debug(ids)
    with open(args.config) as f:
        config = DatasetConfig.load_config(f)
    logger.debug(config)

    print(generate_style(ids, config, args.label))
