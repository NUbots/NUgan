# Masked CycleGAN

A PyTorch implementation of a CycleGAN that uses masks to remove the consideration of the background of a soccer field image from the training. The background is removed based on corresponding segmentation images. 

The Masked CycleGAN maps semi-synthetic images to real images. It uses output from [NUpbr](https://github.com/NUbots/NUpbr) to create real images. 

### Acknowledgments

This code is based on [yhlleo's UAGGAN repository](https://github.com/yhlleo/uaggan), which is based on the TensorFlow implementation by [Mejjati et al.](https://github.com/AlamiMejjati/Unsupervised-Attention-guided-Image-to-Image-Translation). This code accompanies the paper by [Mejjati et al.](https://arxiv.org/pdf/1806.02311.pdf).

This work is based on the work by [Zhu, Park, et al.](https://arxiv.org/pdf/1703.10593.pdf) along with the implementation at [junyanz's pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).

### Changes

This CycleGAN maps semi-synthetic soccer field images to real soccer field images. It loads in paired segmentation and semi-synthetic images from [NUpbr](https://github.com/NUbots/NUpbr). It uses the segmentation images to create attention masks that replace the generated fake background with the original semi-synthetic background. 

The repository contains a pretrained base model that will map semi-synthetic soccer field images to real soccer field images. This model can then be fine-tuned to a specific field by training from the base model with a dataset of real images of a specific field. When training is run, without specifying to continue an existing fine-tuning trained model, the pretrained base will be loaded. 

### Prerequisites

This code has been tested on Windows with Anaconda and Linux Mint.

Clone the repository

```sh
git clone https://github.com/NUbots/CycleGAN
```

You can use either CPU or NVIDIA GPU with latest drivers, [CUDA](https://developer.nvidia.com/cuda-downloads) and [cuDNN](https://developer.nvidia.com/cudnn).

If you are using Windows, we recommend using [Anaconda](https://docs.anaconda.com/anaconda/install/windows/). 

To set up with pip run

```sh
sudo apt install python-pip
pip3 install setuptools wheel
pip3 install -r requirements.txt
```

To set up with Anaconda you can create a new environment with the given environment file

```sh
conda env create -f environment.yml
```

Or alternatively use the batch (`./scripts/conda_deps.bat`) or shell (`./scripts/conda_deps.sh`) scripts to install the dependencies.

### Training

You will need to add a dataset. A semi-synthetic to real dataset can be found on the NAS. 

The dataset folder must contain three folders for training. These are

| Folder | Contents |
| ---- | --- |
| trainA | Contains training images in the Blender semi-synthetic style. |
| trainA_seg | Contains the corresponding segmentation images for the Blender images. |
| trainB | Contains training images in the real style. |

Note that semi-synthetic images and segmentation images should have matched naming (such as the same number on both images in a pair). This ensures they pair correctly when sorted.

Start the Visdom server to see a visual representation of the training.

```sh
python -m visdom.server
```

Open Visdom in your browser at [http://localhost:8097/](http://localhost:8097/).

Open a new window. In Windows, run 

```sh
"scripts/train.bat" <GPU_ID> <BATCH_SIZE> <NAME> <DATAROOT> <CONT> <EPOCHCOUNT>
```

In other OS, such as Linux, run

```sh
sh scripts/train.sh <GPU_ID> <BATCH_SIZE> <NAME> <DATAROOT> <CONT> <EPOCHCOUNT>
```

The options are as follows

| Option | Description | Default |
| -- | -- | --- |
| GPU_ID | ID of your GPU. For CPU, use -1. | 0 |
| BATCH_SIZE | Batch size for training. Many GPUs cannot support a batch size more than 1. | 1 |
| NAME | Name of the training run. This will be the directory name of the checkpoints and results.  | The current date prepended with 'soccer_' |
| DATAROOT | The path to the folder with the trainA, trainA_seg, trainB folders. | ./datasets/soccer |
| CONT | Set if you would like to continue training from an existing trained model. This does not include the base model, which is loaded if CONT is 0. | 0 |
| EPOCHCOUNT | The epoch count to start from. If you are continuing the training, you can set this as the last epoch saved. | 1 |

In most cases you will not need to add any options. 

Training information and weights are saved in checkpoints/NAME/. Checkpoints will be saved every 20 epochs during training.

### Testing

Testing requires testA, testA_seg, and testB folders. 

| Folder | Contents |
| ---- | --- |
| testA | Contains test images in the Blender semi-synthetic style. |
| testA_seg | Contains the corresponding segmentation images for the testA Blender images. |
| testB | Contains test images in the real style. |

In Windows run

```sh
"scripts/test.bat" <GPU_ID> <NAME> <DATAROOT>
```

In other OS, such as Linux, run 

```sh
sh scripts/test.sh <GPU_ID> <NAME> <DATAROOT>
```

The options are as specified in the Training section, with the exception of the default value of NAME, which is soccer_base.  

The results will be in `results/NAME/test_latest`

### Generating

Generating requires a single generateA folder that contains Blender semi-synthetic images.

In Windows run

```sh
"scripts/generate.bat" <GPU_ID> <NAME> <DATAROOT>
```

In other OS, such as Linux, run 

```sh
sh scripts/generate.sh <GPU_ID> <NAME> <DATAROOT>
```

The options are as specified in the Testing section.

The output will be in `results/NAME/generate_latest`.

### Mapping results

Each row contains, from left to right: semi-synthetic Blender image, fake realistic image, masked fake realistic image, and attention mask.

![Results of the transfer between semi-synthetic images and real images.](docs/base_results.png 'Each row contains a semi-synthetic image, fake realistic image, masked fake realistic image, and attention mask.')