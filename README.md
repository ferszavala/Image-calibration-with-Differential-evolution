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

  ![descarga (1)](https://user-images.githubusercontent.com/72468795/204596691-7ccd8189-1336-4794-a386-e83de93b6bbf.png)

  For each variable *k* or *ui*, the value is selected randomly between *vi* or *ui*. If a random number between 0 and 1 is less than Cr, the value is taken from *vi*.   For guarantying that at less one value is taken from *vi*, the value of a variable randomly selected l, is assigned with the value of *vi*.
The new vector *ui* is positionated in one of the corners of the hyperrectangle generated with the positions of *xi* and *vi*
- **Mutation:** in this operator, for each individual *xi*, another one called *vi* is generated. The first step consists of randomly selecting three individuals from the population: ![descarga (2)](https://user-images.githubusercontent.com/72468795/204597454-5d7f6516-009a-4eef-8336-87dff02dad12.png).The new individual *vi* is calculated as follows: 

  ![descarga (3)](https://user-images.githubusercontent.com/72468795/204597830-82139d13-0c4d-4e70-8a83-212c0dd3f6a4.png)

  Where F is a random number between 0 and 2.
The difference between ![descarga (4)](https://user-images.githubusercontent.com/72468795/204598208-0cc6ebe8-b837-4c7d-bb2e-281208fd7499.png) and ![descarga (5)](https://user-images.githubusercontent.com/72468795/204598349-455b1295-f467-4068-8a0c-2aad7b77ba30.png) defines the direction and the magnitude of mutation. *F* slightly changes the magnitude. ![descarga (6)](https://user-images.githubusercontent.com/72468795/204598492-3b126d53-b572-47e7-807c-72b68d4b8f56.png) represents the initial point.
At the beginning, all the individuals are dispersed and ![descarga (7)](https://user-images.githubusercontent.com/72468795/204599532-a809be8b-7eba-4ad7-99d0-6ea3d75a7ffc.png) is big, but when the algorithm is converging, the individuals are concentrated in some local minimums and the value of ![descarga (7)](https://user-images.githubusercontent.com/72468795/204599591-faae08ca-63ee-4308-88ff-f4ab9109d185.png) is smaller. It is magic!
- **Survivor selection:** the selection is performed by tournament. The vest individual of *ui* and *xi* is selected to be part of the next generation

- **In the problem:** individuals are represented by vectors transformed to 3x3 pairwise matrices that symbolize the transformation matrix necessary to arrive at the real colors of the palette

### To review the result 
The images have been compared before and after being processed with the convolution, to the original calibration palette by following the next techniques:
- Structural Similarity Index (SSIM)
- Histogram (cv2.comparehist)
- Macro F1 

### About the files
In each of the "image_calibration_#.ipynb" files there is a development of the algorithm with a different image for different results, depending on factors such as light or the colors of the photograph that was taken. In the file "differential_evolution.py" is the development of the evolutionary computational algorithm
