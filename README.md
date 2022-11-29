# Image color calibration by using differential evolution and a convolution kernel

## Final project of the Optimization and metaheuristics course, seventh semester of artificial intelligence engineering at the Universidad Panamericana, Aguascalientes campus

## María Cristina Velázquez García & María Fernanda Zavala López - November 2022

### Problem to solve

According to a photograph of the calibration palette taken next to an object, it is necessary to calibrate the colors according to the tones and lighting of the original palette with the appropriate colors

### Is needed to first to image processing

- Detect all important edges of the image and select the largest one
- Obtain the coordinates of the most significant edge (the one of the palette)
- Apply transformations to the image so that it can be arranged in the same way as the original (in the same dimensions and angle)

### The algorithm to use is Differential Evolution

**Definition:** Differential Evolution is an optimization method belonging to the category of evolutionary computation, applied in solving complex problems.

- **Types of problems that this algorithm can solve:** It's a robust algorithm for solving continous multidimentional optimization problems.
- **Representation:** Vectors whose entries are the variables values.                    
The first generation of individuals must be initialized using a range of values. Each variable has a minimum 𝑥𝑘 𝑚𝑖𝑛 and a maximum value 𝑥𝑘 𝑚𝑎𝑥. Formally, each variable k of i-th individual can be calculated as follows: 
![descarga](https://user-images.githubusercontent.com/72468795/204595323-1b0788a2-3649-4ea3-a161-e3e60c717ad5.png)

- **Parent selection technique:** the selection is performed by tournament. The best individual is selected to be part of the next generation
- **Crossover:** combines the original vector *xi* with the new one *vi* for creating another one *ui*

![descarga](https://user-images.githubusercontent.com/72468795/204600654-6e0df280-f57e-4635-8a6a-809b7d110db1.png)

  For each variable *k* or *ui*, the value is selected randomly between *vi* or *ui*. If a random number between 0 and 1 is less than Cr, the value is taken from *vi*.   For guarantying that at less one value is taken from *vi*, the value of a variable randomly selected l, is assigned with the value of *vi*.
The new vector *ui* is positionated in one of the corners of the hyperrectangle generated with the positions of *xi* and *vi*
- **Mutation:** in this operator, for each individual *xi*, another one called *vi* is generated. The first step consists of randomly selecting three individuals from the population: ![descarga (1)](https://user-images.githubusercontent.com/72468795/204600867-518fff97-1101-4168-9665-e99d2ce8bd7f.png).The new individual *vi* is calculated as follows: 

  ![descarga (2)](https://user-images.githubusercontent.com/72468795/204601013-a80b8f3d-4b4b-490a-a5e7-b75c10fbba6c.png)

  Where F is a random number between 0 and 2.
The difference between ![descarga (3)](https://user-images.githubusercontent.com/72468795/204601235-0926860a-30a8-402c-9d6e-53476cc7aa85.png) and ![descarga (4)](https://user-images.githubusercontent.com/72468795/204601346-b0d3c014-e098-4c01-801d-612f0d1dad2b.png) defines the direction and the magnitude of mutation. *F* slightly changes the magnitude. ![descarga (5)](https://user-images.githubusercontent.com/72468795/204601776-e6111558-46d0-44df-960f-852f3a759763.png) represents the initial point.
At the beginning, all the individuals are dispersed and ![descarga (6)](https://user-images.githubusercontent.com/72468795/204602031-d19526bb-fbaa-4f46-9b19-9811ae683c6f.png) is big, but when the algorithm is converging, the individuals are concentrated in some local minimums and the value of ![descarga (6)](https://user-images.githubusercontent.com/72468795/204601984-b75a7f94-5c9d-452e-9edd-ea097bb46fb9.png) is smaller. It is magic!
- **Survivor selection:** the selection is performed by tournament. The vest individual of *ui* and *xi* is selected to be part of the next generation

- **In the problem:** individuals are represented by vectors transformed to 3x3 pairwise matrices that symbolize the transformation matrix necessary to arrive at the real colors of the palette

### To review the result 
The images have been compared before and after being processed with the convolution, to the original calibration palette by following the next techniques:
- Structural Similarity Index (SSIM)
- Histogram (cv2.comparehist)
- Macro F1 

### About the files
In each of the "image_calibration_#.ipynb" files there is a development of the algorithm with a different image for different results, depending on factors such as light or the colors of the photograph that was taken. In the file "differential_evolution.py" is the development of the evolutionary computational algorithm
