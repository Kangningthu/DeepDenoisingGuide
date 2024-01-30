# Learn, Denoise and Discover: A Guide to Deep Denoising and its Application to Scientific Imaging

## Overview
This repository contains the Jupyter notebooks accompanying the research project "Learn, Denoise and Discover: A Guide to Deep Denoising and its Application to Scientific Imaging."  It encompasses various Jupyter notebooks that serve as practical complements to the study.

## Introduction
This tutorial provides a self-contained description of deep-learning methodology for denoising, emphasizing aspects that are important in applications to real-world scientific imaging. The tutorial describes convolutional neural networks from first principles, explaining how to train them in a supervised and unsupervised manner. It also explains how to analyze the denoising strategies learned by these models, and how to evaluate their performance. Illustrative examples are provided based on computational experiments with simple 1D piecewise-constant signals, natural images and simulated electron-microscopy data. Code to reproduce all experiments is available online. In addition, a detailed case study is used to demonstrate the potential and challenges of applying deep denoising in real-world scientific-imaging scenarios. In the case study, supervised, unsupervised and semi-supervised deep-learning models are leveraged to denoise transmission-electron-microscopy data acquired at a very low signal-to-noise-ratio with the goal of investigate the atomic structure of catalytic nanoparticles.  
## Contents
1. **Train and inference code for natural images denoising** [1.natural_image.ipynb](1.natural_image.ipynb)
2. **Train and inference code for piecewise constant denoising** [1.piecewise_constant.ipynb](1.piecewise_constant.ipynb)
3. **Train and inference code for microscopy denoising** [1.microscopy.ipynb](1.microscopy.ipynb)
4. **Train of Gradient for Microscopy Images** [2.gradient_microscopy.ipynb](2.gradient_microscopy.ipynb)
5. **Train of Gradient for Natural Images** [2.gradient_natural_images.ipynb](2.gradient_natural_images.ipynb)


## Access to Pre-trained Models

Acknowledging the computational intensity and the potential limitations due to the absence of GPU resources, we provide links to the pre-trained models. For the piecewise constant signal denoising, given the feasibility of CPU training, pre-trained models are not provided.
### Pre-trained Model for Natural Images
[Natural_image](pretrain_models%2FNatural_image)

### Pre-trained Model for Microscopy Images
[Microscopy](pretrain_models%2FMicroscopy)

## GitHub repository
https://github.com/Kangningthu/DeepDenoisingGuide
### Installation
Installing the required Python packages using the `requirements.txt` file within the GitHub repository. 


## Contact

For inquiries, contributions, or further information, please contact us at the following email address:

Email: sm7582 AT nyu.edu or kl3141 AT nyu.edu