import argparse
import logging
import os
import tempfile
import zipfile
from pathlib import Path
from typing import Any, List, Optional

import requests
from pydantic import BaseModel, Field, SecretStr

logger = logging.getLogger(__name__)


class UploadParams(BaseModel):
    APIkey: SecretStr = Field(alias="api_key")
    projectName: str = Field(alias="project_name")
    treeName: Optional[str] = Field(None, alias="tree_name")
    treeDescription: Optional[str] = Field(None, alias="tree_description")


class Uploader:
    def __init__(
        self,
        api_key: str,
        project_name: str,
        tree_name: Optional[str] = None,
        tree_description: Optional[str] = None,
    ) -> None:
        self.url = "https://itol.embl.de/batch_uploader.cgi"
        self.files: List[Path] = []
        self.params: UploadParams = UploadParams(
            api_key=api_key,
            project_name=project_name,
            tree_name=tree_name,
            tree_description=tree_description,
        )

    def add_file(self, path: Path) -> None:
        if not path.is_file():
            raise IOError(f"{str(path)} is not a file")

        self.files.append(path)

    def _prepare_zipfile(self) -> Any:
        assert len(self.files) != 0, "You must add a tree file!"

        temp = tempfile.NamedTemporaryFile()
        with zipfile.ZipFile(temp, "w") as w:
            for f in self.files:
                w.write(f, arcname=f.name)
        temp.flush()
        return temp

    def upload(self) -> None:
        with self._prepare_zipfile() as zip:
            zip_file = open(zip.name, "rb")
            files = {"zipFile": zip_file}
            resp = requests.post(self.url, data=self.params.dict(exclude_none=True), files=files)

            logger.debug(resp)
            zip_file.close()


def upload(args: argparse.Namespace) -> None:
    api_key = os.environ.get("ITOL_APIKEY")

    if args.api_key is not None:
        api_key = args.api_key

    if api_key is None:
        raise ValueError(
            "You should set an ITOL_APIKEY environmental variable or specify by --api-key"
        )

    uploader = Uploader(
        api_key=api_key,
        project_name=args.project_name,
        tree_name=args.tree_name,
        tree_description=args.tree_description,
    )

    for path in os.listdir(os.path.abspath(args.dir)):
        uploader.add_file(Path(path))

    logger.debug(uploader)

    uploader.upload()
