import abc
from pathlib import Path
from typing import Union


class ItolDatasetsImpl(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def from_path(
        path: Union[Path, str], config_path: Union[Path, str], label: str
    ) -> str:
        raise NotImplementedError
