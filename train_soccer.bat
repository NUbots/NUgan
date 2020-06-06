:: train_soccer.bat [GPU_ID] [BATCH_SIZE]

if [%1]==[] SET GPU_ID=-1
else SET GPU_ID=%1
if [%2]==[] SET BATCH_SIZE=1 
else SET BATCH_SIZE=%2
if [%3]==[] SET NAME=soccer 
else SET NAME=%2

python train.py^
 --dataroot ./datasets/soccer^
 --name NAME^
 --model uag_gan^
 --dataset_mode unaligned^
 --gpu_ids 0^
 --batch_size 3^
 --use_early_stopping 1^
 --use_mask_for_D 0^
 --no_dropout^
 --load_size 600^
 --crop_size 256^
 --continue_train 1 