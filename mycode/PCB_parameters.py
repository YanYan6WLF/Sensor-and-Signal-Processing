# PCB_coils_v1
import numpy as np

track_thickness = 140 * 1e-3  # 140um = 4oz
track_width = 0.902  # mm
DOUT = 195.5  # mm
DIN = 6.6  # mm
L = DOUT / 2. - DIN / 2.

number_of_layers = 4
turn_per_layer = 74

A = number_of_layers * turn_per_layer * track_width * track_thickness
Hcoil = A / L

current = 2
jcoil = current / (track_width * track_thickness)

print(A)
print(L)
print(Hcoil)
print(jcoil)
