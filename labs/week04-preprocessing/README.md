# Week 4 — Leak-Free Preprocessing Pipeline

## Part 8 — Reflection

### 1. Why does similar accuracy not mean the leak was harmless?

The original train.py accuracy and the final leak-free pipeline accuracy were both 0.6375. However, similar accuracy does not mean the leak was harmless. The original preprocessing was fitted on the full dataset before the train/test split, so information from rows that later became part of the test set influenced the preprocessing statistics. The professor's instructions emphasize that this type of leak does not necessarily cause a large change in accuracy, so accuracy alone cannot prove that preprocessing was correct.

### 2. Which lines caused the leak, and how was it proven?

The leak was caused by fitting the imputer and StandardScaler on the full dataset before train_test_split:

- `SimpleImputer(strategy="mean").fit_transform(X[NUMERIC_FEATURES])`
- `StandardScaler().fit(...)`

The leak was proven by comparing the scaler means from the full dataset with the scaler means from the training data only. The leaky full-data scaler means were:

`[4.033000e+01 4.376145e+04 7.925000e+01 1.533568e+04 6.877480e+03]`

The correct train-only scaler means were:

`[4.025000e+01 4.321302e+04 7.766000e+01 1.510494e+04 6.750840e+03]`

For example, the `annual_income` mean was approximately 43761.45 when calculated from the full dataset, compared with approximately 43213.02 when calculated from the training data only. Because the fitted statistics were different, the comparison directly demonstrated that the preprocessing had learned information from data that should have remained unseen.

### 3. What production problem does recomputing the StandardScaler describe?
If serving code recomputed a StandardScaler using requests from the last hour instead of loading the scaler fitted during training, that would describe a training-serving consistency problem, where the transformation used during serving does not match the transformation learned during training. This differs from the lab's leakage bug because the lab's problem occurred during training: the preprocessing was fitted using both training and future test rows. In production, the problem would be that serving uses a newly fitted transformation instead of reusing the fitted transformation state from training.

### 4. What does PCA's state mean, and what would go wrong if PCA were refitted during serving?

PCA's state is the fitted transformation learned from the training data, including the directions used to transform the features. In this pipeline, PCA is fitted only as part of the training pipeline and then reused when making predictions. If serving code ran a fresh `PCA().fit_transform()` on incoming requests, it would learn a new transformation from those requests instead of using the transformation learned during training. The resulting feature representation could therefore be different from the representation used to train the classifier, making the model's predictions inconsistent with its training conditions.