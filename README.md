# Attention-Guided CycleGAN

A Pytorch implementation of "Unsupervised Attention-Guided Image-to-Image Translation", NIPS 2018, [[Paper]](https://arxiv.org/pdf/1806.02311.pdf) | [[TF code]](https://github.com/AlamiMejjati/Unsupervised-Attention-guided-Image-to-Image-Translation) from [yhlleo's UAGGAN repository](https://github.com/yhlleo/uaggan) altered for use in dataset creation for machine learning for vision.

This Attention-Guided CycleGAN maps segmentation images to real images.

### Acknowledgments

This code is largely taken from [yhlleo's UAGGAN repository](https://github.com/yhlleo/uaggan) which is based on [junyanz's pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).

### Changes

This implementation utilises the Attention portion of the code for our purposes with segmentation images. Rather than training a Neural Network to create the Attention masks, we create the Attention mask for the segmentation image from the segmentation image. Since the purpose of using Attention is to focus on the classified portions of the image and ignore the background (labeled as black) we can use this image to make the mask. The preprocessing creates an Attention mask by copying the segmentation image and colouring all non-black pixels white. For the real images, we have no way of doing this since these are unpaired images. We set the Attention mask for the real image to all white.

A noticeable issue with unpaired segmentation to real image translation is the lack of ability of the GAN to learn how to map large empty spaces. Along the boundaries of colours, we see a better mapping than away from the boundaries. To help with this, we add noise to the segmentation images. This is in the form of a small random change in the pixel's saturation.

The noise in the segmentation image helps with another problem faced in this mapping. The mapping from real to segmentation images has a loss of convergence. The discriminator becomes almost perfect, and the generator can no longer learn. This affects the training of the segmentation to real mapping. By adding in noise, it increases the difficulty of the problem for the discriminator for the real to segmentation mapping.

### Installation

For Conda users, there is an install script at `./scripts/conda_deps.sh`. Alternatively, you can create a new Conda environment using this command:

```
conda env create -f environment.yml
```

### Prepare Dataset:

Datasets are placed in the datasets directory in their own folder.

datasets
---- example_dataset
---- ---- segTrain
---- ---- segTest
---- ---- realTrain
---- ---- realTest

The segTrain folder will contain the segmentation images you want to train on.
The segTest folder will contain the segmentation images you want to test on.
The realTrain folder will contain the real images you want to train on.
The realTest folder will contain the real images you want to test on.

### Usage

#### Linux

- Training

  ```bash
  sh ./scripts/train_soccer.sh <gpu_id> <batch_size>
  ```

- Testing

  ```bash
  sh ./scripts/test_soccer.sh <gpu_id>
  ```

#### Windows

- Training

  ```bash
  ./scripts/train_soccer.bat <gpu_id> <batch_size>
  ```

- Testing

  ```bash
  ./scripts/test_soccer.bat <gpu_id>
  ```

### Mapping results

TODO: Add soccer results
