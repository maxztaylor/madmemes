import cv2
import os
from random import randrange
from PIL import ImageDraw, ImageFont

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
        cv2.imwrite(os.path.join(path_output_dir, '%s - %d.png') % (filename_prefix, rand_ms), image)
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

def memegen():

    num_memes = int(input("How many memes do you want?\n"))

    for i in range(num_memes):
        video_input = random_file('../../Shared Media/TV/Mad Men')

        season_ep = extract_season_ep(video_input)

        video_to_frames(video_input, './img/auto', season_ep)

    print("Your %d memes are ready!" % num_memes)

memegen()