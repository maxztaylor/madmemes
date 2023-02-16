import cv2
import os
import pandas as pd
from random import randrange, getrandbits
from PIL import Image,ImageDraw, ImageFont
import textwrap

def video_to_frames(video, path_output_dir, filename_prefix):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)

    # count the number of frames
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
  
    # calculate duration of the video
    total_ms = round(frames / fps) * 1000

    # pick a random moment
    rand_ms = randrange(total_ms)

    # set the video time to that random moment and save the image
    vidcap.set(0,rand_ms)

    success, image = vidcap.read()
    if success:
        # cv2.imwrite(os.path.join(path_output_dir, '%s - %d.png') % (filename_prefix, rand_ms), image)
        return image
    else:
        print('ERROR! Womp womp')

    cv2.destroyAllWindows()
    vidcap.release()

def random_file(root_directory):
    dir_list = os.listdir(root_directory)
    dir_list.remove('.DS_Store')

    rand_dir = dir_list[randrange(len(dir_list))]
    dir_path = root_directory + '/' + rand_dir
    file_list = os.listdir(dir_path)
    rand_file = file_list[randrange(len(file_list))]
    rand_file_path = dir_path + '/' + rand_file

    return rand_file_path

def extract_season_ep(path_name):
    findstring = 'Mad Men (2007) - '

    stringstart = path_name.find(findstring)
    se_start = stringstart + len(findstring)
    se_end = se_start + 6
    extracted_season_ep = path_name[se_start:se_end]

    return extracted_season_ep

def memetext(img, toptext, bottomtext, filename):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Impact.ttf", 120)

    width, height = img.size

    max_width = 34

    top_text = textwrap.fill(str(toptext).upper(), width=max_width)
    bottom_text = textwrap.fill(str(bottomtext).upper(), width=max_width)

    if(bool(getrandbits(1))):
        draw.text((width/2, 10), top_text, font=font, stroke_width=2, stroke_fill="black", align="center", anchor="ma")

    draw.text((width/2, height - 10), bottom_text, font=font, stroke_width=2, stroke_fill="black", align="center", anchor="md")

    img.save('./img/auto/' + filename + '.png', "PNG")

def cv2_pil_conv(image):
    image_conv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(image_conv)

def randtext():
    scripts_filename = './scripts/all_scripts.tsv'
    df_scripts = pd.read_csv(scripts_filename, sep='\t')
    line_count = len(df_scripts)
    text_num = randrange(line_count)
    return df_scripts.loc[text_num, 'Text']

def memegen():
    # num_memes = int(input("How many memes do you want?\n"))
    num_memes = 1

    for i in range(num_memes):
        video_input = random_file('../../Shared Media/TV/Mad Men')
        season_ep = extract_season_ep(video_input)

        frame = video_to_frames(video_input, './img/auto', season_ep)

        top_text = randtext().rstrip(".")
        bottom_text = randtext().rstrip(".")

        image_pil = cv2_pil_conv(frame)

        memetext(image_pil, top_text, bottom_text, 'filename')

    # print("Your %d memes are ready!" % num_memes)

memegen()