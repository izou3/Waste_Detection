# Food Waste Detection

The goal of this project was to detect food waste within a school cafeteria setting by analyzing waste footages taken of food and other waste being disposed of in trash cans. A formal report is located in the `./FormalReport.pdf` file and is summarized below. The code and code outputs of the project are located in the following colab notebooks.
* [CNN Implementation]()
* [Mask-RCNN Implemmentation using MatterPort]()
* [Mask-RCNN Implemmentation using Detectron2]()

**Directory Tree**
```bash
├── images
│   └── All_Images                      Contains the 116 meaningfully sampled video frames for Mask-RCNN Training 
│   └── Manual_Test                     Contains the 116 meaningfully sampled video frames but with blackened noise 
│   └── Manual Train                    Contains the 23 sampled video with blackend noise for holdout evaluation  
│   └── Test_Set                        Contains the 23 sampled video frames for Mask-RCNN hold-out evaluation
├── mrcnn                               Classes used to run the Mask-RCNN detection algorith based on Matterport implementation 
├── preprocessing                       Python scripts for reading video frames and blackening noise 
├── weights                             Contains the weight files of the fine-tuned Mask-RCNN and CNN for inference
├── FormalReport.pdf                    Formal report of project 
├── requirements.txt                    Neccessary dependencies to run the preprocessing scripts
├── CNN_WasteDetection.ipynb            [COLAB] Waste Detection using CNN following VGG16 Model        
├── Mask-RCNN_WasteDetection.ipynb      [COLAB] Waste Detection using MaskRCNN based on Matterport Implementation 
├── WasteDetection_Detectron2.ipynb     [COLAB] Waste Detection using MaskRCNN based on Detectron2 Implementation  
├── WasteDetection_LocalCPU.ipynb       Waste Detection using MaskRCNN based on Detectron2 Implementation on local machine CPU
```
---

## Future Work
* Implement Detection on the Edge 
* Algorithm to track and count the frequency of each type of food over time 

---

## References 
Abdulla, W. (2018, December 10). Splash of color: Instance segmentation with mask R-CNN and TensorFlow. 
Medium. Retrieved December 8, 2021, from 
https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46.

Food waste in America in 2022: Statistics & Facts: RTS. Recycle Track Systems. (n.d.). Retrieved December 8, 2021, 
from https://www.rts.com/resources/guides/food-waste-america/.

He, K., Gkioxari, G., Dollár, P., & Girshick, R. (2017). Mask r-cnn. In Proceedings of the IEEE international 
conference on computer vision (pp. 2961-2969).

Hough Circle transform. OpenCV. (n.d.). Retrieved December 8, 2021, from 
https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html.

Make sense. Make Sense. (n.d.). Retrieved December 8, 2021, from https://www.makesense.ai/.

Matterport. (n.d.). Matterport/MASK_RCNN: Mask R-CNN for object detection and instance segmentation on Keras 
and TensorFlow. GitHub. Retrieved December 8, 2021, from https://github.com/matterport/Mask_RCNN.

Seif, G. (2021, July 18). How to do everything in computer vision. Medium. Retrieved December 8, 2021, from 
https://towardsdatascience.com/how-to-do-everything-in-computer-vision-2b442c469928?gi=564b1e53ddf5.

Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. arXiv 
preprint arXiv:1409.1556.

Solawetz, J. (2020, October 5). What is mean average precision (MAP) in object detection? Roboflow Blog. Retrieved 
December 8, 2021, from https://blog.roboflow.com/mean-average-precision/.

Training a classifier. Training a Classifier - PyTorch Tutorials 1.10.0+cu102 documentation. (n.d.). Retrieved 
December 8, 2021, from https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html.

VGG16 - convolutional network for classification and detection. VGG16 - Convolutional Network for Classification 
and Detection. (2021, February 24). Retrieved December 8, 2021, from https://neurohive.io/en/popular-networks/vgg16/

