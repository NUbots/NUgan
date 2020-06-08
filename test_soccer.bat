:: test_soccer.bat [GPU_ID] [NAME]
ECHO OFF

IF "%~1"=="" ( SET GPU_ID=-1 ) ELSE SET GPU_ID=%~1
IF "%~2"=="" ( SET NAME=soccer ) ELSE SET NAME=%~2

python test.py^
 --gpu_ids %GPU_ID%^
 --dataroot ./datasets/soccer^
 --name %NAME%^
 --model uag_gan_updated^
 --dataset_mode blender^
 --phase test^
 --num_test 15^
 --thresh 0.1^
 --load_size 1024^
 --crop_size 1024^