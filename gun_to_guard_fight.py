
'''Bringing a Gun to a Guard Fight
===============================
Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a
beam weapon from an abandoned guardpost while you were running through the station, so you have a
chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to
the elite guard: its beams reflect off walls, meaning youll have to be very careful where you
shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause
damage. You also know that if a beam hits a corner, it will bounce back in exactly the same
direction. And of course, if the beam hits either you or the guard, it will stop immediately
(albeit painfully). 

Write a function answer(dimensions, your_position, guard_position, distance) that gives an array
of 2 integers of the width and height of the room, an array of 2 integers of your x and y
coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room,
and returns an integer of the number of distinct directions that you can fire to hit the elite
guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1000, 1 < y_dim <= 1000]. You and the elite guard
are both positioned on the integer lattice at different distinct positions (x, y) inside the room
such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel
before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2],
you_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in
seven different directions to hit the elite guard (given as vector bearings from your location):
[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot
at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2]
bounces off the left wall and then the bottom wall before hitting the elite guard with a total
shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before
hitting the elite guard with a total shot distance of sqrt(5).'''

from __future__ import division
import math, fractions

def add_room(dim, position, x_disp, y_disp):
    new_position = [position[0] + dim[0] * (x_disp - x_disp % 2) + 2 * (x_disp % 2) * (dim[0] - position[0]),
                        position[1] + dim[1] * (y_disp - y_disp % 2) + 2 * (y_disp % 2) * (dim[1] - position[1])]
    return new_position

def add_rooms(dim, your_pos, guard_pos, dist):
    your_pos_lst, guard_pos_lst = [], []
    x_range, y_range = int(math.ceil(dist / dim[0])), int(math.ceil(dist / dim[1]))
    for x_disp in range(-x_range, x_range + 1):
        for y_disp in range(-y_range, y_range + 1):
            your_pos_lst.append(add_room(dim, your_pos, x_disp, y_disp))
            guard_pos_lst.append(add_room(dim, guard_pos, x_disp, y_disp))
    return your_pos_lst, guard_pos_lst

def shots(your_pos, lst, dist):
    shot_vectors = {}
    for position in lst:
        shot = (position[0] - your_pos[0], position[1] - your_pos[1])
        shot_dist = math.sqrt(shot[0]**2 + shot[1]**2)
        if shot_dist <= dist:
            divisor = abs(fractions.gcd(shot[0],shot[1]))
            try:
                shot = (shot[0]/divisor,shot[1]/divisor)
            except:
                pass
            try:
                if shot_dist > shot_vectors[shot]: continue
            except:
                pass
            shot_vectors[shot] = shot_dist
    return shot_vectors

def answer(dim, your_pos, guard_pos, dist):
    your_pos_lst, guard_pos_lst = add_rooms(dim,your_pos, guard_pos, dist)
    shot_yourself = shots(your_pos, your_pos_lst, dist)
    shot_guard = shots(your_pos, guard_pos_lst, dist)
    return len([shot for shot in shot_guard
                    if shot not in shot_yourself or shot_guard[shot] < shot_yourself[shot]])

def test():
    assert answer([3,2],[1,1],[2,1],4) == 7, "Test case 1 failed"
    assert answer([300,275],[150,150],[185,100],500) == 9, "Test case 2 failed"
    return "All test cases passed"

print test()