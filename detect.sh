
MODEL_PATH=/Users/panjunlin/Downloads/yolov5/runs/train/exp38/weights/best.pt
IMAGE_PATH=/Users/panjunlin/Downloads/begin.png
DETECT_SCRIPT=/Users/panjunlin/Downloads/yolov5/detect.py
IMAGE_DIRECTORY=/Users/panjunlin/repo/arcnight/dataset/test/images

ADB=/Users/panjunlin/Library/Android/sdk/platform-tools/adb
TEMP_DIR=/Users/panjunlin/repo/arcnight/tmp

if [ ! -d ${TEMP_DIR} ];
then
  mkdir ${TEMP_DIR}
fi
if [ -f ${TEMP_DIR}/output_coor.txt ];
then
	rm ${TEMP_DIR}/output_coor.txt
fi

${ADB} shell screencap -p > ${TEMP_DIR}/screen.png
python main.py ${MODEL_PATH} ${TEMP_DIR}/screen.png ${TEMP_DIR}/output_coor.txt
if [ -f ${TEMP_DIR}/output_coor.txt ];
then
${ADB} shell input tap $(cat ${TEMP_DIR}/output_coor.txt)
else
cp ${TEMP_DIR}/screen.png /Users/panjunlin/repo/arcnight/dataset/FN/origin/$(date "+%s").png
fi


