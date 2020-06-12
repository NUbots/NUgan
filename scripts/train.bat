:: train.bat [GPU_ID] [BATCH_SIZE] [NAME] [DATAROOT] [CONT] [EPOCHCOUNT]
    :: GPU_ID : ID of GPU. -1 for CPU.
    :: BATCH_SIZE : size of batch in training
    :: NAME : name of this training
    :: DATAROOT : path to the folder with data folders
    :: CONT : 0 for a new training run, 1 to continue a training run
    :: EPOCHCOUNT : epoch number to start from. Useful if stopped training midway and want to continue from where you left off.

@ECHO OFF

IF "%~1"=="" ( SET GPU_ID=0 ) ELSE SET GPU_ID=%~1
IF "%~2"=="" ( SET BATCH_SIZE=1 ) ELSE SET BATCH_SIZE=%~2
IF "%~3"=="" ( SET NAME=soccer_%RANDOM% ) ELSE SET NAME=%~3
IF "%~4"=="" ( SET DATAROOT= ./datasets/soccer) ELSE SET DATAROOT=%~4
IF "%~5"=="" ( SET CONT=0 ) ELSE SET CONT=%~5
IF "%~6"=="" ( SET EPOCHCOUNT=1 ) ELSE SET CONT=%~6

IF %CONT%==0 (
python train.py^
 --dataroot %DATAROOT%^
 --name %NAME%^
 --model att_cycle_gan^
 --dataset_mode blender^
 --gpu_ids %GPU_ID%^
 --batch_size %BATCH_SIZE%^
 --use_mask_for_D 1^
 --no_dropout^
 --load_size 800^
 --crop_size 256^
 --from_base
 ) ELSE (
 --dataroot %DATAROOT%^
 --name %NAME%^
 --model att_cycle_gan^
 --dataset_mode blender^
 --gpu_ids %GPU_ID%^
 --batch_size %BATCH_SIZE%^
 --use_mask_for_D 1^
 --no_dropout^
 --load_size 800^
 --crop_size 256^
 --continue_train %CONT%^
 --epoch_count %EPOCHCOUNT%^ 
 )