# Talkie Generalization Research

Does the sparse, 1930-cutoff training data of Talkie make it easier to test for generalization?

## Key Findings
- **Zero-Shot Gap**: Talkie-1930 fails 0-shot coding tasks but succeeds 3-shot, providing a "pure" signal of logic generalization without contamination.
- **Temporal Cliff**: A distinct performance boundary exists between pre-1930 and post-1930 MMLU categories, making the model a reliable scientific instrument.
- **Sparsity-as-Signal**: Sparsity reduces the "noise" of memorized modern knowledge, making the "bridge" of generalization easier to isolate and measure.

## Project Structure
- `src/`: Python scripts for experiments (`run_experiments.py`, `run_comparison.py`).
- `results/`: JSON files with raw experimental data.
- `figures/`: Visualizations of the "Generalization Signal" and "Temporal Cliff".
- `REPORT.md`: Full research paper detailing methodology and findings.

## How to Reproduce
1. **Setup Environment**:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt # or install manually from src/run_experiments.py imports
   ```
2. **Download Models**:
   ```bash
   python src/setup_data.py
   ```
3. **Run Experiments**:
   ```bash
   python src/run_comparison.py
   ```
4. **Generate Plots**:
   ```bash
   python src/visualize.py
   ```

## Requirements
- Python >= 3.11
- CUDA GPU with >= 28 GB VRAM (for 13B model inference)
- ~80 GB disk space (for models and datasets)
