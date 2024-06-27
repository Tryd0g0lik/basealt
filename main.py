# This is a sample Python script.
from project.oop.postmane import Postmen
from project.env import APP_API_BRANCH_1, APP_API_BRANCH_2, APP_PATHNAME
URL_BASIC_API = "https://rdb.altlinux.org/api/"
from asyncio import *
import tracemalloc
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


async def print_hi():
    postmen = Postmen(pathnames=[APP_PATHNAME + APP_API_BRANCH_1, APP_PATHNAME + APP_API_BRANCH_2])
    r = await postmen.get_api_request(urls=URL_BASIC_API)

    tracemalloc.start()
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    run(print_hi())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
