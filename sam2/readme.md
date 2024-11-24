Setup
1. place the following files in ```sam2/notebooks/```
* (1) 1. generate_imgs.ipynb
* (2) 2. prepare train val test and pseudo annotated datasets.ipynb
* (3) check_balls.csv
* (4) label.py
2. place association_football_4.mp4 in ```sam2/notebooks/videos/```, can be downloaded from [link](https://drive.google.com/file/d/19scg1agNwHK8WgZL9Ewm7OhMn390t241/view?usp=share_link)
3. download weight and place it in ```sam2/checkpoints/```: https://dl.fbaipublicfiles.com/segment_anything_2/092824/sam2.1_hiera_lar
4. run 1.(1) to generate video frames
5. create a ```test/``` folder under ```images/association_football_4/```
6. place ```vid_*/``` under ```images/association_football_4/test/```, can be downloaded from [link](https://drive.google.com/file/d/1wGhOzX4ABe5JGcdmNlV-FGLWGTFClC7i/view?usp=share_link)

7. run 1.(2) to create yolov7 dataset using labelling tool 1.(4)
