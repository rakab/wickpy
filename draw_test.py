import cv2
import numpy as np
def convert_arc(pt1, pt2, sagitta):
    # extract point coordinates
    x1, y1 = pt1
    x2, y2 = pt2

    # find normal from midpoint, follow by length sagitta
    n = np.array([y2 - y1, x1 - x2])
    n_dist = np.sqrt(np.sum(n**2))

    if np.isclose(n_dist, 0):
        # catch error here, d(pt1, pt2) ~ 0
        print('Error: The distance between pt1 and pt2 is too small.')

    n = n/n_dist
    x3, y3 = (np.array(pt1) + np.array(pt2))/2 + sagitta * n

    # calculate the circle from three points
    # see https://math.stackexchange.com/a/1460096/246399
    A = np.array([
        [x1**2 + y1**2, x1, y1, 1],
        [x2**2 + y2**2, x2, y2, 1],
        [x3**2 + y3**2, x3, y3, 1]])
    M11 = np.linalg.det(A[:, (1, 2, 3)])
    M12 = np.linalg.det(A[:, (0, 2, 3)])
    M13 = np.linalg.det(A[:, (0, 1, 3)])
    M14 = np.linalg.det(A[:, (0, 1, 2)])

    if np.isclose(M11, 0):
        # catch error here, the points are collinear (sagitta ~ 0)
        print('Error: The third point is collinear.')

    cx = 0.5 * M12/M11
    cy = -0.5 * M13/M11
    radius = np.sqrt(cx**2 + cy**2 + M14/M11)

    # calculate angles of pt1 and pt2 from center of circle
    pt1_angle = 180*np.arctan2(y1 - cy, x1 - cx)/np.pi
    pt2_angle = 180*np.arctan2(y2 - cy, x2 - cx)/np.pi

    return (cx, cy), radius, pt1_angle, pt2_angle

def draw_ellipse(
        img, center, axes, angle,
        startAngle, endAngle, color,
        thickness=1, lineType=cv2.LINE_AA, shift=10):
    # uses the shift to accurately get sub-pixel resolution for arc
    # taken from https://stackoverflow.com/a/44892317/5087436
    center = (
        int(round(center[0] * 2**shift)),
        int(round(center[1] * 2**shift))
    )
    axes = (
        int(round(axes[0] * 2**shift)),
        int(round(axes[1] * 2**shift))
    )
    return cv2.ellipse(
        img, center, axes, angle,
        startAngle, endAngle, color,
        thickness, lineType, shift)

img = np.zeros((500, 500), dtype=np.uint8)
img.fill(255)
pt1 = (50, 200)
pt2 = (350, 200)
sagitta = 100

center, radius, start_angle, end_angle = convert_arc(pt1, pt2, sagitta)
axes = (radius, radius)
draw_ellipse(img, center, axes, 0, start_angle, end_angle, 0)

center, radius, start_angle, end_angle = convert_arc(pt1, pt2, -100)
axes = (radius, radius)
draw_ellipse(img, center, axes, 0, start_angle, end_angle, 0)

center, radius, start_angle, end_angle = convert_arc(pt1, pt2, 50)
axes = (radius, radius)
draw_ellipse(img, center, axes, 0, start_angle, end_angle, 0)

center, radius, start_angle, end_angle = convert_arc(pt1, pt2, -50)
axes = (radius, radius)
draw_ellipse(img, center, axes, 0, start_angle, end_angle, 0)

cv2.circle(img, (50,200), 5, (0,0,0), -1)
cv2.circle(img, (350,200), 5, (0,0,0), -1)

# polar equation
theta = np.linspace(-np.pi, np.pi, 3000)
r = 20+30/np.cosh(3*(theta+np.pi/2))
x = r * np.cos(theta)
y = r * np.sin(theta)
c, s = np.cos(np.pi/2), np.sin(np.pi/2)
R = np.array(((c, s), (s, c)))
points = np.vstack((x,y)).T
minn=-points.min(0)[1]
for i,p in enumerate(points):
    points[i] = R@p.T
    points[i][0] += 350+minn
    points[i][1] += 200
print(points)
cv2.polylines(img, np.int32([points]), 0, (0,0,0),1,lineType=cv2.LINE_AA)

cv2.imshow('', img)
cv2.waitKey()
