YOLO_TRAIN_FILE=/Users/panjunlin/Downloads/yolov5/train.py
INPUT_MODEL_PATH=/Users/panjunlin/Downloads/yolov5/runs/train/exp37/weights/best.pt
python ${YOLO_TRAIN_FILE} --batch 16 --cache ram --epochs 16 --data /Users/panjunlin/repo/arcnight/dataset/data.yaml --weights ${INPUT_MODEL_PATH}
