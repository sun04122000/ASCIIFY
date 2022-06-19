import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg = "black"
# bg = "black"
if bg == "white":
    bg_code = (255, 255, 255)
elif bg == "black":
    bg_code = (0, 0, 0)

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 100

cap = cv2.VideoCapture(0)
while cap.isOpened():

    flag, frame = cap.read()
    # Reading Input Image
    if flag:
        # Converting Color Image to Grayscale
        #image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image=frame
    else:
        break

    fps=int(0.1*cap.get(cv2.CAP_PROP_FPS))
    # Extracting height and width from Image
    height, width, _ = image.shape

    # Defining height and width of each cell==pixel
    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h)

    # Calculating Height and Width of the output Image
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = scale * char_height * num_rows

    # Making a new Image using PIL
    out_image = Image.new("RGB", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)

    # Mapping the Characters
    for i in range(num_rows):
        min_h = min(int((i + 1) * cell_h), height)
        row_pix = int(i * cell_h)
        

        # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
        # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
        for j in range(num_cols):
            partial_image = image[int(i * cell_h):min(int((i + 1) * cell_h), height),
                                int(j * cell_w):min(int((j + 1) * cell_w), width), :]
            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cell_h * cell_w)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
            line = char_list[
                min(int(
                    np.mean(partial_image) / 255 * num_chars
                ), num_chars - 1)]
                 
        
        # Draw string at a given position (x,y)
            draw.text((j*char_width, i * char_height), line, fill=partial_avg_color, font=font)
      
    # Inverting Image and removing excess borders
    if bg == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    elif bg == "black":
        cropped_image = out_image.getbbox()

    # Saving the new Image
    out_image = out_image.crop(cropped_image)
    #out_image = cv2.cvtColor(np.array(out_image), cv2.COLOR_GRAY2BGR)
    out_image = np.array(out_image)
    # print(out_image.size)
    try:
        out
    except:
        out = cv2.VideoWriter('./data/l_output.avi', cv2.VideoWriter_fourcc(*"XVID"), fps,((out_image.shape[1], out_image.shape[0])))
    
    overlay_ratio=0.2
    if overlay_ratio:
            height, width, _ = out_image.shape
            overlay = cv2.resize(frame, (int(width * overlay_ratio), int(height * overlay_ratio)))
            out_image[height - int(height * overlay_ratio):, width - int(width * overlay_ratio):, :] = overlay
    out.write(out_image)
    cv2.imshow('frame',out_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #print(out_image.shape)
cap.release()
out.release()
cv2.destroyAllWindows()
