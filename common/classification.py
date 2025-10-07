import json
from typing import Iterable, List, TypeVar, Tuple

from openai.types import Batch
from openbatch import PromptTemplateInputInstance, BatchJobManager

from openai import OpenAI
from pydantic import BaseModel

from common.model import Prompt

T = TypeVar("T", bound=BaseModel)


def create_input_instances(queries: Iterable[str], ids: Iterable[str]) -> List[PromptTemplateInputInstance]:
    instances = []
    for query, id in zip(queries, ids):
        instances.append(PromptTemplateInputInstance(id=id, prompt_value_mapping={"query": query}))
    return instances



def create_batch_file(prompt: Prompt, instances: Iterable[PromptTemplateInputInstance], batch_file_path: str) -> None:
    BatchJobManager().add_templated_instances(prompt.prompt_template, common_request=prompt.common_request,
                                    input_instances=instances, save_file_path=batch_file_path)


def start_batch_job(batch_file_path: str) -> Batch:
    client = OpenAI()
    batch_file = client.files.create(file=open(batch_file_path, "rb"), purpose="batch")
    batch_job = client.batches.create(input_file_id=batch_file.id, endpoint="/v1/responses", completion_window="24h")
    return batch_job


def retrieve_batch_results(batch: Batch, classification_target: type[T]) -> Tuple[List[str], List[T]]:
    client = OpenAI()
    batch = client.batches.retrieve(batch_id=batch.id)
    if batch.output_file_id is None:
        raise RuntimeError("Batch job has not completed yet.")

    batch_output = client.files.content(file_id=batch.output_file_id)
    parsed_output = [json.loads(l) for l in batch_output.text.strip().split("\n")]

    ids = [item["custom_id"] for item in parsed_output]
    classifications = [classification_target.model_validate_json(item['response']['body']['output'][1]['content'][0]['text']) for item in parsed_output]

    return ids, classifications

