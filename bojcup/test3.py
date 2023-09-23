import math
import sys
input = sys.stdin.readline

global finalAverageX
global finalAverageY

n = int(input()) #입력값
def sortPointsClockwise(points):
    averageX = 0
    averageY = 0
    for point in points:
        averageX += point[0]
        averageY += point[1]
    finalAverageX = averageX / len(points)
    finalAverageY = averageY / len(points)
    points.sort(key=lambda point: math.atan2(point[1] - finalAverageY, point[0] - finalAverageX))

points = []
for k in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print("=== Clockwise sort ===")
sortPointsClockwise(points)
for point in points:
    print(point[0], point[1])

print("=== Counter Clockwise sort ===")
points.sort(key=lambda point: math.atan2(point[1] - finalAverageY, point[0] - finalAverageX), reverse=True)
for point in points:
    print(point[0], point[1])