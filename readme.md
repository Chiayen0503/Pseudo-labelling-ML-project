# Machine Learning: Video Object Detection
*	Objective: Detect sports balls in video footage.
*	Instructions: </br>
 &nbsp; &nbsp; - Generate pseudo-annotations for video data. </br>
 &nbsp; &nbsp; -	Build an object detection pipeline that can train on your annotations. </br>
 &nbsp; &nbsp; -	Create an evaluation procedure with visualizations of predictions and annotations. </br>
&nbsp; &nbsp; -	Design a process to iteratively improve your dataset. </br>
*	Dataset: Sports-1M
*	This task is perfect for showcasing your computer vision and machine learning skills, especially if you’re creative with your annotations and improvement pipeline!




# Setup
1. It is recommanded to install two separate virtual environments for ```sam2``` and ```yolov7```, please ```git clone https://github.com/facebookresearch/sam2.git``` and ```git clone https://github.com/WongKinYiu/yolov7.git```  
  * For ```sam2/```, pip install pytorch first (do check compatible cuda version) before ```pip install -e ".[demo]" ```
  * For ```yolov7/```, ```pip install -r requirements.txt```
2. git clone our repository, take files from ```sam2/``` and ```yolov7```, move them to corresponding official sam2 and yolov7 repositories  
3. Read ```HawkEye_ML_project_report.pdf``` to learn about Pseudo-labelling and experiment setup and review.
4. Visit ```sam2/``` and run notebooks
5. Visit ```yolov7``` and run notebooks

# Results
After train on Yolov7 for few rounds of 20 epochs with only 400-600 training images, test/val 85 images, the results are shown in the following table. Here is [first-run weights](https://drive.google.com/file/d/1H4Gx4jdSfm66llZ_zbhwXGPDCsLWFxTi/view?usp=share_link), [second-run weights](https://drive.google.com/file/d/1I2Uquwq9r8KcXeTApl5AOSStKTGdvCoG/view?usp=share_link), [third-run weights](https://drive.google.com/drive/folders/17mGTurNVEQIGzcxCNAVm-yY5sGR7GbVD?usp=share_link) and [third+thres run weights](https://drive.google.com/drive/folders/1LrFkj_f_ENxbyUyXJMFU2j36bzEAQdSz?usp=share_link). Alternatively, we can download them [all](https://drive.google.com/drive/folders/1_URTkyhxhg1ElXu3pKC4iiE86gLG8ZIy?usp=share_link) at once

| run     | P     | R     | mAP@.5 | mAP@.5:.95 | mean conf | detected |
|---------|-------|-------|--------|------------|-----------|----------|
| 1       | 0.918 | 0.918 | 0.932  | 0.698      | 0.31      | 28       |
| 2       | 0.962 | 0.905 | 0.947  | 0.788      | 0.62      | 84       |
| 3       | 0.974 | 0.894 | 0.945  | 0.825      | 0.67      | 84       |
| 3+thres | 0.974 | 0.906 | 0.951  | 0.82       | 0.74      | 84       |

For real-time detection results, download [here](https://drive.google.com/file/d/1JvUnF9pbV16USMvw2572Xbq_Pb2FYVy8/view?usp=share_link)

