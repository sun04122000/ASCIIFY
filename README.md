**Asciify : ASCII Art Generator**
===

ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.

But..what if we use this for something other than text?

How about images? Images on your terminal!


**Project Description**
---
This project comprises of following features:
1. Generating Grayscale ASCII Art image from the original image.
2. Generating and Displaying Grayscale ASCII Art video from the original video.
3. Using our webcam to turn and save our live video into video containing ASCII charaters.

**How to run the project**
---
Language used:
Python

Required Library installations:
pillow
opencv-python

commands to install above libraries:
$ pip install opencv-python
$ pip install pillow

**Internal working of project**
---
<!-- Converting and saving image to ASCII Art -->
first we read the input image and store it in image variable as a matrix where each element of the matrix contains the color intensity of the corresponding pixel.

then we convert this matrix containing BGR(Blue-Green-Red) intensity values to Grayscale values.

Then we fix the number of columns of the image matrix and using the extracted width and height of image we calculate the number of rows in each matrix as well as width and height of each cell.

Now we obtain the height and width of font being used in the code. Since the final matrix  intensty values are to be replaced by the ASCII Characters.
Hence we obtain the final output width and output height of the image using number of columns, number of rows, charater width and charater height.

Then we traverse each pixel of the image using nested loops where for each row we keep appending the ASCII Chracters for each column in a string and then we draw the string obtained on the row we are currently traversing in the image.

the ASCII Charaters corresponding to each pixel are obtained by following the procedure mentioned below:
1. We store 2 charater strings one containing 10 charaters and the other containing 70 charaters.
2. Each of these strings are sorted on the basis of intensities of those charaters for eg. $ has highest intensity hence occuring at the first position in the string.
3. now we first calcualte the average intensity of the cell and then using index = ((av_intensity)/255)*len_charater_string, we obtain the index of ASCII Charater in the string corresponding to the intensity.

Now after writing the text on the image drawn, we remove the excess borders using getbbox(), crop the image obtaied using crop() and then we save the image with the desired name.

<!-- Converting Video to Ascii Art video -->
Video is just the array of images.
So we obtain this array of images by extracting the frames using videocapture method of opencv.
Then we run the loop to convert each image to ASCII Art using above mentioned method.
The we display and save the finally converted video after writing it in new video creted using method of open cv with the desired name.

<!-- Live ASCII Camera -->
Same procedure is followed as above but instead of capturing the input video we capture the input through webcam.

Here the captured live video is converted to ASCII Art colored in RGB rather than Grayscale.

For this we directly use the BGR matrix in the code instead of converting it to GrayScale.

**Learnings & Takeaways from the project**
---
1. ASCII Characters can be sorted in order of their intensities and can be used to replace the pixels of corresponding internsities.
2. Learnt how we can traverse an image using python.
3. Learnt to capture Live videos in ASCII Art Form and save its edited form.

**Resources/References**
https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles

https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/

https://web.archive.org/web/20210506132355/http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/

https://github.com/parthsingh29/ASCII-Art-Gen

