# Resources Catalog: Talkie Generalization Research

## Summary
This catalog lists the models, datasets, and literature gathered to test the hypothesis that Talkie's sparse 1930-cutoff training data makes it easier to verify generalization.

## Models
| Name | Source | Description | Location |
|------|--------|-------------|----------|
| Talkie-1930-13b-it | talkie-lm/HuggingFace | Instruction-tuned 1930-cutoff LLM. | `talkie-lm/talkie-1930-13b-it` |
| Talkie-1930-13b-base | talkie-lm/HuggingFace | Base completion model (1930 cutoff). | `talkie-lm/talkie-1930-13b-base` |

## Datasets
| Name | Source | Size | Task | Location |
|------|--------|------|------|----------|
| Gutenberg Time | community-datasets/HF | ~50K books | Historical text with temporal metadata. | `community-datasets/gutenberg_time` |
| HumanEval | openai/HF | 164 tasks | Coding generalization (post-1930 concept). | `openai/humaneval` |
| MMLU | cais/HF | 57 tasks | General knowledge (can be filtered for temporal facts). | `cais/mmlu` |

## Key Literature
| Title | Authors | Year | Relevance |
|-------|---------|------|-----------|
| Talkie Technical Report | Radford et al. | 2026 | Primary source for the model and reasoning experiments. |
| GPT and Prejudice | Mahran & Simbeck | 2025 | Study of sparse historical representations. |
| On the Limits of LLM Reasoning | Salido et al. | 2025 | Methodology for disentangling reasoning from memorization. |
| Can LLMs Represent the Past... | Underwood et al. | 2025 | Importance of period pre-training. |

## Recommendations for Experiment Design
1. **Zero-Shot/Few-Shot Modern Tasks**: Test Talkie on HumanEval (Python). Since it has zero pre-1931 knowledge of Python, any success is a strong signal of logic generalization.
2. **Temporal Reasoning**: Compare Talkie's performance on MMLU questions about pre-1930 history vs. post-1930 history.
3. **Surprisingness Analysis**: Measure the perplexity of modern text vs. historical text to quantify the "knowledge gap."

## Search Strategy Notes
- Initial searches for "Talkie" were successful once the 2026 release date was identified.
- The "Living with Machines" project at the Alan Turing Institute is a major hub for historical LLM research.
