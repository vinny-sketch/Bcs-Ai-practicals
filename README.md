# CCS 2226 Foundations of AI - 2026 Practical Tasks

This repository contains the code implementations for the practical tasks in **CCS 2226 – Foundations of Artificial Intelligence**.

The practicals focus on the implementation of core Artificial Intelligence concepts including:
- Machine Learning
- Constraint Satisfaction Problems
- Logic Programming
- Search Algorithms

Each task is organized into its own directory containing:
- Source code
- Supporting resources/datasets
- Output samples
- Task-specific explanations

Additional explanations for each implementation are provided in the corresponding `README.md` file inside every task folder.

---

# Repository Structure

```text
CCS-2226-FOUNDATIONS-OF-AI/
│
├── Task-1-MNIST-Digit-Recognition/
│   ├── mnist_classifier.py
│   └── README.md
│
├── Task-2-Constraint-Satisfaction/
│   ├── australia_map_coloring.py
│   ├── nairobi_map_coloring.py
│   └── README.md
│
├── Task-3-Prolog-Family-Tree/
│   ├── family.pl
│   ├── screenshots/
│   └── README.md
│
├── Task-4-Search-and-Optimization/
│   ├── bfs.py
│   ├── dfs.py
│   └── README.md
│
├── requirements.txt
└── README.md
```

# Setup
1. Clone Repository
```bash
git clone https://github.com/GodswillOmondi/bse-AI-practicals.git
cd CCS-2226-FOUNDATIONS-OF-AI
```

2. Create Virtual Environment (Optional)
- Windows
```bash
python -m venv venv
venv\Scripts\activate
```

- Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies

```bash
pip install -r requirements.txt
```
# Running the Tasks

Navigate into the required task directory and run the corresponding program.

## Example:
```bash
cd Task-4-Search-and-Optimization
python bfs.py
```

# Requirements

Recommended tools and software:

- Python 3.10+
- SWI-Prolog
- VS Code / PyCharm
- Git

# Author

- - Godswill Omondi Ajuoga
- - **RegNo**: CIT-227-096/2024
- - BSc. Software Engineering
- - CCS 2226 – Foundations of Artificial Intelligence
