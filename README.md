# car_pedestrian_tracking
> Python app that tracks cars and pedestrians in a video using OpenCV

A very simple python program that uses public classifiers to perform tracking with OpenCv.
The classifier has a decent accuracy and is not perfect. This is a simple project that helps understand how tracking in video works.

## Demo

<img src="demo.gif?raw=true" width="200px">

## Resources 

> Haar Cascade XML Files

- [Car Classifier](https://www.youtube.com/redirect?v=zg9X6ASj3Q0&event=video_description&q=https%3A%2F%2Fraw.githubusercontent.com%2Fandrewssobral%2Fvehicle_detection_haarcascades%2Fmaster%2Fcars.xml&redir_token=QUFFLUhqbWhTVmNNY25MdkVtaEhOT01Mdjgtd1N2b1NDZ3xBQ3Jtc0tuczgyVWl5UFJGYTllX2oxRDdEUXhjSmhWZFlxLVU1NTNKYVhRWklsLWl5Yi1NSHdhX2FPZzJSZFRldHF4c0tzelMtdjhKY1pCcUlya0RZVEIxMFJCREZaMmZhemVtcU83aXY4c2xCYUcyVVlfY1ZlYw%3D%3D)
- [Person Full Body Classifier](https://www.youtube.com/redirect?v=zg9X6ASj3Q0&event=video_description&q=https%3A%2F%2Fraw.githubusercontent.com%2Fopencv%2Fopencv%2Fmaster%2Fdata%2Fhaarcascades%2Fhaarcascade_fullbody.xml&redir_token=QUFFLUhqbExuTDJtcy00aEI5TlY5LWZUYV9yX0RxbmlCZ3xBQ3Jtc0ttdE0yU2pWM2Y4ZVZsZExMMzk5NUg5WkJ0WVRiVHVmTEZDS1VxbU1takJROVRKczcxZTdianJMcmVzUHJfVUtXNmxyNG5VR2VpdHBNdHo5S0dQTW1QN2xZaGIxTkJJUFgzaVNtejN4b0hSWFBCU05pcw%3D%3D)

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