:: train_soccer.bat [GPU_ID] [BATCH_SIZE]

if [%1]==[] GPU_ID=-1
else GPU_ID=%1
if [%2]==[] BATCH_SIZE=1 
else BATCH_SIZE=%2

python train.py   --dataroot ./datasets/soccer   --name soccer   --model uag_gan   --dataset_mode unaligned   --gpu_ids 0  --batch_size 3 --use_early_stopping 1 --use_mask_for_D 0  --no_dropout   --load_size 600   --crop_size 256  --continue_train 1 