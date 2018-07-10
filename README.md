# pix2pix + BEGAN
- [Image-to-Image Translation with Conditional Adversarial Nets](https://phillipi.github.io/pix2pix/)
- [BEGAN: Boundary Equilibrium Generative Adversarial Networks](https://arxiv.org/abs/1703.10717)
- Slightly Modified from [pix2pix+BEGAN](https://github.com/taey16/pix2pixBEGAN.pytorch)

# Install
- install [pytorch](https://github.com/pytorch/pytorch) and [pytorch.vision](https://github.com/pytorch/vision)
- GPU is required

# Dataset
- Due to liscence issues, I cannot provide face data I used. Please download from the original site: [Basel Face Model](https://faces.cs.unibas.ch/bfm/index.php?nav=1-2&id=downloads) Download the code to ./PublicMM1 folder
- Copy the codes in ./matlab into ./PublicMM1/matlab
- Use ./PublicMM1/matlab/script_gen_random_head.m to generate random training and testing data

# Train
- **pix2pixBEGAN**
- We use two steps for training.
- ```CUDA_VISIBLE_DEVICES=x python main_pix2pixBEGAN.py --exp save --niter 59```
- ```CUDA_VISIBLE_DEVICES=x python main_pix2pixBEGAN.py --exp /path/to/save/folder --netD save/net_D_epoch_58.pth --lambdaIMG 0.5 --lrD 0.00001```

# Results after 400 epoch
- (order in input, real-target, reconstructed-real, fake, reconstructed-fake) 
![reconDandGenG](./imgs/generated.png)


# Reference
- [pix2pixBEGAN](https://github.com/taey16/pix2pixBEGAN.pytorch)
- [Basel Face Model](https://faces.cs.unibas.ch/bfm/index.php?nav=1-1-0&id=details)
