# Implementation, Training and Optimization of LLMs for Automated API Fuzzing on Heterogeneous GPUs

This repository contains the complete set of executable Jupyter Notebooks, HTML execution logs, and the final compiled report for the Graduation Project (Project III).

## Author
* **Student:** Tran Duy Gia Long (ID: 22071106)
* **Instructor:** Dr. Kim Dinh Thai
* **Major:** Applied Information Technology (Network Security)

## Repository Structure
This repository holds 27 executable Jupyter Notebooks (`.ipynb`) and 4 HTML execution logs (`.html`) representing the offline Colab and Blackwell experiment iterations, structured as follows:

### 1. SFT Training & Fine-Tuning
* `gemma4_12b_lora_ddp_training_blackwell.ipynb` (and its `.html` log): Interactive notebook executing the LoRA DDP fine-tuning run on 2x Blackwell GPUs in Snowflake.
* `github_issue_crawler_2024_2026.ipynb` & `github_issue_dataset_builder.ipynb`: Data collection, preprocessing, and training/validation/testing split compilation.

### 2. Inference & Serving Benchmarks
* `gemma4_12b_inference_benchmark_blackwell.html`: Evaluation of Gemma4 12B token generation throughput on Blackwell GPUs under various configurations (Unsloth vs. SDPA vs. Static KV Cache).
* `gemma4_e2b_t4_inference_bench.ipynb` & `gemma4_e4b_mtp_assistant_bench.ipynb`: Benchmark runs on speculative decoding, assistant drafts, and backend engines.

### 3. Program Prover & Certified Oracles (Fuzzer Engine)
* `gemma4_12b_program_prover_fuzzer_t4.ipynb` (and its `.html` log): T4-optimized program-prover execution conducting base-vs-fine-tuned differential sampling and execution-gate evaluation on Colab.
* `gemma4_program_prover_fuzzer_v5.ipynb` & `gemma4_program_prover_fuzzer_v5.html`: Program-prover implementation with GPU execution checks.
* `tensor_program_prover_v4.ipynb` & `tensor_program_prover_v5_t4.ipynb`: Certified oracle prover with program-level Wilkinson-Higham bounds.

### 4. Differential Fuzzing Loop & Subprocess Hunters
* `common_gpu_fuzzer.ipynb`: Common-GPU fuzzer probing linalg, sparse, indexing, and storage lifecycle surfaces.
* `framework_crash_fuzzer_engine.ipynb` & `pytorch_subprocess_crash_hunter.ipynb`: Subprocess-isolated offline crash hunter and fuzzer engine.
* `numerical_reliability_fuzz_ultimate.ipynb` & `numerical_reliability_fuzzer_ultimate.ipynb`: Full-scale numerical reliability fuzz run.

---

## Final Report
The final compiled PDF report is available in this repository as:
* [final_report.pdf](./final_report.pdf)
