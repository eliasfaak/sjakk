import gym
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

LR = 0.001
env = gym.make('CartPole-v0')
env.reset()
goal_steps=200
score_requirement = 50
initial_games = 10000

def some_random_games_first():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                break

#some_random_games_first()


def intial_population():
    training_data = []
    scores = []
    accepted_scores = []
    output = []
    for i in range(initial_games):
        score = 0
        game_memory = []
        prev_observation = []
        for j in range(goal_steps):
            action = random.randrange(0,2)
            observation, reward, done, info = env.step(action)

            if len(prev_observation) > 0:
                game_memory.append(prev_observation)

            prev_observation = observation
            score += reward
            if done:
                break

        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0,1]
                elif data[1] == 0:
                    output = [1,0]
            training_data.append([data[0], output])
        env.reset()
        scores.append(score)
    training_data_save = np.array(training_data)
    print('average accepted score', mean(accepted_scores))
    print('median accepted score', median(accepted_scores))

intial_population()
