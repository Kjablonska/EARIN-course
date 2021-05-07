Introduction to Artificial Intelligence summer 2021 - exercise 5
Karolina Jabłońska
Wojciech Marosek

To run&build:
The program requires python 3 to be executed.

In order to run:
Go to the folder containing project files and type in the terminal:
    python3 tui.py

Program will ask you then to specifty the variables:
1. User must specify .json file name. All JSON files must be stored under ../assts directory.
    At this point, the program parses JSON and validates the correctness of the network. If it raises error, the program will not proceed.

2. User can select to run MCMC sampling algorithm.
    Then, program variables must be specified:
    * evidences
    * queries
    * steps - number of steps for MCMC sampling algorithm

3. User can select to run Markov Blanket.
    Then, program variables must be specified:
    * node name for which Markov Blanket will be printed.

After program execution ended, it asks user to run the selected method again or input new variables.

Attention!
Given evidence value must be set in the same way as probabilites!
For instance:
alarm.json  =>  evidence={"burglary": "T", "alarm": "T"}
flower.json =>  evidence={"flower_species": "rose"}