import abc
from pathlib import Path
from typing import Union


class ItolDatasetsImpl(abc.ABC):
    @abc.abstractmethod
    def template(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def from_path(path: Union[Path, str], config: Union[Path, str], label: str) -> str:
        raise NotImplementedError
