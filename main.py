import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip

def create_text_image(text, font_size, color, background_color, width, height):
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=50)
    _, _, w, h = draw.textbbox((0, 0), text)
    x = (width - w*4) // 2 
    y = (height - h*3 ) // 2
    draw.text((x, y), text, font=font, fill=color)
    return image

# Step 1: Load the video clip from URL
video_url = "https://file-examples.com/storage/fe3b4f721f64dfeffa49f02/2020/03/file_example_WEBM_480_900KB.webm"
video_clip = VideoFileClip(video_url)

text = "Welcome to Educative!"
font_size = 50
text_color = (255, 255, 255)  # White color
background_color = (0, 0, 0)  # Black background
width, height = video_clip.size
text_image = create_text_image(text, font_size, text_color, background_color, width, height)

# Convert the Pillow Image to a NumPy array
text_np = np.array(text_image)

final_clip = video_clip.fl_image(lambda frame: cv2.addWeighted(frame, 1, text_np, 0.5, 0))

for frame in final_clip.iter_frames(fps=final_clip.fps):
    cv2.imshow("Final Clip", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
