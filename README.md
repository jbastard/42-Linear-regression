# 42 Linear Regression

A simple linear regression project that predicts car price from mileage using gradient descent.

## Overview

This repository provides:
- Model training from a CSV dataset
- Basic model evaluation with a tolerance-based success rate
- Interactive price prediction from user input
- JSON persistence for trained parameters (`theta0`, `theta1`)

The current implementation uses one feature (`km`) and one target (`price`).

## Project Structure

```text
.
├── data/
│   └── data.csv
├── models/
│   └── theta.json
├── scripts/
│   ├── __init__.py
│   ├── estimate_price.py
│   ├── main.py
│   ├── tester.py
│   └── train.py
├── src/
│   └── linear_regression/
│       ├── __init__.py
│       ├── cli.py
│       ├── data_loader.py
│       ├── paths.py
│       ├── predictor.py
│       ├── storage.py
│       ├── testing.py
│       └── training.py
└── requirements.txt
```

## Requirements

- Python 3.10+
- `pip`

Dependencies are pinned in `requirements.txt`:
- `numpy`
- `pandas`

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Dataset Format

The default dataset is `data/data.csv`.

Required columns:
- `km`
- `price`

Example:

```csv
km,price
240000,3650
139800,3800
```

## Usage

### Unified CLI

Use the scripts command with one option:

```bash
python scripts/main.py train
python scripts/main.py test
python scripts/main.py run
```

Options:
- `train`: trains the model and writes parameters to `models/theta.json`
- `test`: evaluates model performance on the dataset
- `run`: prompts for mileage and prints estimated price

### Dedicated Commands

You can also run dedicated entrypoints:

```bash
python scripts/train.py
python scripts/tester.py
python scripts/estimate_price.py
```

## How It Works

### Training

Training logic is implemented in `src/linear_regression/training.py`.

- Feature normalization is applied to mileage (`km`)
- Gradient descent runs for a fixed number of iterations
- Learned coefficients are converted back to the original feature scale
- Parameters are saved via `storage.save()`

Default hyperparameters:
- Learning rate: `0.02`
- Iterations: `200`

### Evaluation

Evaluation is implemented in `src/linear_regression/testing.py`.

For each sample:
- Prediction: `theta0 + theta1 * km`
- Success condition: absolute error <= 10% of true price

Reported metric:
- Success rate = successful predictions / number of samples

### Prediction

Prediction is implemented in `src/linear_regression/predictor.py`.

- Loads trained parameters from `models/theta.json`
- Reads mileage from user input
- Computes and prints predicted price
- Floors negative predictions at `0.0`

## File Responsibilities

- `src/linear_regression/cli.py`: command dispatcher (`train`, `test`, `run`)
- `src/linear_regression/training.py`: gradient descent and training workflow
- `src/linear_regression/testing.py`: evaluation metric and test loop
- `src/linear_regression/predictor.py`: interactive prediction
- `src/linear_regression/data_loader.py`: CSV loading and validation
- `src/linear_regression/storage.py`: JSON model persistence
- `src/linear_regression/paths.py`: central project paths

## Notes

- If `models/theta.json` is missing or invalid, default parameters `(0.0, 0.0)` are used.
