<b>

<h1>Immersive Collaboration System</h1><br>
This presents a prototype idea for wall-top displays for future offices, where instead of a small desktop, we treat the available walls as the desktop.<br> We have developed an effective human-computer interface for a virtual mouse system in a projector-camera configuration without any hardware requirement.<br> To experience our project only one camera source is required to detect the object. Tools used: Python 3.x, Opencv, Xlib
<b>
<h3>Step 1:</h3><br>
1.Place the camera in such a way that it captures the projection screen.<br>
2.The projection on the screen must of the aspect ratio : (4:3), that is adjust the projector to 4:3 aspect ratio.<br>
3.Adjust the monitor's resolution to aspect ratio : (4:3)(This program uses 1024*768 resolution).<br>
4.Run the calibrator.py, which captures a frame of the projection screen.<br> 
5.Firstly double click on the top-left vertex of the projected area(You must only click on the vertex of the part of the screen which is projected, not the entire screen).<br>
6.You will get the x and y positions of the vertex. Note it down.<br>
7.Repeat step 5 for bottom-right vertex. Note down the x and y positions.<br>
8.Terminate the calibrator.py using escape key.<br>


<h3>step 2</h3><b><br>
1.Open the program pgm.py.<br>
2.Enter the range of colors to be detected in 'lower' and 'upper' variables in BGR format.<br>
3.Enter the x and y possitions for vertex1 and vertex2 in vertix1,vertiy1,vertix2,vertiy2 respectively.<br>
4.Run the program.<br>
You will be able to drive the mouse pointer by placing the coloured object over the projected area and dragging it.<br> 

You can terminate the program by pressing 'q' on keyboard.<br>


<h2>To get lower and upper BGR values for the colored object.</h2><br>
<b>
I used the site :<br>
https://www.colorcodepicker.com<br>

Here you can upload the image of the colored object(For good accuracy, use the same camera for both purposes.)<br>
Then you will get many RGB values from the image by clicking on different possition on the image.<br>
Note down RGB value for each position in the image.<br>

Then find the lowest and highest R value from the whole sample of RGB.Similarly find lower and upper values for G and B.<br>

Now you have lower RGB and upper RGB.(Note: You must enter the vales in reverse order ,i.e BGR format.)<br>


You can see my video in youtube were I used to drive particle effect using an orange glove.

Youtube: https://www.youtube.com/watch?v=Eip19nIOG24
