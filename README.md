Facial Detection Convolutional Neural Network <br> Aubrey Browne <br> DSCI6005 <br> May 2017
----

**Goal:**
The goal of this project was to create a convolutional neural network (CNN) that could identify people from a camera stream (web camera). This is a simple classification problem. Facial detection is an interesting problem since it has several different applications. One application is for photography which is demonstrated when a camera can recognize a face within the image and then autofocus to the face.  


**Procedure:**
My facial detection project started as a facial recognition but I decided to change it because neural network for facial recognition did not respond quickly to the streaming web camera images. Therefore, I decided to change the focus of my project but I will go over the procedure for both the facial detection and facial recognition model.

For the facial recognition part of the project, the goal was for the convolutional neural network to distinguish between myself and everyone else. This required me to build and label a dataset of images which included approximately 11,000 images. Augmenting the imaged to include some rotation, shear, rescale, and flipped changes which added robustness to my model. Using the existing CNN VGGnet allowed me to retrain the last two layers of the model which significantly decreased the training time of the deep CNN while personalized it to the problem I was trying to solve. This was fairly successful with an AUC of 0.897. However, even with only retraining the last two layers I found that it took a significant amount of time to train the model. This prevented me from finishing training and not seeing a better AUC. Then later during testing, I found that it would take a couple of mins to test an image for facial detection and this would not work well for a live streaming webcam. This problem could probably be fixed with the use of a graphics processing unit (GPU).

The facial detection portion of the project, had a similar approach as above. One difference between the two was the image dataset now included images without faces in them and in total included approximately 30,000 images.  I then build a shallow CNN for this problem since it would require less features or filters to distinguish between a face and non face within an image. This CNN included 3 convolutional layers, a max pooling layer, a flattening layer, and a softmax dense layer. The neural network performed well and started to overfit after one epochs which required me to stop training early. The AUC for the shallow CNN was 0.998.

This predicted both that a face was present within the image and it did it quickly which was useful for the determining if a face was included within the web camera stream.  I also found that it did well finding faces when they were not straight on or when there was only a partial face within the image. This is important because people are not always looking straight into the camera.
