

Spirograph-like Drawing with Python Turtle


##Introduction
This Python script allows you to create Spirograph-like drawings using the Turtle graphics library. Each step of the drawing consists of a circle with a random color and a slightly rotated angle.

##Setup
Before you begin, ensure you have Python installed on your computer.

##Usage
Copy and paste the provided Python code into a Python script or IDE.

Run the Python script containing the code.

##A window will appear with the drawing. You can adjust the window size by modifying the following line of code:
screen.setup(800, 600)


##Customization:

You can customize the number of steps and the colors of the drawing.
To change the number of steps, modify the range in the loop. For example, range(100) will create 100 steps.
To customize colors, you can:
Modify the random_color() function to return specific colors.
Replace t.pencolor(color) with t.pencolor("your_color") to use a specific color.
Dependencies
The code uses the turtle module, which is a standard library in Python, so no additional installations are required.
