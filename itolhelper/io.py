import logging
import os
from enum import Enum
from pathlib import Path
from typing import List, Union

from Bio import SeqIO  # type: ignore
from Bio.Phylo import NewickIO  # type: ignore
from pydantic import BaseModel

logger = logging.getLogger(__name__)

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
    ids = []
    with open(path) as handle:
        for tree in NewickIO.parse(handle=handle):
            for clade in tree.get_terminals():
                ids.append(clade.name)
    return ids


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
    logger.debug(file_type)

    mapf = {
        FileType.fasta: _read_ids_from_fasta,
        FileType.phy: _read_ids_from_phy,
        FileType.nwk: _read_ids_from_newick,
        FileType.txt: _read_ids_from_txt,
    }

    read = mapf[file_type]
    ids = read(path)

    return ids


class SeqRecord(BaseModel):
    id: str
    seq: str


def _read_seqrecords_from_fasta(path: Path) -> List[SeqRecord]:
    recs = []
    with open(path) as f:
        for rec in SeqIO.parse(f, format="fasta"):
            recs.append(SeqRecord(id=rec.id, seq=str(rec.seq)))
    return recs


def _read_seqrecords_from_phy(path: Path) -> List[SeqRecord]:
    recs = []
    with open(path) as f:
        # skip first line
        f.readline()

        for line in f:
            id, seq = line.strip().split(" ")
            recs.append(SeqRecord(id=id.strip(), seq=seq.strip()))
    return recs


def read_seq_records(path: PathLike) -> List[SeqRecord]:
    if isinstance(path, str):
        path = Path(path)

    file_type = FileType.detect(path)
    logger.debug(file_type)

    if file_type == FileType.fasta:
        recs = _read_seqrecords_from_fasta(path)
    elif file_type == FileType.phy:
        recs = _read_seqrecords_from_phy(path)
    else:
        raise IOError("only support fasta and phy format")

    return recs
