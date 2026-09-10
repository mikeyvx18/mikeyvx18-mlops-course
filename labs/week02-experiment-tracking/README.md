# Week 02 Lab

Instrument a provided training script (`train.py`) with MLflow experiment tracking; log params, metrics, and artifacts across a few runs, then compare them in the MLflow UI.

Starter files for this week's lab are pulled into your repo via `git fetch upstream && git merge upstream/main`, as introduced in the Week 1 lab.
## Reflection

### 1. Which run performed best, and how much better was it than the baseline?

The run with `n_estimators=200` and `max_depth=None` performed the best, achieving an accuracy of 0.9694. The baseline run with `n_estimators=10` and `max_depth=3` achieved an accuracy of 0.8306. Therefore, the best run improved accuracy by approximately 13.88 percentage points compared with the baseline.

### 2. Why do you think those hyperparameters won?

The `n_estimators=200` and `max_depth=None` configuration performed best because the Random Forest used more decision trees and allowed the trees to grow without a specified maximum depth. Using more trees can improve the stability and generalization of the ensemble, while allowing greater tree depth gives the model more flexibility to learn patterns in the digits dataset.

### 3. Which reproducibility leg does MLflow cover that a bare script did not?

MLflow helps cover the configuration leg of reproducibility that a bare training script does not capture as clearly. It records the hyperparameters used for each run, the resulting metrics, and the confusion matrix artifact, making it easier to compare experiments and identify exactly which configuration produced the best result.