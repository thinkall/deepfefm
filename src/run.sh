CUDA_VISIBLE_DEVICES=0 nohup python -u src/trainer.py -m config/config_bigdata-1.yaml > log1.log &
CUDA_VISIBLE_DEVICES=0 nohup python -u src/trainer.py -m config/config_bigdata-2.yaml > log2.log &
CUDA_VISIBLE_DEVICES=3 nohup python -u src/trainer.py -m config/config_bigdata-8.yaml > log8.log &
CUDA_VISIBLE_DEVICES=3 nohup python -u src/trainer.py -m config/config_bigdata-7.yaml > log7.log &
CUDA_VISIBLE_DEVICES=2 nohup python -u src/trainer.py -m config/config_bigdata-6.yaml > log6.log &
CUDA_VISIBLE_DEVICES=2 nohup python -u src/trainer.py -m config/config_bigdata-5.yaml > log5.log &
CUDA_VISIBLE_DEVICES=1 nohup python -u src/trainer.py -m config/config_bigdata-4.yaml > log4.log &
CUDA_VISIBLE_DEVICES=1 nohup python -u src/trainer.py -m config/config_bigdata-3.yaml > log3.log &
