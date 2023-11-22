import json
from random import randint

_path = '/Users/colby/Documents/Lambda/playground/output'

def generate_base_ipynb(file_name):
    "Generates a blank .ipynb-styled dictionary. Input the file name."

    ipynb = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {
                "name": f"{file_name}.ipynb",
                "provenance": [],
                "collapsed_sections": []
            },
            "kernelspec": {
                "name": "python3",
                "display_name": "Python 3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "cells": []
    }

    return ipynb

def write_file(ipynb, path_output = ''):
    "Writes a ipynb dictionary into a file."

    file_text = json.dumps(ipynb, indent=2)
    file_path = path_output
    if path_output != '':
        file_path += '/'
    file_path += ipynb["metadata"]["colab"]["name"]

    file = open(file_path, 'w')
    file.write(file_text)
    file.close()

    return True

def _generate_id():
    "Generates a random 12 character ID that hopefull will work in a ipynb."

    valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'
    id12dig = ''

    for x in range(12):
        id12dig += valid_characters[randint(0, len(valid_characters)-1)]

    return id12dig

def _preserve_forward_slash(string):
    "Adds an additional forward slash in the code portion of code lines."

    without_end = string.strip('\n')
    new_str = ''
    for char in without_end:
        if char == '\\':
            new_str += '\\'
        new_str += char
    
    return new_str

def add_code_cell(ipynb, code_list):
    "Adds a code cell to your ipynb. Pass in the ipynb and a list of code."

    cell = {
        "cell_type": "code",
        "metadata": {
            "id": _generate_id()
        },
        "source": code_list,
        "execution_count": None,
        "outputs": []
    }

    ipynb["cells"].append(cell)

    return True

def add_text_cell(ipynb, text_list):
    "Adds a text cell to your ipynb. Pass in the ipynb and a list of text."

    cell = {
        "cell_type": "markdown",
        "metadata": {
            "id": _generate_id()
        },
        "source": text_list
    }

    ipynb["cells"].append(cell)

    return True



def ask_topics():
    pass


day1 = {
    "pd.read_csv()": {
        "param": {
            "names": {
                "decription": "Rename the columns, pass in a list of column names."
            }
        }
    },
    "df.head()": {},
    "df.shape()": {},
    "df.info()": {},
    "df.dtypes": {},
    "df.describe()": {
        "param": [
            "include",
            "exclude"
        ]
    },
    "df[]": {},
    "df.sort_values()": {
        "param": {
            "by": {},
            "ascending": {},
            "normalize": {}
        }
    },
    "df.isnull()": {},
    "df.any()": {},
    "df.sum()": {},
    "df.drop()": {
        "param": {
            "inplace": {},
            "axis": {},
            "columns": {}
        }
    }
}



flags = {
    "name": "flags",
    "url": "https://raw.githubusercontent.com/RCD2020/playground/main/flag.csv?token=ARDGHEF4JFXUEUFELMINMTTA5JKD2",
    "header": {
        "has_header": False,
        "column_names": [
            'name',
            'landmass',
            'zone',
            'area',
            'population',
            'language',
            'religion',
            'bars',
            'stripes',
            'colours',
            'red',
            'green',
            'blue',
            'gold',
            'white',
            'black',
            'orange',
            'mainhue',
            'circles',
            'crosses',
            'saltires',
            'quarters',
            'sunstars',
            'crescent',
            'triangle',
            'icon',
            'animate',
            'text',
            'topleft',
            'botright'
        ]
    },
    "no_index": True,
    "shape": (194, 30)
}

disney = {
    "name": "disney",
    "url": "http://users.stat.ufl.edu/~winner/data/disneymarathon2020.csv",
    "header": {
        "has_header": True,
        "column_names": [
            "gender",
            "age",
            "place",
            "group",
            "netTime",
            "minutes",
            "mph"
        ]
    },
    "no_index": True,
    "shape": (14106, 7)
}