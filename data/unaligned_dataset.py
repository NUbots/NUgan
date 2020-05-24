import os.path
from data.base_dataset import BaseDataset, get_params, get_transform
from data.image_folder import make_dataset
from PIL import Image
import random


class UnalignedDataset(BaseDataset):
    """
    This dataset class can load unaligned/unpaired datasets.

    It requires two directories to host training images from domain A '/path/to/data/trainA'
    and from domain B '/path/to/data/trainB' respectively.
    You can train the model with the dataset flag '--dataroot /path/to/data'.
    Similarly, you need to prepare two directories:
    '/path/to/data/testA' and '/path/to/data/testB' during test time.
    """

    def __init__(self, opt):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        BaseDataset.__init__(self, opt)
        # create a path '/path/to/data/trainA'
        self.dir_A = os.path.join(opt.dataroot, opt.phase + 'A')
        # create a path '/path/to/data/trainB'
        self.dir_B = os.path.join(opt.dataroot, opt.phase + 'B')

        # load images from '/path/to/data/trainA'
        self.A_paths = sorted(make_dataset(self.dir_A, opt.max_dataset_size))
        # load images from '/path/to/data/trainB'
        self.B_paths = sorted(make_dataset(self.dir_B, opt.max_dataset_size))
        self.A_size = len(self.A_paths)  # get the size of dataset A
        self.B_size = len(self.B_paths)  # get the size of dataset B
        btoA = self.opt.direction == 'BtoA'
        # get the number of channels of input image
        input_nc = self.opt.output_nc if btoA else self.opt.input_nc
        # get the number of channels of output image
        output_nc = self.opt.input_nc if btoA else self.opt.output_nc
        # self.transform_A = get_transform(self.opt, grayscale=(input_nc == 1))
        self.transform_B = get_transform(self.opt, grayscale=(output_nc == 1))
        # self.transform_Att = get_transform(
        #     self.opt, grayscale=(input_nc == 1))

    def __getitem__(self, index):
        """Return a data point and its metadata information.

        Parameters:
            index (int)      -- a random integer for data indexing

        Returns a dictionary that contains A, B, A_paths and B_paths
            A (tensor)       -- an image in the input domain
            B (tensor)       -- its corresponding image in the target domain
            A_paths (str)    -- image paths
            B_paths (str)    -- image paths
        """
        A_path = self.A_paths[index %
            self.A_size]  # make sure index is within then range
        if self.opt.serial_batches:   # make sure index is within then range
            index_B = index % self.B_size
        else:   # randomize the index for domain B to avoid fixed pairs.
            index_B = random.randint(0, self.B_size - 1)
        B_path = self.B_paths[index_B]
        A_img = Image.open(A_path).convert('RGB')
        B_img = Image.open(B_path).convert('RGB')
        
        width, height = A_img.size

        # Yellow is high RED GREEN low BLUE
        # Red is high RED low GREEN BLUE
        # Green is high GREEN low RED BLUE

        for x in range(width):
            for y in range(height):
                current_color = A_img.getpixel((x, y))
                if current_color[0] > 50 and current_color[1] > 50 and current_color[2] < 50:
                    A_img.putpixel((x,y), current_color + noise(true, true, false)) # add noise to yellow
                elif current_color[0] > 50 and current_color[1] < 50 and current_color[2] < 50:
                    A_img.putpixel((x,y), current_color + noise(true, false, false)) # add noise to red
                elif current_color[0] < 50 and current_color[1] > 50 and current_color[2] < 50:
                    A_img.putpixel((x,y), current_color + noise(true, false, false)) # add noise to green

        btoA = self.opt.direction == 'BtoA'
        input_nc = self.opt.output_nc if btoA else self.opt.input_nc

        # apply the same transform to both A and and Att
        transform_params = get_params(self.opt, A_img.size)
        self.transform_A = get_transform(self.opt, transform_params, grayscale=(input_nc == 1))
        self.transform_Att = get_transform(self.opt, transform_params, grayscale=(input_nc == 1))

        # apply image transformation
        A = self.transform_A(A_img)
        B = self.transform_B(B_img)

        Att_img = Image.open(A_path).convert('RGB')
        width, height = Att_img.size
        
        for x in range(width):
            for y in range(height):
                current_color = Att_img.getpixel((x, y))
                if current_color[0] > 50 or current_color[1] > 50 or current_color[2] > 50:
                    Att_img.putpixel((x, y), (255, 255, 255))
                else: 
                    Att_img.putpixel((x,y), (0,0,0))

        ATT=self.transform_Att(Att_img)

        return {'A': A, 'B': B, 'ATT': ATT, 'A_paths': A_path, 'B_paths': B_path}

    def __len__(self):
        """Return the total number of images in the dataset.

        As we have two datasets with potentially different number of images,
        we take a maximum of
        """
        return max(self.A_size, self.B_size)

    def noise(red, green, blue):
        randRed = random.randint(0, 255) if red else 0
        randGreen = random.randint(0, 255) if green else 0
        randBlue = random.randint(0, 255) if blue else 0
        return (randRed, randGreen, randBlue)

        
        

 a if a < b else b 