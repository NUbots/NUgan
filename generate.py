"""General-purpose generate script for image-to-image translation.

Based one CycleGAN project: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

Once you have trained your model with train.py, you can use this script to generate image from the model.
It will load a saved model from --checkpoints_dir and save the results to --results_dir.

It first creates model and dataset given the option. It will hard-code some parameters.
It will save all the images to a results folder.

Example (You need to train models first):
    Generate images from a CycleGAN model (one side only):
        python test.py --dataroot datasets/soccer --name soccer_base --model generate --no_dropout

    The option '--model generate' is used for generating CycleGAN results.
    This option will automatically set '--dataset_mode single', which only loads the images from one set.
    On the contrary, using '--model cycle_gan' requires loading and generating results in both directions,
    which is sometimes unnecessary. The results will be saved at ./results/.
    Use '--results_dir <directory_path_to_save_result>' to specify the results directory.

See options/base_options.py and options/test_options.py for more test options.
See training and test tips at: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/tips.md
See frequently asked questions at: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/qa.md
"""
import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import generate_save_images
from util.util import mkdir

if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 1    # test code only supports num_threads = 1
    opt.batch_size = 1     # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True     # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1    # no visdom display; the generate code will save the files.
    opt.model = 'test'     # Use the test model since it has everything we want
    opt.dataset = 'single' # Use the single dataset since it has everything we want
    opt.phase = 'generate' # We are in the generate phase
    dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    

    # Generate for all the data
    for i, data in enumerate(dataset):
        model.set_input(data)  # unpack data from data loader
        model.test()           # run inference
        img_dir = os.path.join(opt.results_dir, opt.name, '%s_%s' % (opt.phase, opt.epoch))  # define the website directory
        mkdir(img_dir)
        visuals = model.get_current_visuals()  # get image results
        img_path = model.get_image_paths()     # get image paths
        print(img_path)
        if i % 5 == 0:  # save images
            print('processing (%04d)-th image... %s' % (i, img_path))
        generate_save_images(img_dir, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)    
