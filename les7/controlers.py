from requests1 import action,db_view
from db import db_print, data_colector, db_save

def start_b():
    while (True):
        ansver =  action()
        if ansver == 1:
            data = data_colector()
            db_save(data)
        elif ansver == 2:
            db_vieW = db_view()
            db_print(db_view)
        elif ansver == 3:
            break
