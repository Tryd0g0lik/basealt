from project.oop.postmane import Postmen
from project.env import APP_API_BRANCH_1, APP_API_BRANCH_2, APP_PATHNAME
URL_BASIC_API = "https://rdb.altlinux.org/api/"

async def filtering_data():
    postmen = Postmen(pathnames=[APP_PATHNAME + APP_API_BRANCH_1, APP_PATHNAME + APP_API_BRANCH_2])
    response = await postmen.get_api_requestAll(urls=URL_BASIC_API)
    filter_data = []
    if response == None:
        return
    # if isinstance(response, list):
    #     for data_list in response:
    #         filter_data.append(data_list)
    # else:
    #     raise ValueError("[Error]: What something wrong to the 'filtering_data' from 'index.py")
    await postmen.sorter_data(response)