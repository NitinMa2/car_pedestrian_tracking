# car_pedestrian_tracking
> Python app that tracks cars and pedestrians in a video using OpenCV

A very simple python program that uses public classifiers to perform tracking with OpenCv.
The classifier has a decent accuracy and is not perfect. This is a simple project that helps understand how tracking in video works.

## Demo

<img src="demo.gif?raw=true" width="500px">

## Resources 

> Haar Cascade XML Files

- [Car Classifier](https://raw.githubusercontent.com/andrewssobral/vehicle_detection_haarcascades/master/cars.xml)
- [Person Full Body Classifier](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_fullbody.xml)

## Setup

### Requirements

  * Python 3.3+
  * OpenCV

To install OpenCV using `pip3`:

```shell
pip3 install opencv-python
```

And if that doesn't work, try
```shell
pip3 install opencv-python-headless
```