import os
from enum import Enum
from pathlib import Path
from typing import List, Union

import newick
from Bio import SeqIO

PathLike = Union[Path, str]


class FileType(Enum):
    txt = "txt"
    fasta = "fasta"
    phy = "phy"
    nwk = "newick"

    @staticmethod
    def detect(path: Path) -> "FileType":
        fasta_exts = [".fa", ".fasta", ".faa"]
        txt_exts = [".txt"]
        phy_exts = [".phy"]
        nwk_exts = [".newick", ".nwk", ".support", ".tree"]

        _, ext = os.path.splitext(path)

        if ext in fasta_exts:
            return FileType.fasta
        elif ext in txt_exts:
            return FileType.txt
        elif ext in phy_exts:
            return FileType.phy
        elif ext in nwk_exts:
            return FileType.nwk
        else:
            raise ValueError(f"Invalid extension: {path}")


def _read_ids_from_fasta(path: Path) -> List[str]:
    ids = []
    with open(path) as f:
        for rec in SeqIO.parse(f, format="fasta"):
            ids.append(rec.id)
    return ids


def _read_ids_from_newick(path: Path) -> List[str]:
    return [node.name for node in newick.read(path)]


def _read_ids_from_phy(path: Path) -> List[str]:
    ids = []
    with open(path) as f:
        # skip first line
        f.readline()

        for line in f:
            id, _ = line.strip().split(" ")
            ids.append(id)
    return ids


def _read_ids_from_txt(path: Path) -> List[str]:
    ids = []
    with open(path) as f:
        for line in f:
            ids.append(line.strip())

    return ids


def read_ids(path: PathLike) -> List[str]:
    if isinstance(path, str):
        path = Path(path)

    file_type = FileType.detect(path)

    match file_type:
        case FileType.fasta:
            ids = _read_ids_from_fasta(path)
        case FileType.phy:
            ids = _read_ids_from_phy(path)
        case FileType.txt:
            ids = _read_ids_from_txt(path)
        case FileType.nwk:
            ids = _read_ids_from_newick(path)

    return ids
