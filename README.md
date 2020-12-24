# Reinforcement Learning (RL) Tutorial

This is my own examination and implementation of the [Reinforcement Learning with Python Tutorial](https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/) from [sentdex](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ).

Content list:
- [Part 1 - Q-Learning introduction and Q Table](https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/) ([video](https://youtu.be/yMk_XtIEzH8))
- [Part 2 - Q Algorithm and Agent (Q-Learning)](https://pythonprogramming.net/q-learning-algorithm-reinforcement-learning-python-tutorial/) ([video](https://youtu.be/Gq1Azv_B4-4))
- [Part 3 - Q-Learning Analysis](https://pythonprogramming.net/q-learning-analysis-reinforcement-learning-python-tutorial/) ([video](https://youtu.be/CBTbifYx6a8))
- [Part 4 - Q-Learning In Our Own Custom Environment](https://pythonprogramming.net/own-environment-q-learning-reinforcement-learning-python-tutorial/) ([video](https://youtu.be/G92TF4xYQcU))
- [Part 5 - Deep Q Learning and Deep Q Networks (DQN) Intro and Agent](https://pythonprogramming.net/deep-q-learning-dqn-reinforcement-learning-python-tutorial/) ([video](https://youtu.be/t3fbETsIBCY))
- [Part 6 - Training Deep Q Learning and Deep Q Networks (DQN) Intro and Agent](https://pythonprogramming.net/training-deep-q-learning-dqn-reinforcement-learning-python-tutorial/) ([video](https://youtu.be/qfovbG84EBg))

***Note:*** some of the parts were squashed for simplicity

## How to run

### Setup

Makefile contains helper commands to create [virtual environment](https://docs.python.org/3.8/library/venv.html) 
and install requirements

```shell script
make venv
source venv/bin/activate
make update
``` 

### Run code

Activate virtual environment and run one of the tutorial files

```shell script
source venv/bin/activate
python3.8 rl_tutorial/rl1_qlearning_intro.py
```
