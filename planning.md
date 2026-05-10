# Research Planning: Is it easier to test if Talkie generalizes?

## Motivation & Novelty Assessment

### Why This Research Matters
Data contamination is the "silent killer" of LLM evaluation. As models are trained on increasingly large portions of the internet, finding truly "unseen" tasks to test generalization becomes nearly impossible. This research explores whether a model with a strict historical cutoff (1930) and a sparser training corpus provides a superior scientific instrument for measuring "pure" generalization—the ability to apply learned structural patterns to entirely novel domains (e.g., modern programming, post-war science).

### Gap in Existing Work
Most generalization research focuses on modern models and attempts to "de-contaminate" them or use synthetic tasks. Using a historically-grounded model like Talkie-1930 as a "zero-contamination" benchmark is a relatively new approach. Specifically, the idea that *sparsity* itself (the lack of broad, modern "human experience" in the data) makes generalization *easier to verify* has not been rigorously tested against a modern-data baseline.

### Our Novel Contribution
We will empirically test the "Sparsity-as-Signal" hypothesis. We will compare Talkie-1930's performance on tasks it *cannot* have memorized (post-1930 knowledge) against its performance on pre-1930 knowledge, and contrast this "gap" with a modern model's performance. We aim to show that the "cliff" in performance for Talkie is much sharper and more predictable, making the "bridge" of generalization easier to isolate and measure.

### Experiment Justification
- **Experiment 1: Zero-Shot vs. Few-Shot Coding (HumanEval)**
  - *Why needed?*: Python was created in 1991. Talkie has 0% contamination. If it can code after few-shot prompting, it is the most robust proof of logic generalization possible. Modern models might just be "reciting" HumanEval.
- **Experiment 2: Temporal Knowledge Cliff**
  - *Why needed?*: To verify the "sparsity" and "cutoff" are actually functional. We test MMLU questions filtered by "Pre-1930" and "Post-1930" dates.
- **Experiment 3: Analogical Generalization (Anachronism)**
  - *Why needed?*: Can Talkie reason about a "digital computer" by drawing analogies to "difference engines" or "human computers"? This tests if sparse data forces the model to use more abstract, generalized representations.

---

## Research Question
Does the sparse, historically-limited training data of Talkie-1930 make it easier (more scientifically rigorous/detectable) to test for generalization compared to modern, dense-data models?

## Hypothesis Decomposition
1. **H1 (Contamination-Free):** Talkie-1930 has zero exposure to post-1930 technical concepts, making any performance on them a "pure" measure of generalization.
2. **H2 (Sparsity Benefit):** The sparser training data of 1930 results in a more discrete knowledge boundary, making the "signal" of generalization (when it happens) more distinct from the "noise" of memorization.
3. **H3 (Detectability):** The delta between zero-shot (failure) and few-shot (success) on modern tasks is larger and more consistent in Talkie than in modern models, facilitating easier measurement of the "generalization coefficient."

## Proposed Methodology

### Approach
We will use a comparative framework between `talkie-1930-13b-it` and a modern baseline (either `talkie-web-13b-base` if accessible, or a similar-scale modern model).

### Experimental Steps
1. **Setup**: Install `talkie` library and dependencies.
2. **Benchmark 1 (Coding)**: Run HumanEval on Talkie-1930 (0, 1, 3, 5 shots).
3. **Benchmark 2 (MMLU Temporal)**: Filter MMLU for pre-1930 and post-1930 questions. Compare performance drop-off.
4. **Benchmark 3 (Structural Analogies)**: Test Talkie's ability to explain modern concepts using only pre-1930 vocabulary and concepts.

### Evaluation Metrics
- **Accuracy (Pass@1)** for HumanEval.
- **Performance Gap (Delta)**: (Post-1930 Score) / (Pre-1930 Score).
- **Few-shot Gain**: The rate of improvement per example for "unseen" vs "seen" domains.

### Statistical Analysis Plan
- T-tests to compare the "generalization slope" (few-shot gain) between Talkie and Modern models.
- Correlation analysis between task "modernity" and performance drop-off.

## Expected Outcomes
- Talkie will fail HumanEval 0-shot but show a non-zero (though likely low) success rate with 5-shot prompts, proving generalization.
- The "Temporal Cliff" in MMLU will be significantly steeper for Talkie than for modern models.
- The "easiness" of testing generalization will be evidenced by the clear, binary-like transition from "no knowledge" to "reasoned application" in Talkie.

## Timeline and Milestones
- **Phase 2 (Setup)**: 30m
- **Phase 3 (Implementation)**: 1h
- **Phase 4 (Experiments)**: 2h
- **Phase 5 (Analysis)**: 1h
- **Phase 6 (Reporting)**: 1h

## Success Criteria
- Successful reproduction of Talkie's "logic generalization" on at least one post-1930 task.
- Quantifiable evidence that the "generalization signal" is cleaner in Talkie due to the absence of contamination.
