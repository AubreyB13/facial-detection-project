Facial Detection Convolutional Neural Network <br> Aubrey Browne <br> DSCI6005 <br> May 2017
----

**Goal:**  
The goal of this project was to create a convolutional neural network (CNN) that could identify people from a camera stream (web camera). This is a simple classification problem. Facial detection is an interesting problem since it has several different applications. One application is for photography which is demonstrated when a camera can recognize a face within the image and then autofocus to the face.  


**Procedure:**  
My facial detection project was originally a facial recognition project but I decided to change it because the neural network for facial recognition did not respond quickly to the streaming web camera images (OpenCV). Therefore, I decided to change the focus of my project but I will go over the procedure for both the facial detection and facial recognition model. 

For the facial recognition model, the goal was for the convolutional neural network to distinguish between myself and everyone else. This required me to build and label a dataset of images (~11,000 images). I augmented the images to include some rotation, shear, rescale, and flipped changes which adds ‘noise’ to the images and robustness to my model. Using the existing CNN VGGnet, I retrained the last two layers of the model which significantly decreased the training time of the deep CNN but allowed me to personalize the model to find images that I was included in. This was fairly successful with an AUC of 0.897. However, even with only retraining the last two layers I found that it took a significant amount of time to train the model. This prevented me from finishing training and not seeing a better AUC. Then later during testing, I found that it would take a couple of mins to test an image for facial recognition and this would not work well for a live streaming webcam (using OpenCV). This problem could probably be fixed with the use of a graphics processing unit (GPU). 

The facial detection model, had a similar approach as above. One difference between the two was the image dataset now also included images without faces and in total included approximately 30,000 images.  I then build a shallow CNN since it would require less features or filters to distinguish between a face and non face within an image. This CNN included three convolutional layers, a max pooling layer, a flattening layer, and a softmax dense layer. The neural network performed well and started to overfit after one epoch which required me to stop training early. The AUC for the shallow CNN was 0.998.

This quickly predicted whether or not a face was present within the image which worked well with the live streaming webcam images. The network did well to recognize faces even when they were not straight on or complete. This outperformed the baseline model of Haar Cascade Classifier available through OpenCV which works mainly by detecting facial features (eyes, mouth, and nose). 

