# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT committed to git due to size. Follow the download instructions below.

## Dataset 1: Gutenberg Time
- **Source**: [community-datasets/gutenberg_time](https://huggingface.co/datasets/community-datasets/gutenberg_time)
- **Size**: ~50,000 books
- **Format**: HuggingFace Dataset
- **Task**: Historical text analysis / training
- **Notes**: Contains metadata about publication years, useful for filtering to pre-1931.

### Download Instructions
```python
from datasets import load_dataset
dataset = load_dataset("community-datasets/gutenberg_time")
dataset.save_to_disk("datasets/gutenberg_time")
```

## Dataset 2: HumanEval
- **Source**: [openai/humaneval](https://huggingface.co/datasets/openai/humaneval)
- **Size**: 164 samples
- **Format**: JSONL / HuggingFace Dataset
- **Task**: Code generation generalization
- **Notes**: Used to test if Talkie can "invent" Python logic without having seen it in training.

### Download Instructions
```python
from datasets import load_dataset
dataset = load_dataset("openai/humaneval")
dataset.save_to_disk("datasets/humaneval")
```

## Dataset 3: MMLU (Massive Multitask Language Understanding)
- **Source**: [cais/mmlu](https://huggingface.co/datasets/cais/mmlu)
- **Task**: General knowledge and reasoning
- **Notes**: Can be filtered to compare performance on historical vs. modern subjects.

### Download Instructions
```python
from datasets import load_dataset
dataset = load_dataset("cais/mmlu", "all")
dataset.save_to_disk("datasets/mmlu")
```
