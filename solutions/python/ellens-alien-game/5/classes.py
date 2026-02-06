"""Solution to Ellen's Alien Game exercise."""
class Alien:
    health = 3
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        pass

def new_aliens_collection(new_aliens) :
    alien_list = []
    for x_coordinate, y_coordinate in new_aliens :
        alien = Alien(x_coordinate, y_coordinate)
        alien_list.append(alien)
    return alien_list
    