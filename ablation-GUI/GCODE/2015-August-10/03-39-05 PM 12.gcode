;(***************uWellPlate******************)
;(*** Monday, August 10, 2015 @ 03:39:05 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G28
G0 X6 Y7 F2000
G0 Z121.1 F300
G1 X-8 S1.0 L2000 P0.2 F4 B1
G0 X5.5 Y-4.33 F1000
G4 P10
G1 X-8 S1.0 L2000 P0.2 F4 B1
G0 X10.5 Y-4.33 F1000
G4 P10
G1 X-8 S1.0 L2000 P0.2 F4 B1
G0 X5.5 Y-4.33 F1000
G4 P10

;; Cleaning

M3 S0
G90
G0 X232 Y335 F1000
G4 P250
G0 Y255 F1000
G4 P250
G0 Y335 F1000
G4 P250
G0 X3.5 Y-5.99 F1000
G4 P500
G91
;; Done Cleaning


;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
