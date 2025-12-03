mkdir logs
CUDA_VISIBLE_DEVICES=0 python main.py --net resnet18 --dataset irish --epochs 5 --steps 50 80 --batch-size 16 --save-dir clover_res18_irish --seed 1 --lr 0.03 --num-classes 4 --pretrained imagenet > logs/logs_irish.txt
CUDA_VISIBLE_DEVICES=0 python main.py --net resnet18 --dataset irish_ext --epochs 5 --steps 50 80 --batch-size 16 --save-dir clover_res18_irish_ext --seed 1 --lr 0.03 --num-classes 4 --pretrained imagenet > logs/logs_irish_ext.txt

# CUDA_VISIBLE_DEVICES=0 python main.py --net resnet18 --dataset danish --epochs 5 --steps 50 80 --batch-size 16 --save-dir clover_res18_danish --seed 1 --lr 0.03 --num-classes 5 --pretrained imagenet > logs/logs_danish.txt
# CUDA_VISIBLE_DEVICES=0 python main.py --net resnet18 --dataset danish_ext --epochs 5 --steps 50 80 --batch-size 16 --save-dir clover_res18_danish_ext --seed 1 --lr 0.03 --num-classes 5 --pretrained imagenet > logs/logs_danish_ext.txt
