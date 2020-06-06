:: train_soccer.bat [GPU_ID] [BATCH_SIZE] [NAME]

ECHO OFF

IF "%~1"=="" ( SET GPU_ID=-1 ) ELSE SET GPU_ID=%~1
IF "%~2"=="" ( SET BATCH_SIZE=1 ) ELSE SET BATCH_SIZE=%~2
IF "%~3"=="" ( SET NAME=soccer ) ELSE SET NAME=%~3

python train.py^
 --dataroot ./datasets/soccer^
 --name %NAME%^
 --model uag_gan^
 --dataset_mode unaligned^
 --gpu_ids %GPU_ID%^
 --batch_size %BATCH_SIZE%^
 --use_early_stopping 1^
 --use_mask_for_D 0^
 --no_dropout^
 --load_size 600^
 --crop_size 256^