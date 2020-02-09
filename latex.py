import sympy as sp
import numpy as np
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image
import cv2

img = np.zeros((500, 500), dtype=np.uint8)
img.fill(255)

expr = "$\displaystyle \phi$"

#This creates a ByteIO stream and saves there the output of sympy.preview
f = BytesIO()
the_color = "{0.95}"
#sp.preview(expr, euler = False, preamble = r"\documentclass{standalone}"
	#r"\usepackage{pagecolor}"
	#r"\definecolor{graybg}{gray}" + the_color +
	#r"\pagecolor{graybg}"
	#r"\begin{document}",
	#viewer = "BytesIO", output = "ps", outputbuffer=f)
preamble = "\\documentclass[12pt]{standalone}\n" \
        "\\usepackage{amsmath,amsfonts}\\begin{document}"
#sp.preview(r'$\int_0^1 e^x\,dx$', euler = False, preamble=preamble, viewer = "BytesIO", output="png", outputbuffer=f)
sp.preview(r'$\int_0^1 e^x\,dx$', euler = False, viewer = "BytesIO", output="ps", outputbuffer=f)

f.seek(0)

#file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
#img = cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)
#res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#
#cv2.imshow("img", img)
#cv2.waitKey(0)
#f.close()

img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
#Open the image as if it were a file. This works only for .ps!
img1 = Image.open(f)
#See note at the bottom
img1.load(scale = 50)
img1 = img1.resize((int(img1.size[0]/2),int(img1.size[1]/2)),Image.BILINEAR)
img = np.array(img1)
f.close()

cv2.imshow("img", img)
cv2.waitKey(0)
