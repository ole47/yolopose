import shutil
import os
import random


parent_dir_frames = "/itf-fi-ml/home/olekrus/master/master/frames_for_training/"
parent_dir_txt = "/itf-fi-ml/home/olekrus/master/master/labels_frames_for_training/keypoints/txt/"

frame_files = sorted(os.listdir(parent_dir_frames)) #Alphabetical order
txt_files = sorted(os.listdir(parent_dir_txt)) #alphabetical order

outcome = [0, 1, 2]
weights = [0.7, 0.15, 0.15]  # 70% chance for 0, 15% chance for 1, 15% chance for 2

train_folder = "/itf-fi-ml/home/olekrus/master/master/Data/train/"
val_folder = "/itf-fi-ml/home/olekrus/master/master/Data/val/"
test_folder = "/itf-fi-ml/home/olekrus/master/master/Data/test/"

for file_ind in range(len(frame_files)):
    if frame_files[file_ind].endswith(".png"):
        train_val_test = random.choices(outcome, weights=weights, k=1)[0]
        if train_val_test == 0: #Train
            shutil.move(parent_dir_frames + frame_files[file_ind], train_folder + "images/" + frame_files[file_ind])
            shutil.move(parent_dir_txt + txt_files[file_ind], train_folder + "labels/" + txt_files[file_ind])

        elif train_val_test == 1: #Val
            shutil.move(parent_dir_frames + frame_files[file_ind], val_folder + "images/" + frame_files[file_ind])
            shutil.move(parent_dir_txt + txt_files[file_ind], val_folder + "labels/" + txt_files[file_ind])

        else: #Test
            shutil.move(parent_dir_frames + frame_files[file_ind], test_folder + "images/" + frame_files[file_ind])
            shutil.move(parent_dir_txt + txt_files[file_ind], test_folder + "labels/" + txt_files[file_ind])