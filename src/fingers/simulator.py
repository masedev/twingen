import logging
import time
import random
import matplotlib.pyplot as plt
import os
import json
from utils.logger import Logger
from datetime import datetime

current_datetime = datetime.now() # log file datetime is isolated for the container startup process

filename = os.environ.get('DATAFILE') if os.environ.get('DATAFILE') is not None else os.path.join(os.path.dirname(__file__), "data", "finger_movements.json")
log_path = os.path.join(os.path.dirname(__file__), "../logs")

""" if os.environ.get('ENV') is None:
    print('error during inizialization of the fingers simulator, environment variable not defined')
    exit(-1)

env = os.environ.get('ENV') """
env = 'dev'

if not os.path.exists(log_path):
    os.makedirs(log_path)

class FingersSimulator:
    def __init__(self, num_fingers=5):
        self.num_fingers = num_fingers
        self.finger_positions = [0.0] * num_fingers
        self.pressure_values = [0.0] * num_fingers
        self.time_steps = []
        self.finger_positions_history = [[] for _ in range(num_fingers)]
        self.logger = Logger(log_dir=log_path, log_filename=f'{current_datetime}.log', log_level=logging.INFO)

    def update_finger_positions(self):
        for i in range(self.num_fingers):
            self.finger_positions[i] += random.uniform(-0.1, 0.1)

    def update_pressure_values(self):
        for i in range(self.num_fingers):
            self.pressure_values[i] = max(0.0, min(1.0, self.pressure_values[i] + random.uniform(-0.1, 0.1)))

    def generate_hand_data(self):
        hand_data = {
            'finger_positions': self.finger_positions.copy(),
            'pressure_values': self.pressure_values.copy()
        }
        return hand_data

    def record_history(self):
        self.time_steps.append(time.time())
        for i in range(self.num_fingers):
            self.finger_positions_history[i].append(self.finger_positions[i])

    def save_history_to_file(self):
        data = {
            'time_steps': self.time_steps,
            'finger_positions_history': self.finger_positions_history
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        

    def visualize_movement(self):
        for i in range(self.num_fingers):
            plt.plot(self.time_steps, self.finger_positions_history[i], label=f'Finger {i + 1}')

        plt.xlabel('Time (s)')
        plt.ylabel('Finger Positions')
        plt.legend()
        plt.show()

def run(duration : int, frequency : int, step_frequency : int):
    # hand simulator provides a robotic hands for finger movements 
    hand_simulator = FingersSimulator()

    # TODO: add the fingers driver for inbound and outbound communication
    while True:
        start_time = time.time()
        while time.time() - start_time < duration:
            # Update finger positions and pressure values according to the linear variation  
            hand_simulator.update_finger_positions()
            hand_simulator.update_pressure_values()

            hand_simulator.record_history()
            hand_data = hand_simulator.generate_hand_data()
            hand_simulator.logger.info(hand_data)

            time.sleep(frequency)

        time.sleep(step_frequency)

if __name__ == "__main__":
    run(30, 10, 20)
