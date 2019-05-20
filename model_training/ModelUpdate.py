import os
import glob
import shutil
import time
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
import ModelTrain

# copy all file to history
def copy_rename(old_file_name, new_file_name):
    dst_dir = 'model_training/history'
    # copy
    src_file = 'model_training/' + old_file_name
    shutil.copy(src_file, dst_dir)
    # rename
    dst_file = dst_dir + '/' + old_file_name
    new_dst_file_name = dst_dir + '/' + new_file_name
    os.rename(dst_file, new_dst_file_name)
    print('copy and rename ' + old_file_name +
          ' to ' + new_file_name + ' in history folder')

def model_update():
    # check the UP file whether is exist 
    try:
        # get new news
        filePath = sorted(glob.glob(r"model_training/input_labelled_news/UP*"), reverse=False)[0]
        fileName = os.path.basename(filePath)
        new_filename = 'model_training/input_labelled_news/' + fileName
        fields = ['statement', 'label']
        new = pd.read_csv(new_filename, usecols=fields)
        new.columns = ['Statement', 'Label']
    except IndexError as e:
        print('please input the UP file then run again')
        quit(0)

    # check the train.csv and test.csv file whether is exist and copy and rename file test.csv and test.csv
    try:
        # get train
        train = pd.read_csv('model_training/train.csv')
        # get test
        test = pd.read_csv('model_training/test.csv')

        # append
        out = train.append(test, sort=True)
        out = out.append(new, sort=True)

        # Drop Duplicate Rows
        out = out.drop_duplicates()
        
        # get timestamp
        ts = time.time()
        timestamp = datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
        # news filename
        new_train_filename = timestamp + 'train' + '.csv'
        new_test_filename = timestamp + 'test' + '.csv'
        new_model_filename = timestamp + 'model' + '.sav'
        # copy and rename
        copy_rename('model.sav', new_model_filename)
        copy_rename('train.csv', new_train_filename)
        copy_rename('test.csv', new_test_filename)
    except FileNotFoundError as e:
        print('please check your train.csv, test.csv and model.sav file')
        quit(0)

    X_train, X_test, y_train, y_test = train_test_split(out['Statement'], out['Label'], test_size=0.2)  

    # output train file
    train_df = pd.DataFrame(X_train, columns = ['Statement']) 
    train_df['Label'] = y_train
    with open('model_training/train.csv', 'w', encoding='utf-8') as f:
        train_df.to_csv(f, index=False)

    # output test file
    test_df = pd.DataFrame(X_test, columns = ['Statement']) 
    test_df['Label'] = y_test
    with open('model_training/test.csv', 'w', encoding='utf-8') as f:
        test_df.to_csv(f, index=False)

    # move the UP file to processed file 
    inputPath = "model_training/input_labelled_news/" + fileName
    processedPath = "model_training/processed/" + fileName
    shutil.move(inputPath, processedPath)

    # run the model training
    ModelTrain.model_training()

if __name__ == '__main__':
    model_update()
