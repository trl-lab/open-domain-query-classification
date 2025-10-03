from os import PathLike
from pathlib import Path
from typing import List, Optional, Self

from pydantic import BaseModel

from openbatch import PromptTemplate, ResponsesRequest


class Prompt(BaseModel):
    name: str
    description: str
    results: List[str]
    observations: Optional[str]
    prompt_template: PromptTemplate
    common_request: ResponsesRequest

    def to_file(self, path: PathLike) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)

        with open(path, 'w+') as f:
            f.write(self.model_dump_json(indent=4))

    @classmethod
    def from_file(cls, path: PathLike) -> Self:
        with open(path, 'r') as f:
            return Prompt.model_validate_json(f.read())

