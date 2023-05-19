#!/usr/bin/env python3
"""
bulk packaging UI

get packaging input from db, track progress
"""


__author__ = "David Cirella"
__version__ = "0.1"
__license__ = "MIT"


from pathlib import Path
import yesc.yesc as yesc
import argparse
import configparser
import sqlite3
import datetime

sys_set = 'test'
total = True


localAIPstr = ''
sips_out_path = ''

## user set defaults
default_security_tag = 'open'


## set arg parse fields, keep equivalent to yesc.py optional arg flags
def set_args(conf_set, item_row):
    
    # item_row[0] for input
    # item_row[1] for aspace_title 
    # item_row[2] for ao_ref 
    # item_row[3] security_tag 
   
    args = argparse.Namespace(input = conf_set[sys_set]['path_prefix'] + conf_set[sys_set]['input'], \
        output = conf_set[sys_set]['output'], \
        securitytag = item_row[3], \
        parent = conf_set[sys_set]['parent'], \
        aspace = item_row[2], \
        prefix = conf_set[sys_set]['prefix'], \
        sotitle = conf_set[sys_set]['sotitle'], \
        iotitle = conf_set[sys_set]['iotitle'], \
        sodescription = item_row[1], \
        iodescription = conf_set[sys_set]['iodescription'], \
        sometadata = conf_set[sys_set]['sometadata'], \
        iometadata = conf_set[sys_set]['iometadata'], \
        ioidtype = conf_set[sys_set]['ioidtype'], \
        ioidvalue = conf_set[sys_set]['ioidvalue'], \
        soidtype = conf_set[sys_set]['soidtype'], \
        soidvalue = conf_set[sys_set]['soidvalue'], \
        sipconfig = conf_set[sys_set]['sipconfig'], \
        excludedFileNames = conf_set[sys_set]['excludedFileNames'], \
        assetonly = conf_set[sys_set]['assetonly'], \
        singleasset = conf_set[sys_set]['singleasset'], \
        export = conf_set[sys_set]['export'], \
        representations = conf_set[sys_set]['representations'], \
        md5 = conf_set[sys_set]['md5'], \
        sha1 = conf_set[sys_set]['sha1'], \
        sha256 = conf_set[sys_set]['sha256'], \
        sha512 = conf_set[sys_set]['sha512'])
    return args


def config_set():
    global sys_set
    global conn
    # Configuration file info
    config = configparser.ConfigParser()
    config.read("./config.ini")
    # sql lite database 
    db_name = config[sys_set]['db_name']
    print(db_name)
    
    # DB setup
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT input, aspace_title, ao_ref, security_tag FROM entities WHERE packaged_date is '' LIMIT 2")    
         
    return c, config


def writeBack(entryID, field, value, table):
    global conn
    d = conn.cursor()
    d.execute("UPDATE {table} SET {field} = '{value}' WHERE input = '{entryID}' " .format(field=field, value=value, table=table, entryID=str(entryID)),)
    conn.commit()

def main():
    global sips_out_path 
    global total
    
    c, config = config_set()
    
    print(config)
    
    # master execution loop, set false when query finds no more db rows   
    while total == True: 
        row = c.fetchone()
        if row:
            print(row)
            args = set_args(config, row)
            sip_report = yesc.main(args)
            sip_report['packaged_date'] = str(datetime.datetime.today())
            for k,v in sip_report.items():
                writeBack(row[0], k, v, 'entities')
        else:
            total = False   

 
    
    
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
