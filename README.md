# Classifications of Open-Domain Queries for Tabular Data Analysis

This repository contains the code for the classifiers underlying the experiments in the paper ["Are We Asking the Right
Questions? On Ambiguity in Natural Language Queries for Tabular Data Analysis"](https://arxiv.org/abs/2511.04584), 
accepted at the AI for Tabular Data workshop at EurIPS 2025.


## Usage


### Setup

First, make sure to install the required dependencies. This repository provides requirements configurations that can be synced with `pip` or `uv`. 

Install requirements with `pip`:

```bash
pip install -r requirements.txt
```

**Or** syncing the [`uv`](https://docs.astral.sh/uv/) project:

```bash
uv sync
```

Since the classifiers leverage the OpenAI API, ensure you have your API key set up in your environment:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

### Running Classifiers

The classifiers can be run in a step-by-step manner in the respective notebooks:

- [`01_DataPrivilegeClassification.ipynb``](./01_DataPrivilegeClassification.ipynb): Classifies whether a query requires privileged data access.
- [`02_QuerySpecificationClassification.ipynb`](./02_QuerySpecificationClassification.ipynb): Classifies the specification of the query.

### Analysis and Visualization

The results of the classifiers are analyzed in the notebook [`03_Analysis.ipynb`](./03_Analysis.ipynb).

## Organization of the Repository

**Code for reproducing results:** Find the main code in the jupyter notebooks in the root directory.

**Shared Code:** Find the shared code for processing, classification, and prompt management in the [`common/`](./common) directory.

**Data:** Find the input, development, and output data in the [`data/`](./data) directory.

**Prompts:** Find the prompt templates used for classification in the [`prompts/`](./prompts) directory. In this directory you can also find a full history of the prompt engineering process in the `history` subdirectories.


## Citation

If you find this work useful in your research, please consider citing the following paper:

```bibtex
@inproceedings{gommAreWeAsking2025,
  title = {Are {{We Asking}} the {{Right Questions}}? {{On Ambiguity}} in {{Natural Language Queries}} for {{Tabular Data Analysis}}},
  shorttitle = {Are {{We Asking}} the {{Right Questions}}?},
  booktitle = {{{AI}} for {{Tabular Data}} Workshop at {{EurIPS}} 2025},
  author = {Gomm, Daniel and Wolff, Cornelius and Hulsebos, Madelon},
  year = 2025,
  url = {https://arxiv.org/abs/2511.04584}
}

