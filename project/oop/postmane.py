# project/oop/postmane.py

import aiohttp as aiohttp
from project.env import PACKAGES_P10, PACKAGES_SISYPHUS
from project.oop.basic import BasicBranches
from asyncio import *

class Postmen(BasicBranches):

	def __init__(self, pathnames: list, ):
		super().__init__(pathnames)
		self.data: list = []

	async def get_api_requestAll(self, urls:str) -> list:
		'''
			TODO: getting all the data from API-url
		:param urls: type 'str'
		:return: theis json's list received from the server
		'''
		async with aiohttp.ClientSession() as session:
			try:
				for pathname in self.pathnames.copy():
					url = urls + pathname

					# async with session.get(url) as response:
					response = await session.get(url)
					if response.status == 200:
						data_json = await response.json()

						await sleep(2)
						self.data.append(data_json['packages'])

					else:
						raise ValueError(f"[Error]: {response.status} - {response.text} from the 'index.py'")
				return (self.data).copy()
			except Exception as ex:
				print(f"[Error.message]: {ex}")

	async def sorter_data(self, *args) -> list:

		''' Note: Refresh variables: sisyphus_packages / packages_p10 '''
		# sisyphus_packages = args[0][0]
		packages_sisyphus = PACKAGES_SISYPHUS
		# packages_p10 = args[0][1]
		packages_p10 = PACKAGES_P10
		result = await Postmen.compare_version_release(packages_sisyphus, packages_p10)
		return result

	@staticmethod
	async def compare_version_release(package1:list, package2:list) -> list:
		result_package1 = []
		result_package2 = []
		result = []

		result_package1:list = await Postmen.search_list(package1.copy(), package2.copy())
		result.append({"sisyphus": result_package1})
		result_package2:list = await Postmen.search_list(package2.copy(), package1.copy())
		result.append({"p10":result_package2})
		return result

	@staticmethod
	async def search_list(list_analog:list, list_toSearch:list ) -> list:
		'''
		TODO: list_analog: in it we take the dictionary['name'] and \
		 searching to diсtionaries of the 'list_toSearch'. If dict of the 'list_analog' not found in the 'list_analog'
		 'list_analog.append(< dict >)'
		:param list_analog: it's what we will be search
		:param list_toSearch: it's dictionaries for a searching dictionary['name'] from list_analog
		:return: '[]' or dictionary's list
		'''

		result_package = []
		async def subsearch_list(first_list) -> list | bool:
			list_bool = [first_list['name'] not in subsingle['name'] for subsingle in list_toSearch]
			if list_bool.count(False) == 0:
				return first_list

			return False

		for single in list_analog:
			result = await subsearch_list(single)
			if type(result) != bool:
				result_package.append(result)

		return result_package

	def found_compare_count(self, sisyphus:list, p10:list) -> list:
		'''
		TODO: At entrypoint gets lists - `sisyphus` and 'p10'. \
			Then:
			 - dictionaries create of the every list.
			 - searching a dingle key from the all lists.
			 -  calculate quantity the every key from the evry lists
			 - `result_packages` is list all dictionareis. The dictionary insert in the `result_packages` if \
			  quantity the key of the `sisyphus` more then quantity that key from the `p10`

		:param sisyphus: This's a type list.
		:param p10: This's a type list.
		:return: Type list.
		'''
		sisyphus_packages = {package['name']: package for package in sisyphus}
		p10_packages = {package['name']: package for package in p10}

		result_packages = []
		result_dict_sisyphus_packages = {}
		result_dict_p10 = {}

		for name, sisyphus_package in sisyphus_packages.items():
			# result_list_ifTotal_name = {[name in p10_one for p10_one in p10_packages][0]: sisyphus_package }
			if ([name in p10_key for p10_key in p10_packages]).count(True) > 0:
				result_dict_sisyphus_packages.update({name:[sisyphus_package for key in sisyphus_packages ]})
				result_dict_p10.update({name: [package for package in p10_packages.values() if list(package.values()).count(name) > 0]})

		for k, v in result_dict_sisyphus_packages.items():
			calculator_sisyphus: int = len(result_dict_sisyphus_packages[k])
			if calculator_sisyphus > len(result_dict_p10[k]):
				result_packages.append({k: v})
		return result_packages

