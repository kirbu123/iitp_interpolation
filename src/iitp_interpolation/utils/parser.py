import argparse
from typing import Dict

import numpy as np

from .image import path_to_image
from .utils import parse_tuple


class Parser(argparse.ArgumentParser):
   def __init__(self, module_name: str='cartesiangrid', describition: str='Argument parse process...'):
      super().__init__(description=describition)
      self.module_name = module_name    
  
   def make_parse(self):
      if self.module_name == 'cartesiangrid':
          self.add_argument('--image_path', type=str, help='Path to the input image file', default=None)
          self.add_argument('--limits', type=list, help='Limits to the interpolation', default=[(0, 1), (0, 1), (0, 1)])
          self.add_argument('--points', type=parse_tuple, help='Points for interpolation', default=([0.1], [0.5], [0.3]))
      elif self.module_name == 'nearest_neighbour':
          self.add_argument('--image_path', type=str, help='Path to the input image file', default=None)
      elif self.module_name == 'bilinear':
          self.add_argument('--image_path', type=str, help='Path to the input image file', default=None)
      elif self.module_name == 'bicubic':
          self.add_argument('--image_path', type=str, help='Path to the input image file', default=None)
      else:
          self.add_argument('--image_path', type=str, help='Path to the input image file', default=None)         

      self.args = self.parse_args()
  
   def _load_image(self) -> np.ndarray:
      if self.args.image_path:
          try:
              image = path_to_image(self.args.image_path)
          except Exception as e:
              print(f"Error loading image: {e}, using random noise image.")
              image = np.random.rand(512, 512, 3)
      else:
          print("No image path provided. Using random noise image.")
          image = np.random.rand(512, 512, 3)
      return image

   def get_params(self) -> Dict:
        params = {}
        image = self._load_image()

        if self.module_name == 'cartesiangrid':
          limits = self.args.limits
          points = self.args.points

          params = {
            'image': image,
            'limits': limits,
            'points': points,
          }
        elif self.module_name == 'nearest_neighbour':
          params = {
            'image': image,
          }
        elif self.module_name == 'bilinear':
          params = {
            'image': image,
          }
        elif self.module_name == 'bicubic':
          params = {
            'image': image,
          }

        return params
