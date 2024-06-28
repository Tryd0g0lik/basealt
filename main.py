from project.index import filtering_data
URL_BASIC_API = "https://rdb.altlinux.org/api/"
from asyncio import *

if __name__ == '__main__':

    run(filtering_data())

