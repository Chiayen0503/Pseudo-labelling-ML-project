Setup
1. place ```Improve model iteratively.ipynb``` under ```yolov7/``` 
2. place ```custom_data/``` under ```yolov7/``` 
3. place ```association_football_4.mp4``` under ```yolov7/```, can be downloaded [here](https://drive.google.com/file/d/19scg1agNwHK8WgZL9Ewm7OhMn390t241/view?usp=share_link) 
4. Training command (for reproducing weights download [first run weights](https://drive.google.com/file/d/1H4Gx4jdSfm66llZ_zbhwXGPDCsLWFxTi/view?usp=share_link) and [second run weights](https://drive.google.com/file/d/1I2Uquwq9r8KcXeTApl5AOSStKTGdvCoG/view?usp=share_link)):
(1) first run: ```python train.py --img-size 640 --cfg cfg/training/yolov7.yaml --hyp data/hyp.scratch.custom.yaml --batch 16 --epochs 20 --data custom_data/dataset.yaml --weights yolov7.pt --workers 24 --name yolo_ball_det```
(2) second run: ```python train.py --img-size 640 --cfg cfg/training/yolov7.yaml --hyp data/hyp.scratch.custom.yaml --batch 16 --epochs 20 --data custom_data/dataset.yaml --weights runs/train/yolo_ball_det/weights/best.pt --workers 24 --name yolo_ball_det_2```
5. Save video prediction: 
```python detect.py --weights runs/train/yolo_ball_det_2/weights/best.pt --conf 0.25 --img-size 640 --source association_football_4.mp4```
