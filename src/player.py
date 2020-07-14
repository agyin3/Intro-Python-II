# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
    
    def set_curr_room(self, room):
        self.curr_room = room
