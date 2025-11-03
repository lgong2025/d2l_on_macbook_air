import torch


if __name__ == "__main__":
    available = torch.backends.mps.is_available()
    assert available, "MPS backend is not available."
    print("MPS backend is available.")
