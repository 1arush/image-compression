# image-compression-using-k-means

This repository contains code for image compression using K-means clustering.
The notebook is self-explanatory and contains explanations of all cells written to aid the reader.

The code in the notebook makes use of only numpy, pandas, and matplotlib. Other external libraires have not been used. 
In essence, it is an implementation 'from scratch'.

In this repository, also added are 2 files, which serve to be samples for this notebook. Successful compression shows that there is a significant difference
in the sizes of these 2 files, while also maintaining information from the original image.
1) image_before_compression (Original sample image)
2) image_after_compression (The compressed sample image)

Some things to note;

- Value of chosen K is 4 (can be changed)
- Works on a single image with runtime of about 2 minutes
- Image is input using a path to plt.imread
- Allows any input dimensions for an image
