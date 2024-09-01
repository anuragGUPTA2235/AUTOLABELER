# AUTOLABELER CUM AUTO-TRAINING PIPELINE
# Auto-Annotation Pipeline for Labeling Large Datasets
## The Automated Algorithm
![1700477345006](https://github.com/user-attachments/assets/29381f47-08e2-49d3-bbb2-dabb271612b7)
IN SAE AEROSPACE AEROTHON 2023 , the problem statement wanted us to localize 4 hotspots and one target from a height of 30 metres, and my subsystem was successfully able to deliver a YOLOV7 model that was highly reliable and accurate.
The model was trained in the aerial environment of Hubli, but when faced a new environment, in Bengaluru it performed satisfactorily, which was due to extensive training,augmentation and a dataset that eventually contained more than 10k images.
But to label such a huge dataset was not possible with traditional methods of hand labelling, outsourcing or a large workforce was required to tackle this challenge.
But the team came up with an innovative way that not only automatically labelled this huge dataset but was able to simultaneously train on it also.
## Filtration through Segmentation
![1700477329913](https://github.com/user-attachments/assets/71c58759-de8d-4c93-8d3d-ddbc222e32d1)
The developed system AUTOLABELLER CUM AUTOTRAINING PIPELINE.
The principle behind is simple that we can use a trained model to detect objects which in turn will give pixel coordinates that can be normalized to, yolo label format of x,y,w,h and a txt file can be generated which will be used for subsequent training. Then we will use that newly labeled dataset to train while keeping the previous model as a base so that the previous learning is passed to the new model.
But this system requires that users have to first manual hand label between 100 to 200 images and train at first and the system will take care of the rest.
Also, if a model which is trained on less number of images with less noise will fail to detect, autolabel a image with is very complex. Therefore, the original dataset of about 10000 images was arranged in increasing order of noise/visual complexity. This was done by analysing the number of masks an image has by segmentation using meta segment anything.
Due to this, the model was trained and then subsequently used to autolabel and again train on images which were in the range of the detection strength of that particular version of model.
With each iteration, the model becomes stronger and stronger, capable of detecting and autolabel in the environment with more noises,
##  NO MANUAL LABELING
![1700477336182](https://github.com/user-attachments/assets/517f2edf-5341-454d-8e5b-f346454b0f77)
![1700477340607](https://github.com/user-attachments/assets/b468733f-1359-4f55-b53e-306e48b53807)
![1700477337539](https://github.com/user-attachments/assets/86224358-bc4b-4c01-bede-ee5c89fa0530)
Finally, the whole dataset of 10000 images was automatically labelled and a final model pt file was received well which was trained on the whole dataset and was able to perform well in untested environments.
Dedicated pipelines,transfer models and files automatically without the need to do it manually using python automation scripts.
The model was crucial as its detected pixel coordinates were directly sent to the GNC script which is used to command the drone to go towards the hotspots and targets to do payload drop and photography missions.
Future plan include to make it available in pypi library so that any one can use it by just installing from command pip install autolabeller.
