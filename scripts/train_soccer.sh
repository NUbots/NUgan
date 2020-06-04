GPU_ID=$1

python3 train.py \
  --dataroot ./datasets/soccer \
  --name soccer \
  --model uag_gan \
  --dataset_mode unaligned \
  --gpu_ids ${GPU_ID} \
  --batch_size 4 \
  --use_early_stopping 1 \
  --use_mask_for_D 0 \
  --no_dropout \
  --load_size 600 \
  --crop_size 256 \