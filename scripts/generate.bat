:: generate.bat [GPU_ID] [NAME] [DATAROOT]
    :: GPU_ID : ID of GPU. -1 for CPU.
    :: NAME : name of this training
    :: DATAROOT : path to the folder with data folders

@ECHO OFF

IF "%~1"=="" ( SET GPU_ID=0 ) ELSE SET GPU_ID=%~1
IF "%~2"=="" ( SET NAME=soccer_base ) ELSE SET NAME=%~2
IF "%~3"=="" ( SET DATAROOT= ./datasets/soccer) ELSE SET DATAROOT=%~3

python generate.py^
 --gpu_ids %GPU_ID%^
 --dataroot %DATAROOT%^
 --name %NAME%^
 --model_suffix _A^
 --no_dropout^
 --phase generate^
 --aspect_ratio 1.25^
 --crop_size 1024^
 --load_size 1024^