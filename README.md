<h1 align="center">HM0-01: Platform for training a maze solver </h1>

<p align="center">
  <img src="/img/demo00.png" alt="Demo"/>
 </p>
 
- Testing the basic functionality.
- Choose between user/computer mode.
- Choose the dimensions of the map.

# This project has two partitions:
Pt 01: The computer side | Pt 02: The **self-learning** side
----------------------- | ----------------------- 
Generates a random maze with graphics | Travels through the maze and tries to optimize it's movement by gathering data about the map.
Monitors the movements of the second partion. | It stores the data it has collected and makes its dicisions based on the previous trials
Acts as an supervisor to the second partion but does not interfere | Acts as the learner and it gets smarter in a way to optimize it's path.

## `It tracks the movements:`
<p align="center">
  <img src="/img/demo.png" alt="Demo" />
</p>
