import copy
import random
# Consider using the modules imported above

# hat class - take a variable number of arguments that specify the number of balls of each color in the hat
# kwargs is keyword arguments
# ** means it should take any no. of kwargs
# list of strings: 1 item for each ball in hat


class Hat():

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  # draw method
  # argument = no. balls to draw from hate
  # remove balls at random from contents - return as list of strings
  # if no. draws > contents of hat, return balls to hat

  def draw(self, draws_from_hat):
    if draws_from_hat > len(self.contents):
      return self.contents
    drawn_balls = []
    for i in range(draws_from_hat):
      d = random.randrange(len(self.contents))
      drawn_balls.append(self.contents.pop(d))
    return drawn_balls


# experiment function outside hat class
# hat: A hat object containing balls that should be copied inside the function
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment
# num_balls_drawn: The number of balls to draw out of the hat in each experiment
# num_experiments: The number of experiments to perform
# deep copy creates a new compound object before inserting copies of the items found in the original into it in a recursive manner


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for j in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    experiment = new_hat.draw(num_balls_drawn)

    balls_drawn = []
    for key, value in expected_balls.items():
      for i in range(value):
        balls_drawn.append(key)

    match_ball = 0

    for i in balls_drawn:
      if i in experiment:
        experiment.remove(i)
        match_ball += 1

    if match_ball == len(balls_drawn):
      successes += 1

  if successes == 0:
    return 0
  else:
    return successes / num_experiments
