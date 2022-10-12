import argparse
import logging

from itolhelper.datasets.config import DatasetConfig
from itolhelper.datasets.text import generate_text
from itolhelper.io import read_ids

logger = logging.getLogger(__name__)


def text(args: argparse.Namespace):
    ids = read_ids(args.ids)
    logger.debug(ids)
    with open(args.config) as f:
        config = DatasetConfig.load_config(f)
    logger.debug(config)

    print(generate_text(ids, config, args.label))
