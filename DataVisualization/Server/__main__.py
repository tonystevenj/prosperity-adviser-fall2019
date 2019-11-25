# -*- coding: utf-8 -*-
from . import server
from .models import data
from .scripts import downloader,uploader

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Assistant for Restaurant Site Selection')
    parser.add_argument('run_type', default='run',
                        help='run: run webserver, pre: pretreatment')
    args = parser.parse_args()
    if args.run_type == 'run':
        data.load(True)
        server.run()
    elif args.run_type == 'init':
        data.load(False)
    elif args.run_type == 'uploaddata':
        uploader.active()
    elif args.run_type == 'downloaddata':
        downloader.active()
    elif args.run_type == 'help':
        print("run -> to run server")
        print("uploaddata -> upload data to server")
        print("downloaddata -> download data from server")
        print("init -> to load data")
