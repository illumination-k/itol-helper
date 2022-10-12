import argparse

from itolhelper.datasets.config import DatasetConfig
from itolhelper.datasets.text import generate_text
from itolhelper.io import read_ids


def text(args: argparse.Namespace):
    ids = read_ids(args.ids)

    with open(args.config) as f:
        config = DatasetConfig.load_config(f)

    print(generate_text(ids, config, args.label))
