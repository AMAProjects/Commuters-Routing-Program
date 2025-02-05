from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

#Start of building the program
landmark_string = ''
for letter, landmark in landmark_choices.items(): #.items() is used on a dictionary to access both the keys and values as pairs.
  landmark_string += '{0} - {1}\n'.format(letter, landmark)