# Maze Solver: Platform for training a maze solver </h1>

This is side-project where I have designed an environment to test out Reinforcement Learning techniques. A maze is generated using a cli, then an agent will start moving within the environemnt. The data obtained from the agent will be stored so its performance could be improved using Machine Learning models.

<p align="center">
  <img src="/img/entry_point.png" width=80% height=80% alt="Demo"/>
</p>

# Graphics

PyGame is used to render the graphics of the project alongside interactive cli properties.

- ```Testing the basic functionality.```
- ```Choose between user/computer mode.```
- ```Choose the dimensions of the map.```

# Command Line

Command Line Interface could be accessed through the terminal where first the user is prompted to enter information about the Maze properties. Then a randomly generated maze will appear with a moving agent.

### CLI commands
- `x`: Pauses the movement.
- `space`: Resets the map.
- `r`: resets the map and the object.

# This project has two partitions:
Partition 01: Environment| Partition 02: Agent
---------------------------- | ----------------------------
Generates a random maze with graphics | Travels through the maze and tries to optimize it's movement by gathering data about the map.
Monitors the movements of the second partion. | It stores the data it has collected and makes its dicisions based on the previous trials
Acts as an supervisor to the second partion but does not interfere | Acts as the learner and it gets smarter in a way to optimize it's path.

<br />

### Partion 01: 
By the use of the modules in Map, Consts  and the utilties in the  utility folder, there is a map generated.
      Markup : <details>
                 <summary>Map</summary>
                 <p align="center">
                  In this module, there is a 2D array of <b>0's</b> and <b>1's</b> produced and based on this array 
                  the gets generated. 
                 </p>
               </details>
               <details>
                 <summary>Utilities</summary>
                 <p align="center">
                  In this directory, there are constant variables and as well as some loggings that are stored to 
                  help the user interact with the platform.
                 </p>
               </details>

### Partion 02:
<p align="left">
  They are two main aspects to the mover module(which controls the self-learning partition.). The first one is that
  it goes through the map and records its own moves and mistakes(when it ends up in a deadend). The second part is where it     decides what to do based on the previously collected data, in other words by doing analysis on the data, it tries to avoid
  making the old mistakes and in other words, it learns.
</p>

The schema for stored data:
```python
path_info = {
  "coor": (self.x, self.y),
  "options": [d for d in dirs if self.possible_moves[d] and not (d in self.visited)],
  "move_type": [dir]
}
```

<h6> Which can be visualised as: </h6>
<p align="center">
  <img src="/img/demo.png" width=90% height=90% alt="Demo" />
</p>
