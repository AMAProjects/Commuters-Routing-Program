from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

#Start of building the program
landmark_string = ''
for letter, landmark in landmark_choices.items(): #.items() is used on a dictionary to access both the keys and values as pairs.
  landmark_string += '{0} - {1}\n'.format(letter, landmark)

def greet():
  print('Hi there and welcome to SkyRoute!')
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  greet()


def set_start_and_end(start_point, end_point): #This will handle setting the selected origin and destination points.
  if start_point != None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()

    elif change_point == 'o':
      start_point = get_start()
    
    elif change_point == 'd':
      end_point == get_end()
    
    else: #HANDLING USER INPUT ERRORS
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)

  else:
    start_point = get_start()
    end_point = get_end()
  
  return start_point
  return End_point


def get_start(): # will be used to request an origin from the user.
  start_point_letter = input('"Where are you coming from? Type the corresponding letter: ')

  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
  
  else:
    print("Sorry that's not a landmark we have data on. Let's try again...")
    get_start()
  
  return start_point

def get_end(): #to request and end from the user
  end_point_letter = input("Ok, where are you headed?: ")

  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]

  else:
    print("Sorry that's not a landmark we have data on. Let's try again...")
    get_end()
  
  return end_point


print(set_start_and_end(None, None))