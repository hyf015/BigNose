# simple pix2pix + BEGAN for nasal distortion
- [Pix2Pix: Image-to-Image Translation with Conditional Adversarial Nets](https://phillipi.github.io/pix2pix/)
- [BEGAN: Boundary Equilibrium Generative Adversarial Networks](https://arxiv.org/abs/1703.10717)
- [Basel Face Model](https://faces.cs.unibas.ch/bfm/index.php?nav=1-1-0&id=details)

# Install & Requirements
- install [pytorch](https://github.com/pytorch/pytorch) and [pytorch.vision](https://github.com/pytorch/vision)
- GPU and MATLAB is required

# Dataset
- Due to liscence issues, I cannot provide face data I used. Please download from the original site: [Basel Face Model](https://faces.cs.unibas.ch/bfm/index.php?nav=1-2&id=downloads) Download the code and unzip the file to [`./PublicMM1`](./PublicMM1) folder
- Do not overwrite the codes in [`./PublicMM1/matlab`](./PublicMM1/matlab)
- Use `./PublicMM1/matlab/script_gen_random_head.m` in [`./PublicMM1/matlab`](./PublicMM1/matlab) to generate random training and testing data

# Train
- **pix2pixBEGAN**
- We use two steps for training.
- ```CUDA_VISIBLE_DEVICES=x python main_pix2pixBEGAN.py --exp save --niter 59```
- ```CUDA_VISIBLE_DEVICES=x python main_pix2pixBEGAN.py --exp /path/to/save/folder --netD save/net_D_epoch_58.pth --lambdaIMG 0.5 --lrD 0.00001```

# Pretrained Models
- We provide pretrained Discriminators in [`./Pretrained`](./Pretrained)
- The pretrained Generator is a splitted zip file, which can be downloaded [here](https://drive.google.com/drive/folders/1jlaZcRCOU1PrwBNoxHpFyOGe9KH-L7XL?usp=sharing)

# Results after 400 epoch
- (order in input, real-target, reconstructed-real, fake, reconstructed-fake) 
![reconDandGenG](./imgs/generated.png)


# Reference
- [pix2pix Pytorch](https://github.com/taey16/pix2pix.pytorch)
- [BEGAN Pytorch](https://github.com/sunshineatnoon/Paper-Implementations/tree/master/BEGAN)
- [pix2pixBEGAN](https://github.com/taey16/pix2pixBEGAN.pytorch)
- [Basel Face Model](https://faces.cs.unibas.ch/bfm/index.php?nav=1-1-0&id=details)
