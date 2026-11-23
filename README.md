# ICD341 — Advanced Statistical Computing

## Overview

This repository contains my practical laboratory exercises, programming implementations, and statistical computing projects for **ICD341: Advanced Statistical Computing** at Mulungushi University.

The work focuses on developing practical skills in Python programming, scientific computing, statistical analysis, data visualisation, numerical methods, and reproducible computational workflows.

## Repository Structure

```text
ICD341/
│
├── labs/
│   ├── lab01_environment.ipynb
│   ├── lab02_numpy_fundamentals.ipynb
│   ├── lab03_numpy_vectorization_broadcasting.ipynb
│   ├── lab04_profiling_benchmarking.ipynb
│   ├── ICD341_Lab05_...
│   ├── ICD341_Lab06_...
│   └── ...
│
├── ICD341_Capstone/
│
├── Maize_Production_Project/
│
├── .gitignore
└── README.md
```

The `labs/` directory contains the practical laboratory notebooks, Python scripts, and related exercises. The project directories contain additional statistical computing and data analysis work.

## Development Environment

The laboratory exercises use a dedicated Conda environment to maintain consistent Python and package configurations.

### 1. Create the Conda Environment

```bash
conda create -n icd341 python=3.12
```

### 2. Activate the Environment

```bash
conda activate icd341
```

### 3. Install Required Packages

```bash
conda install numpy scipy pandas matplotlib jupyterlab
```

### 4. Verify the Environment

Check the installed Python version:

```bash
python --version
```

Run the environment verification script:

```bash
python labs/environment_test.py
```

### 5. Launch JupyterLab

```bash
jupyter lab
```

Alternatively, the notebooks can be opened and executed in Visual Studio Code after selecting the `icd341` Python interpreter.

## Technologies and Tools

The laboratory work uses the following technologies:

- **Python 3.12** — primary programming language.
- **NumPy** — numerical computing and array operations.
- **Pandas** — data manipulation and analysis.
- **SciPy** — scientific and statistical computing.
- **Matplotlib** — data visualisation.
- **JupyterLab** — interactive notebook development.
- **Visual Studio Code** — code editing and development.
- **Git and GitHub** — version control and repository management.

Additional libraries and tools are used where required by individual laboratory exercises and projects.

## Reproducibility

A dedicated Conda environment helps maintain consistent dependencies across laboratory exercises.

Git is used to track project changes, while `.gitignore` excludes unnecessary temporary files, Python cache files, and Jupyter checkpoint directories.

## Author

**Mwila Singoma**
Bachelor of Data Science Student
Mulungushi University