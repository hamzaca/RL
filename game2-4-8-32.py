import gymnasium as gym
from gymnasium import spaces
import random


class Env2_4_8_32(gym.Env):

  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, game_size = 3):
    super(CustomEnv, self).__init__()

    assert isinstance(game_size, int)
    self.game_size = game_size
    self.space_shape = (game_size, game_size)
    self.action_space = spaces.Discrete(4)

    initial_space = np.full(elf.space_shape, -1)
    row = np.random.randint(game_size)
    col = np.random.randint(game_size)
    initial_space[row, col] = random.choices([2,4], weights= [4/5, 1/5])


    self.observation_space = spaces.Box(shape=self.space_shape, 
                                        initial_state=initial_space)

  def step(self, action):
    # Execute one time step within the environment


  def reset(self):
    # Reset the state of the environment to an initial state


  def render(self, mode='human', close=False):
    # Render the environment to the screen
