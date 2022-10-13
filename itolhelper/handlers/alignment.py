import argparse
import logging

from itolhelper.datasets.alignment import generate_alignment
from itolhelper.datasets.config import DatasetConfig
from itolhelper.io import read_seq_records

logger = logging.getLogger(__name__)


def alignment(args: argparse.Namespace):
    recs = read_seq_records(args.input)
    logger.debug(recs)

    print(generate_alignment(recs, args.label))
