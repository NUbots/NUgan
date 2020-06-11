#!/bin/sh

# train.sh [GPU_ID] [BATCH_SIZE] [NAME] [DATAROOT] [CONT] [EPOCHCOUNT]
    # GPU_ID : ID of GPU. -1 for CPU.
    # BATCH_SIZE : size of batch in training
    # NAME : name of this training
    # DATAROOT : path to the folder with data folders
    # CONT : 0 for a new training run, 1 to continue a training run
    # EPOCHCOUNT : epoch number to start from. Useful if stopped training midway and want to continue from where you left off.

if [ -z "$1" ]; then GPU_ID=0; else GPU_ID=$1; fi
if [ -z "$2" ]; then BATCH_SIZE=1; else BATCH_SIZE=$2; fi
if [ -z "$3" ]; then NAME=soccer; else NAME=$3; fi
if [ -z "$4" ]; then DATAROOT=./datasets/soccer; else DATAROOT=$4; fi
if [ -z "$5" ]; then CONT=0; else CONT=$5; fi
if [ -z "$6" ]; then EPOCHCOUNT=1; else EPOCHCOUNT=$6; fi

if [ "${CONT}"==0 ]
then python3 train.py \
 --dataroot "${DATAROOT}" \
 --name "${NAME}" \
 --model att_cycle_gan \
 --dataset_mode blender \
 --gpu_ids "${GPU_ID}" \
 --batch_size "${BATCH_SIZE}" \
 --use_mask_for_D 1 \
 --no_dropout \
 --load_size 800 \
 --crop_size 256 \
 --from_base
else python3 train.py \
 --dataroot "${DATAROOT}" \
 --name "${NAME}" \
 --model att_cycle_gan \
 --dataset_mode blender \
 --gpu_ids "${GPU_ID}" \
 --batch_size "${BATCH_SIZE}" \
 --use_mask_for_D 1 \
 --no_dropout \
 --load_size 800 \
 --crop_size 256 \
 --continue_train "${CONT}" \
 --epoch_count "${EPOCHCOUNT}"
fi