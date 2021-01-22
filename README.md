This is a clone of the BasicSR repo https://github.com/xinntao/BasicSR.git. Used for a University project.

## :wrench: Dependencies and Installation

- Python >= 3.7 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- [PyTorch >= 1.3](https://pytorch.org/)
- NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)

1. Clone repo

    ```bash
    git clone https://github.com/heeycoen/BasicSRClone.git
    ```

1. Install dependent packages

    ```bash
    cd BasicSR
    pip install -r requirements.txt
    ```

1. Install BasicSR

    Please run the following commands in the **BasicSR root path** to install BasicSR:<br>
    (Make sure that your GCC version: gcc >= 5) <br>
    If you do not need the cuda extensions: <br>
    &emsp;[*dcn* for EDVR](basicsr/models/ops)<br>
    &emsp;[*upfirdn2d* and *fused_act* for StyleGAN2](basicsr/models/ops)<br>
    please add `--no_cuda_ext` when installing

    ```bash
    python setup.py develop --no_cuda_ext
    ```

    If you use the EDVR and StyleGAN2 model, the above cuda extensions are necessary.

    ```bash
    python setup.py develop
    ```

    You may also want to specify the CUDA paths:

      ```bash
      CUDA_HOME=/usr/local/cuda \
      CUDNN_INCLUDE_DIR=/usr/local/cuda \
      CUDNN_LIB_DIR=/usr/local/cuda \
      python setup.py develop
      ```
