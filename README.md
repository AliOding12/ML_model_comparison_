
# ML Models Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

This project provides a framework for loading datasets, training, evaluating, and comparing various machine learning models using scikit-learn. It is organized for easy experimentation and extension, with modular code and Jupyter notebooks for interactive analysis.

## Motive
The main motive behind this project is to create a simple, extensible, and educational platform for:
- Learning and experimenting with machine learning models
- Comparing model performance on different datasets
- Demonstrating best practices in data preprocessing, training, and evaluation
- Providing a starting point for students and practitioners to build upon

## Features
- Load popular datasets (Iris, Wine, Digits, Titanic)
- Preprocess and split data
- Train and evaluate multiple models
- Visualize results and compare model performance
- Modular code for easy extension

## Project Structure
```
ml_models_project/
│
├── README.md
├── requirements.txt
├── data/
│   └── train.csv
├── notebooks/
│   └── models_comparison.ipynb
└── src/
    ├── __init___.py
    ├── data_loader.py
    ├── models.py
    ├── train_eval.py
    └── utils.py
```

## How It Works
1. **Data Loading**: Use functions in `src/data_loader.py` to load and preprocess datasets.
2. **Model Training**: Use `src/models.py` to get model definitions and `src/train_eval.py` to train and evaluate them.
3. **Visualization**: Use `src/utils.py` for plotting and analysis.
4. **Notebook**: Run `notebooks/models_comparison.ipynb` for interactive model comparison and results visualization.

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your data files (e.g., Titanic's `train.csv`) in the `data/` folder.
3. Open and run the notebook in `notebooks/` to start experimenting.

---

## Acknowledgements
- [scikit-learn](https://scikit-learn.org/) for machine learning algorithms
- [pandas](https://pandas.pydata.org/) for data manipulation
- [Jupyter](https://jupyter.org/) for interactive notebooks
- Open datasets from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

Feel free to extend the codebase with new datasets or models!
<!-- Initial commit: Set up project with README, requirements.txt and .gitignore -->
<!-- Update README with project overview and usage -->
<!-- Final updates to dependencies and documentation -->
