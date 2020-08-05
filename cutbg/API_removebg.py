#https://www.remove.bg/api
#pip install removebg

from cutbg.removebg2 import RemoveBg

import datetime
import traceback

import os

class API_removebg:
    def __init__(self , api_key , path):
        self.api_key=api_key
        self.path=path

    def API_RMBG_use(self):
        try:
            rmbg=RemoveBg(self.api_key,"error.log")
            rmbg.remove_background_from_img_file(self.path)

        except Exception:
            with open('./error.log', 'a+') as f:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write('Time: '+ now_time + '\nBackground cutout fail :'+ traceback.format_exc())
                print("Error: See error.log and you will know what happen")

        print("Cutout Done")   

