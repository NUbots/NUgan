:: train_soccer.bat [GPU_ID] [BATCH_SIZE] [NAME]

@ECHO OFF

IF "%~1"=="" ( SET GPU_ID=-1 ) ELSE SET GPU_ID=%~1
IF "%~2"=="" ( SET BATCH_SIZE=1 ) ELSE SET BATCH_SIZE=%~2
IF "%~3"=="" ( SET NAME=soccer_%DATE% ) ELSE SET NAME=%~3
IF "%~4"=="" ( SET CONT=0 ) ELSE SET CONT=%~4

python train.py^
 --dataroot ./datasets/soccer_blender_real^
 --name %NAME%^
 --model uag_gan_updated^
 --dataset_mode blender^
 --gpu_ids %GPU_ID%^
 --batch_size %BATCH_SIZE%^
 --use_early_stopping 1^
 --use_mask_for_D 1^
 --no_dropout^
 --load_size 600^
 --crop_size 256^
 --continue_train %CONT%^
 --print_freq 1000