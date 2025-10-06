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

    def save(self, path: PathLike) -> None:
        if not str(path).endswith(".json"):
            raise ValueError("Prompt has to be saves as \".json\" file.")
        Path(path).parent.mkdir(parents=True, exist_ok=True)

        with open(path, 'w+') as f:
            f.write(self.model_dump_json(indent=4))

    @classmethod
    def load(cls, path: PathLike) -> Self:
        with open(path, 'r') as f:
            return Prompt.model_validate_json(f.read())

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\n\nMessages:\n{"\n".join([f"Role: {m.role}\nContent:\n{m.content}" for m in self.prompt_template.messages])}"

