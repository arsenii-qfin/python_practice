import math

AB = int(input())
BC = int(input())

AC = math.sqrt(AB**2 + BC**2)
MC = AC / 2

thetaR = math.acos(BC / AC)

thetaD = round(math.degrees(thetaR))

print(thetaD, chr(176), sep='')

