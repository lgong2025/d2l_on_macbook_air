# Deep Learning on MacBook Air M4: PyTorch + d2l + Jupyter

This repository contains code examples (with slight modifications) from [Dive into Deep Learning](https://d2l.ai)
, adapted for the MacBook Air M4.

**Warning**: While the MacBook Air M4 includes GPU support, its performance is **significantly slower** than that of NVIDIA GPUs.

## Setup

1️⃣ Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew --version
```

2️⃣ Install Python (via pyenv recommended)

```bash
brew install pyenv
pyenv install 3.12.2   # or latest Python 3.x
pyenv global 3.12.2
python3 --version
```

3️⃣ Create a virtual environment

```bash
python3 -m venv ~/pytorch_env
source ~/pytorch_env/bin/activate
```

4️⃣ Install PyTorch and other dependencies with Apple MPS support

```bash
pip install --upgrade pip
pip install torch torchvision torchaudio pandas numpy scipy matplotlib notebook jupyterlab ipykernel
```

Register your environment as a kernel:

```bash
python -m ipykernel install --user --name=pytorch_env --display-name "Python (pytorch_env)"
```

Check if MPS (Apple GPU) is available:

```bash
python ./mps_gpu_readiness_check.py
```
