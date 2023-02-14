import urllib.request
import cv2
import numpy as np

# Load image from URL
url = "https://example.com/image.jpg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as url_response:
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

# Add text to the image
text = "Hello World!"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_pos = (img.shape[1] // 2 - text_size[0] // 2, img.shape[0] - 50)
cv2.putText(img, text, text_pos, font, font_scale, (255, 255, 255), thickness)

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
