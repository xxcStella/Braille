import pickle
import numpy as np

with open("D:\PersonalFiles\Bristol\GraduationThesis\Code/Events_Examples/taps_pin_separation_pose_0_tap_0.pickle", "rb") as file:
    data = pickle.load(file)

print(data.shape)

cnt=0
for iy in range(data.shape[0]):
    for ix in range(data.shape[1]):
        if data[iy,ix] != []:
            print(data[iy,ix])
            # cnt += 1


# print(cnt)
"""
[[[], [12], [14,25]],
 [[], [], []],
 [[], [], []],
 [[], [], []],]
"""