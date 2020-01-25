<h1 align="center">HM0-01: Platform for training a maze solver </h1>

<p align="center">
  <img src="/img/entry_point.png" width=80% height=80% alt="Demo"/>
 </p>
 
- Testing the basic functionality.
- Choose between user/computer mode.
- Choose the dimensions of the map.

<h5> Platform variables: </h5>
<ul>
  <li><p background-color: #FFFF00>x</p>: Pauses the movement.</li>
  <li>`space`: Resets the map.</li>
  <li>`r`: resets the map and the object.</li>
</ul>


# This project has two partitions:
Partition 01: Computer| Partition 02: The **self-learning** side
---------------------------- | ----------------------------
Generates a random maze with graphics | Travels through the maze and tries to optimize it's movement by gathering data about the map.
Monitors the movements of the second partion. | It stores the data it has collected and makes its dicisions based on the previous trials
Acts as an supervisor to the second partion but does not interfere | Acts as the learner and it gets smarter in a way to optimize it's path.

## `It tracks the movements:`
<p align="center">
  <img src="/img/demo.png" width=80% height=80% alt="Demo" />
</p>

- Gets the co-ordinates and the movement that has been done from that co-ordinate.
