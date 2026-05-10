# Literature Review: Generalization in Historical LLMs (Talkie-1930)

## Research Area Overview
The study of generalization in Large Language Models (LLMs) often faces challenges due to data contamination, where evaluation benchmarks are present in the massive web-scale training data. Historical language models, particularly those with a strict temporal cutoff (like the 1930 cutoff in the Talkie project), provide a unique "contamination-free by construction" environment. This allows researchers to test whether a model's performance on modern tasks (e.g., coding, post-1930 science) is due to genuine reasoning and abstract pattern generalization or simply memorization.

## Key Papers

### 1. Talkie: A 13B Vintage Language Model from 1930
- **Authors**: Alec Radford, Nick Levine, David Duvenaud (Project lead)
- **Year**: 2026
- **Source**: talkie-lm.com / Technical Report
- **Key Contribution**: Released Talkie-1930, a 13B parameter model trained on 260B tokens of pre-1931 text.
- **Methodology**: Strict data filtering by publication date. Instruction-tuning using historical reference works (etiquette manuals, encyclopedias).
- **Results**: Demonstrated "capability emergence" in modern tasks like Python coding and understanding post-1930 scientific concepts when provided with brief in-context examples.
- **Relevance**: Central to the research hypothesis. It provides the empirical base for testing generalization without contamination.

### 2. GPT and Prejudice: A Sparse Approach to Understanding Learned Representations in LLMs
- **Authors**: Mariam Mahran, Katharina Simbeck
- **Year**: 2025
- **Source**: arXiv (2025)
- **Key Contribution**: Analyzed learned representations in a model trained on 19th-century novels.
- **Methodology**: Coupled LLMs with Sparse Autoencoders (SAEs) to trace thematic encoding.
- **Results**: Identified stable "thematic backbones" around gender and kinship that exist even in sparse historical data.
- **Relevance**: Supports the idea that historical data has structured "backbones" that can serve as a foundation for generalization.

### 3. On the Limits of LLM Reasoning: Evidence From Contamination, Translation, and Answer Modification
- **Authors**: E. Salido, Julio Gonzalo, Guillermo Marco
- **Year**: 2025
- **Source**: arXiv (2025)
- **Key Contribution**: Proposed "Answer Modification" (e.g., "None of the other answers") to disentangle reasoning from memorization.
- **Results**: Accuracy drops significantly when answer patterns are modified, highlighting the fragility of current LLM "reasoning."
- **Relevance**: Provides a methodology for testing whether Talkie's generalization is robust or merely pattern-matching.

### 4. Can Language Models Represent the Past without Anachronism?
- **Authors**: Ted Underwood, Laura K. Nelson, Matthew Wilkens
- **Year**: 2025
- **Source**: arXiv (2025)
- **Key Contribution**: Evaluated the risk of anachronism in LLMs simulated to be historical.
- **Results**: Found that pre-training on period prose is superior to prompting or fine-tuning modern models for simulating historical perspectives.
- **Relevance**: Validates the Talkie approach of pre-training from scratch on period data.

## Common Methodologies
- **Temporal Cutoff Filtering**: Ensuring training data does not exceed a specific date (e.g., Dec 31, 1930).
- **Anachronism Benchmarking**: Testing models on concepts they could not have seen (e.g., Python, DNA, Turing machines).
- **In-Context Learning (ICL) for Modern Tasks**: Providing the model with a few modern examples in the prompt to see if it can adapt its "vintage" knowledge.

## Gaps and Opportunities
- **Sparsity vs. Scale**: Does sparser data (1930 cutoff) actually make generalization "easier" to test, or does it just make the model less capable overall?
- **Cross-Era Generalization**: How well do linguistic structures from 1930 map to modern technical logic?

## Recommendations for Our Experiment
- **Dataset**: Use `community-datasets/gutenberg_time` to extract more specific 1930-cutoff data if needed.
- **Model**: Evaluate `talkie-lm/talkie-1930-13b-it`.
- **Benchmark**: Use HumanEval and a modified version of MMLU filtered for "post-1930" knowledge vs. "pre-1930" knowledge.
