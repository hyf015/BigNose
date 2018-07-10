import torch.utils.data as data

from PIL import Image
import os
import os.path
import numpy as np

IMG_EXTENSIONS = [
  '.jpg', '.JPG', '.jpeg', '.JPEG',
  '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

def is_image_file(filename):
  return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def make_dataset(dir):
  images = []
  if not os.path.isdir(dir):
    raise Exception('Check dataroot')
  fars = sorted(os.listdir(os.path.join(dir, 'far')))
  nears = sorted(os.listdir(os.path.join(dir, 'near')))
  return sorted([os.path.join(dir,'far', f) for f in fars]), sorted([os.path.join(dir,'near', f) for f in nears])

def default_loader(path):
  return Image.open(path).convert('RGB')

class pix2pix(data.Dataset):
  def __init__(self, root, transform=None, loader=default_loader, seed=None):
    imgfar, imgnear = make_dataset(root)
    if len(imgfar) == 0:
      raise(RuntimeError("Found 0 images in subfolders of: " + root + "\n"
                 "Supported image extensions are: " + ",".join(IMG_EXTENSIONS)))
    self.root = root
    self.imgfar = imgfar
    self.imgnear = imgnear
    self.transform = transform
    self.loader = loader

    if seed is not None:
      np.random.seed(seed)

  def __getitem__(self, _):
    index = np.random.randint(self.__len__(), size=1)[0]
    pathA = self.imgnear[index]
    imgA = self.loader(pathA)
    pathB = self.imgfar[index]
    imgB = self.loader(pathB)
    # NOTE: img -> PIL Image
    #w, h = img.size
    #w, h = 512, 256
    #img = img.resize((w, h), Image.BILINEAR)
    # NOTE: split a sample into imgA and imgB
    #imgA = img.crop((0, 0, w/2, h))
    #imgB = img.crop((w/2, 0, w, h))
    if self.transform is not None:
      # NOTE preprocessing for each pair of images
      imgA, imgB = self.transform(imgA, imgB)
    return imgA, imgB

  def __len__(self):
    return len(self.imgfar)
