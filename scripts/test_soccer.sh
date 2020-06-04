GPU_ID=$1

python3.5 test.py \
  --gpu_ids ${GPU_ID} \
  --dataroot ./datasets/soccer \
  --name soccer \
  --model uag_gan \
  --phase test \
  --num_test 15 \
  --thresh 0.1 \
  --load_size 1024 \
  --crop_size 1024 \