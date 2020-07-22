# Image Stitching
This repository implements an image stitching algorithm. The stitching algorithm used here is based on this [publication](http://matthewalunbrown.com/papers/ijcv2007.pdf). Unlike many image stitching algorithms that are sensitive to the order of input images, this method is not only insensitive to the order of the input images but also orientation and illumination changes.  
An example of the same when subjected to different Illumination changes(Hazy and dark) is shown below:
![](output/out_illuminationchanges.jpg)

This is implemented on both videos as well as images:  

##### Usage:
###### Images:  python3 stitch.py  
###### Videos:  python3 vid_stitch.py  
