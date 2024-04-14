# image-compression-using-k-means

This repository contains code for image compression using K-means clustering.
The notebook is self-explanatory and contains explanations of all cells written to aid the reader.

The code in the notebook makes use of only numpy, pandas, and matplotlib. Any other external libraries have not been used. 
In essence, it is an implementation from "scratch".

![download](https://github.com/1arush/image-compression-using-k-means/assets/105356056/66647fe6-0429-4114-bfd9-2de82d03ab82)

In this repository, also added are 2 files, which serve to be samples for this notebook. Successful compression shows that there is a significant difference
in the sizes of these 2 files, while also maintaining information from the original image.
1) image_before_compression
    - The original sample image
    - size=336 KB
2) image_after_compression
   - The compressed sample image
   - size=277 KB

Some things to note;

- Value of chosen K is 20 (can be changed)
- Works on a single image with runtime of about 2 seconds
- Image is input using a path to plt.imread
- Allows any input dimensions for an image


**UPDATE**: I have added a folder 'online', which contains my naive implementation of hosting this model on a local web server, using flask.

 # How to run? 
1) run the following command
    - ```git clone https://github.com/1arush/image-compression-using-k-means.git```
2) navigate to ```image-compression-using-k-means/online``` and run
    - ```pip install -r requirements.txt```
4) now run the following command
    - ```python -m app.py``` (if it doesn't work, remove the ```-m``` flag and run)
5) a web server on your local machine should open up. now upload the file you would like to compress

