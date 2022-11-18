import argparse
import logging

from itolhelper.datasets.config import DatasetConfig
from itolhelper.datasets.branch_symbols import generate_branch_symbols
from itolhelper.io import read_ids

logger = logging.getLogger(__name__)


def branch_symbols(args: argparse.Namespace):
    ids = read_ids(args.ids)
    logger.debug(ids)
    with open(args.config) as f:
        config = DatasetConfig.load_config(f)
    logger.debug(config)

    print(generate_branch_symbols(ids, config, args.label))