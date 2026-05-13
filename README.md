# QML_DFT
#*Atomic locality embedded quantum machine learning for materials simulation*

---

## Quick Start

### Installation

Create a clean Python environment first. `Python 3.10` is recommended.
```bash
conda create -n qml_dft python=3.10 -y
conda activate qml_dft
pip install numpy scipy h5py psutil tensorboard tqdm pathos pymatgen tensorflow tensorcircuit
```

Then install the PyTorch-related packages with versions matching your local
Python, CUDA, and PyTorch environment:
- `torch`
- `torch_geometric`
- `torch_scatter`

### Dataset

Part of the datasets are included in this repository. Additional datasets used for reproducing the reported results are available on Zenodo:

https://doi.org/10.5281/zenodo.20129923

After downloading the dataset, place it under the project directory, for example:

```bash
QML_DFT/
├── dataset/
├── config/
├── run_train/
└── ...
```

### Run Training

From the parent directory:
```bash
python3 QML_DFT/run_train/train.py --config QML_DFT/config/train.ini
```
Or from inside the project directory:
```bash
python3 run_train/train.py --config config/train.ini
```

## Project Layout

The main folders inside `QML_DFT/` are:
- `config/`
  - training configuration files
- `dataset/`
  - example dataset
  - default training output directory
- `qml_dft_core/`
  - source code package
- `run_train/`
  - training entrypoint

The complete source code and datasets will be uploaded after the manuscript is accepted for publication.
The associated dataset has been deposited privately on Figshare and will become publicly available upon publication through the following DOI:
https://doi.org/10.6084/m9.figshare.32253582


## Output Files

In the provided `config/train.ini`, training outputs are written to:
```
/path/to/train_model
```
