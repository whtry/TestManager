#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: whtrys
Email: whtrys@163.com
Description:
"""
import os
import json


class Main:
    def __init__(self):
        self.doc_path = "{}\\Documents".format(os.getenv("USERPROFILE"))
        self.main_path = '{}\\TestManager'.format(self.doc_path)
        self.first_open = not os.path.isdir(self.main_path)

    def create_project(self):
        about_json = {"subject": ['']}
        json_type = json.dumps(about_json)
        with open("{}\\about.json".format(self.main_path), 'w') as j:
            j.write(json_type)