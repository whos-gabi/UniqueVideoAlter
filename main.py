#!/usr/bin/env python3.11
import os
import sys
from moviepy.editor import VideoFileClip, vfx
import random
import numpy as np

def alter_video(input_path, output_path):
    video = VideoFileClip(input_path)

    # Slightly adjust brightness
    video = video.fx(vfx.colorx, 1.01)

    # Change a single pixel in the first frame
    frame = video.get_frame(0)
    height, width, _ = frame.shape
    random_x = random.randint(0, width - 1)
    random_y = random.randint(0, height - 1)
    frame[random_y, random_x] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    
    # Function to modify the first frame
    def modify_first_frame(img):
        if np.array_equal(img, frame):
            return frame
        return img

    # Apply the frame modification to the video
    modified_video = video.fl_image(modify_first_frame)

    # Write the modified video to a file, preserving audio
    modified_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

def process_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"unique_{filename}")
            alter_video(input_path, output_path)
            print(f"Processed {filename}")
            # Delete the initial video
            os.remove(input_path)
            print(f"Deleted {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py folderWithMp4s/")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Provided path is not a directory")
        sys.exit(1)
    
    process_videos(folder_path)
