from project.oop.postmane import Postmen
from project.env import APP_API_BRANCH_1, APP_API_BRANCH_2, APP_PATHNAME, \
    PACKAGES_SISYPHUS, PACKAGES_P10
URL_BASIC_API = "https://rdb.altlinux.org/api/"

async def filtering_data():
    postmen = Postmen(pathnames=[APP_PATHNAME + APP_API_BRANCH_1, APP_PATHNAME + APP_API_BRANCH_2])
    response = await postmen.get_api_requestAll(urls=URL_BASIC_API)
    filter_data = []
    if response == None:
        return

    '''
    - все пакеты, которые есть в p10 но нет в sisyphus
    - все пакеты, которые есть в sisyphus но их нет в p10
    '''
    result_list = await postmen.sorter_data(response)


    '''
    - все пакеты, version-release которых больше в sisyphus чем в p10
    
    Note: Refresh variables: result_list[0] / result_list[1] 
    '''
    postmen.found_compare_count(PACKAGES_SISYPHUS, PACKAGES_P10)