# python3
# author: Michael Williams
# date: 3/17/16
# description: create file write to text file.
# update:
# version: 0.5
import os,sys

def create_text_file( folder ):
    '''creates text file for list of items
       from folder you are outtputting from.
    '''
    path = folder
    files = os.listdir( path )

    text_file_name = input('text file name ')
    print('creating text file..')
    text_file = open(text_file_name + '.txt', 'w') # creates text_file_name and writes to text_file
    for filenames in files:
        if filenames.startswith('.'):
            continue                   # skip directories
        file_names = text_file.write(filenames)
        line_space = text_file.write('\n')
        text_file.close

create_text_file( 'c:\\users\\mjwil\\documents\\github\\python\\createfile')
