# Setup
1. It is recommanded to install two separate virtual environments for ```sam2``` and ```yolov7```, please ```git clone https://github.com/facebookresearch/sam2.git``` and ```git clone https://github.com/WongKinYiu/yolov7.git```  
  * For ```sam2/```, pip install pytorch first (do check compatible cuda version) before ```pip install -e ".[demo]" ```
  * For ```yolov7/```, ```pip install -r requirements.txt```
2. git clone our repository, take files from ```sam2/``` and ```yolov7```, move them to corresponding official sam2 and yolov7 repositories  
3. Read ```HawkEye_ML_project_report.pdf``` to learn about Pseudo-labelling and experiment setup and review.
4. Visit ```sam2/``` and run notebooks
5. Visit ```yolov7``` and run notebooks

Here is our benchmark, after 2 rounds of 20 epochs with only 400-600 training images, test/val 85 images each

![image info](./benchmark.png)
