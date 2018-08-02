#!/bin/bash

# Copyright (c) 2018-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

shift

case $1 in 
EASY) LEVEL="4";;
MEDIUM) LEVEL="256";;
HARD) LEVEL="16384";;
*) LEVEL="256";;
esac

game=elfgames.go.game model=df_pred model_file=elfgames.go.df_model3 python3 df_console.py --mode online --keys_in_reply V rv \
    --use_mcts --mcts_verbose_time --mcts_use_prior --mcts_persistent_tree \
    --load ../../../pretrained-go-19x19-v0.bin \
    --server_addr localhost --port 1234 \
    --replace_prefix resnet.module,resnet \
    --no_check_loaded_options \
    --no_parameter_print \
    --verbose --gpu 0 --num_block 20 --dim 224 --mcts_puct 1.50 --batchsize 16 \
    --mcts_rollout_per_batch 16 --mcts_threads 2 --mcts_rollout_per_thread $LEVEL \
    --resign_thres 0.05 --mcts_virtual_loss 1
