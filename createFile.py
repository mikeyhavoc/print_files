# python3
# author: Michael Williams
# date: 3/17/16
# description: create file write to text file.
# update:
# version: 0.5
import os,sys

def create_text_file( text_file ):
    '''creates text file for list of items
       from folder you are outtputting from.
    '''
    text_file_name = input('text file name ')
    text_file = open(text_file_name, 'w') # creates text_file_name and writes to text_file
    
