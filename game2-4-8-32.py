import gymnasium as gym
from gymnasium import spaces


class Env2_4_8_32(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, game_size = 3):
    super(CustomEnv, self).__init__()

    assert isinstance(game_size, int)
    self.game_size = game_size
    self.action_space = spaces.Discrete(["up", "down", "left","right"])
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
                    (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

  def step(self, action):
    # Execute one time step within the environment
    ...
  def reset(self):
    # Reset the state of the environment to an initial state
    ...
  def render(self, mode='human', close=False):
    # Render the environment to the screen
