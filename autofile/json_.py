""" load and dump to json files
"""
import os
import json
from shutil import copyfile
import time


def read_json(file_path):
    """ read a file as a string

    :param file_path: path of file to be read
    :type file_path: str
    :return: file contents
    :rtype: dict
    """
    assert os.path.isfile(file_path)
    avail = 'in use'
    while avail == 'in use':
        time.sleep(.1)
        if os.path.exists(file_path.replace('.json', '.avail')):
            with open(file_path.replace('.json', '.avail'), 'r') as afile:
                avail = afile.read()
        else:
            avail = 'available'
    try:
        with open(file_path) as file_obj:
            json_dct = json.load(file_obj)
    except Exception as specific_error:
        if os.path.exists('_'.join([file_path, 'backup'])):
            copyfile('_'.join([file_path, 'backup']), file_path)
            print(
                'failure reading json file,',
                'falling back to {}_backup'.format(file_path))
            raise IOError from specific_error
        raise Exception(
            'failure reading json file,',
            'no backup to fall back to for {}'.format(
                file_path)) from specific_error
    return json_dct


def write_json(json_dct, file_path):
    """ write a string to a file

    :param file_path: path of file to be written
    :type file_path: str
    :param file_path: dictionry to be written
    :type file_path: dict
    """
    avail = 'in use'
    while avail == 'in use':
        time.sleep(.1)
        if os.path.exists(file_path.replace('.json', '.avail')):
            with open(file_path.replace('.json', '.avail'), 'r') as afile:
                avail = afile.read()
        else:
            avail = 'available'
    with open(file_path.replace('.json', '.avail'), 'w') as afile:
        afile.write('in use')
    if os.path.exists(file_path):
        copyfile(file_path, '_'.join([file_path, 'backup']))
    try:
        with open(file_path, 'w') as file_obj:
            json.dump(json_dct, file_obj, ensure_ascii=False, indent=4)
    except Exception as specific_error:
        if os.path.exists('_'.join([file_path, 'backup'])):
            copyfile('_'.join([file_path, 'backup']), file_path)
            print(
                'failure writing json file,'
                'falling back to {}_backup'.format(file_path))
            raise IOError from specific_error
        raise Exception(
            'failure writing json file,'
            'no backup to fall back to for {}'.format(
                file_path)) from specific_error
    with open(file_path.replace('.json', '.avail'), 'w') as afile:
        afile.write('available')
