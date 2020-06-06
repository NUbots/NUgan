GPU_ID=$1
BATCH_SIZE=$2

python3 train.py \
  --dataroot ./datasets/soccer \
  --name soccer \
  --model uag_gan \
  --dataset_mode unaligned \
  --gpu_ids $1 \
  --batch_size $2 \
  --use_early_stopping 1 \
  --use_mask_for_D 0 \
  --no_dropout \
  --load_size 600 \
  --crop_size 256 \