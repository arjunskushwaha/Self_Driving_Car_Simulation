# Self Driving Car Simulation
The project makes use of technique of **_Behavioural Cloning_** to train the model to drive a car on it's own.
Dataset for the training of the model was collected using [Udacity-Self-Driving-simulator](https://github.com/udacity/self-driving-car-sim) which is available for the major platforms (Linux / Windows / MacOS). The files also include a trained model i.e **_model.h5_**. Below is the detailed description about how the model was trained, preprocessing that was done on data and the video of the project in action where the model drives the car on its own.

**Section1** : Describes prerequisites for the project and how to run the project on your local machine.<br>
**Section2** : Describes in detail about every step done in project including the Neural Network model that was made in the project. 

## Section1: Getting Started

### Prerequisites

1. Download the simulator from [Udacity-Self-Driving-simulator](https://github.com/udacity/self-driving-car-sim#avaliable-game-builds-precompiled-builds-of-the-simulator).

2. Use your package manager to install `pip`.
```
    $ sudo apt-get update && sudo apt-get -y upgrade
    $ sudo apt-get install python-pip
```
3. Install the project dependecies:

    - Flask : ```$ pip install Flask```
    - Numpy : ``` $ pip install numpy```
    - SocketIO : ```$ pip install socketio``` 
    - Eventlet : ```$ pip install eventlet```
    - PIL : ```$ pip install Pillow```
    - Keras : ```$ pip install keras```
    - argparse : ```$ pip install argparse```

### Run Simulation
1. Clone the repository or [Download as zip](https://github.com/arjunskushwaha/Self_Driving_Car_Simulation/archive/master.zip). To clone it, type the following command in your terminal/Command Prompt (if you are boring and use Windows😜)<br>
```sh
     $ git clone https://github.com/arjunskushwaha/Self_Driving_Car_Simulation.git
     $ cd Self_driving_car_simulation/
```
2. Run the simulator.Choose the 'lake track' and click on Autonomous mode.<br>
3. Make sure your terminal is in the project directory and Run the python script **_"Run_Simulation.py"_** using the following command below:
```
    python Run_Simulation --path [provide the path to model.h5 file in the project] 
```

Note: 
- If it is not in same directory then execute this command first - ``` cd [path to the project folder] ```
- While running the above command, if you don't give command line arguments then script will look for the **_"model.h5"_** file in same directory as that of the script.

## Section2: Detailed Report

## Author

**[_Arjun Singh Kushwaha_]()** 

## Acknowledgments
### Inspirations 
- [MIT Technology Review](https://www.technologyreview.com/s/609503/the-open-source-driving-simulator-that-trains-autonomous-vehicles/)

### References
- [Introduction to Udacity Self-Driving Car Simulator](https://towardsdatascience.com/introduction-to-udacity-self-driving-car-simulator-4d78198d301d)
- [A Similar Project](https://github.com/suri97/Self-Driving-Car-Simulation)
