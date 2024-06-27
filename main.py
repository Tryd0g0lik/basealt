# This is a sample Python script.
from project.index import filtering_data
from project.oop.postmane import Postmen
from project.env import APP_API_BRANCH_1, APP_API_BRANCH_2, APP_PATHNAME
URL_BASIC_API = "https://rdb.altlinux.org/api/"
from asyncio import *
import tracemalloc
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




    # tracemalloc.start()
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    run(filtering_data())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
