# Sierpinski fractals
## Sierpinski triangle or Sierpinski gasket
Chaos plot visualization is done using two different libraries (turtle and mathplotlib). In the first visualization, the points are drawn sequentially, due to this, the speed is much lower than in the second method, where all the points are drawn together and the result is presented in the form of a picture. Attractor points are 3 vertices of the triangle. The number of points can be changed (it is necessary to change the value of the variable n). <br/><br/>
**Sample image for an image using the turtle module and n = 50000**<br/><br/>
![image](https://user-images.githubusercontent.com/71276784/129447409-fe4fc377-165c-410a-83ba-496288ba8e47.png)<br/><br/>
**Sample image for an image using the mathplot module and n = 100000**<br/><br/>
![image](https://user-images.githubusercontent.com/71276784/129448057-686c301d-30c1-43c0-8d39-4f50b1a246dc.png)
## Sierpinski square or Sierpinski carpet
The algorithm is similar to drawing a Sierpinski triangle, but 8 points of attractors are used: 4 points of the apex of the square and midpoints of the sides.<br/><br/>
**Sample image for an image using the mathplot module and n = 100000**
<br/><br/>
![image](https://user-images.githubusercontent.com/71276784/129447623-d42f5976-be65-4df1-aeb7-3d65fef15aef.png)
<br/><br/>
## Note
When using the variant that uses the mathplotlib library for large `n` (~> 100000), it is recommended to additionally specify specify the last additional line width parameter  in `ax.scatter`, which can be made small, or even equal to zero, for example: `linewidths = 0`<br/><br/>
**An example of drawing a triangle for n = 10e7 without decreasing linewidth to 0**<br/><br/>
![image](https://user-images.githubusercontent.com/71276784/129447744-5c6b5639-185c-4437-b46f-c539f1e0080f.png)<br/><br/>
**An example of drawing a triangle for n = 10e7 with decreasing linewidth to 0**<br/><br/>
![image](https://user-images.githubusercontent.com/71276784/129447992-56846649-d4a5-4b06-89de-6b895313d129.png)<br/><br/><br/>
**Example of distribution of points with increasing n for a triangle**<br/><br/>
![Гифка с Gifius ru](https://user-images.githubusercontent.com/71276784/129448491-b5381c06-5248-4baf-9a59-539a3ccd83e4.gif)<br/><br/>
**Example of distribution of points with increasing n for a square**<br/><br/>
![Гифка с Gifius ru (6)](https://user-images.githubusercontent.com/71276784/129448740-6f9443f6-925a-439c-aa18-4f74e314432d.gif)



