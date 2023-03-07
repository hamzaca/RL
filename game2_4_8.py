import random
import numpy as np

# for actions : {"up":0, "down":1, "left":2, "right":3 } 
class Game:

	def __init__(self, game_size = 3):

		assert isinstance(game_size, int), "game_size must be an integer"
		self.empty_value = 0
		self.space_shape = (game_size, game_size)
		self.action_space = spaces.Discrete(4)

		initial_space = np.full(self.space_shape, self.empty_value)
		row = np.random.randint(game_size)
		col = np.random.randint(game_size)
		initial_space[row, col] = random.choices([2,4], weights= [4/5, 1/5])


		self.observation_space = spaces.Box(shape=self.space_shape, 
		                                    initial_state=initial_space)

	def add_num_to_space(self):
		"""Add 2 or 4 randomly to the empty space in the space self.observation_spacerix """

		nb_to_add = random.choice([2,4])

		# Add where
		rows_indices, cols_indices = self.find_empty_spaces()
		index = random.randint(len(rows_indices))
		row_chosen,col_chosen = rows_indices[index],cols_indices[index]
		# add value to self.observation_spacerix
		self.observation_space[row_chosen, col_chosen] = nb_to_add

	def find_empty_spaces(self):
		return np.where(self.observation_space == self.empty_value)

	def step(self, action_taken):

		if action_taken==0:
			self.step_up()

		elif action_taken==1:
			self.step_down()
		
		elif action_taken==2:
			self.step_left()
		
		else :
			self.step_right()


	def step_up(self):

		
		def shift_up():
			# count the number of non-zero elements in each column
			num_non_zero = np.count_nonzero(self.observation_space, axis=0)
			# generate the modified self.observation_spacerix
			next_observation_space = np.zeros_like(self.observation_space)
			for col in range(self.observation_space.shape[1]):
			    non_zero = self.observation_space[:, col][self.observation_space[:, col] != self.empty_value]
			    next_observation_space[:len(non_zero), col] = non_zero

			self.observation_space=next_observation_space

		shift_up()

		# Sum sames values
		col_mask = self.observation_space[:-1, :] == self.observation_space[1:, :]
		col_values = self.observation_space[:-1, :][col_mask]
		row_indices, col_indices = np.where(col_mask == True)
		row_col_indices = list(zip(row_indices, col_indices))
		for row_index, col_index in row_col_indices:
		    self.observation_space[row_index][col_index]= self.observation_space[row_index][col_index]+self.observation_space[row_index+1][col_index]
		    self.observation_space[row_index+1][col_index] = self.empty_value

		shift_up()


	def step_down(self):

		
		def shift_down():
			# count the number of non-zero elements in each column
			num_non_zero = np.count_nonzero(self.observation_space, axis=0)
			# generate the modified self.observation_spacerix
			next_observation_space = np.zeros_like(self.observation_space)
			for col in range(self.observation_space.shape[1]):
			    non_zero = self.observation_space[:, col][self.observation_space[:, col] != self.empty_value]
			    next_observation_space[:len(non_zero), col] = non_zero

			self.observation_space=next_observation_space

		shift_down()

		# Sum sames values
		col_mask = self.observation_space[:-1, :] == self.observation_space[1:, :]
		col_values = self.observation_space[:-1, :][col_mask]
		row_indices, col_indices = np.where(col_mask == True)
		row_col_indices = list(zip(row_indices, col_indices))
		for row_index, col_index in row_col_indices:
		    self.observation_space[row_index][col_index]= self.observation_space[row_index][col_index]+self.observation_space[row_index+1][col_index]
		    self.observation_space[row_index+1][col_index] = self.empty_value

		shift_down()
		    
		    



		








