from PIL import ImageDraw, ImageFont, Image
import cv2

text_to_show = "testing 123"

image = cv2.imread('./img/auto/S03E02 - 2557209.png')

# Convert the image to RGB (OpenCV uses BGR)  
cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  

# Pass the image to PIL  
pil_im = Image.fromarray(cv2_im_rgb)  

draw = ImageDraw.Draw(pil_im)  
# use a truetype font  
font = ImageFont.truetype("PAPYRUS.ttf", 80)  

# Draw the text  
draw.text((10, 700), text_to_show, font=font, fill='#FFFFFF')  

# Get back the image to OpenCV  
cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  

# cv2.imshow('Fonts', cv2_im_processed)  
# cv2.waitKey(0)  
cv2.imwrite('output.png', image)

cv2.destroyAllWindows()  