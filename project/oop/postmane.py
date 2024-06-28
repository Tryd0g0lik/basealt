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
			TODO: getting all the data
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

	async def sorter_data(self, *args):
		list_total_data = []

		list_total_data.append(args[0])
		# list_total_data.append(list(args)[1][1])

		# sisyphus_packages = args[0][0]
		packages_sisyphus = PACKAGES_SISYPHUS
		# packages_p10 = args[0][1]
		packages_p10 = PACKAGES_P10
		result = await Postmen.compare_version_release(packages_sisyphus, packages_p10)

		# list_sisyphus = list_total_data[0].copy()
		# list_p10 = list_total_data[1].copy()
		new_list_sisyphus = []
		# sisyphus_packages
		# for sisyphus in sisyphus_packages:
		#
		# for name, sisyphus_packages in sisyphus_packages.items():
		# 	name = 'name'
		# 	# if name == sisyphus_package[0] in sisyphus_package:
		# 	# 	pass
		# 	pass

	@staticmethod
	async def compare_version_release(package1:list, package2:list) -> list:
		result_package1 = []
		result_package2 = []
		result = []

		result_package1:list = await Postmen.search_list(package1, package2)
		result.append(result_package1)
		result_package2:list = await Postmen.search_list(package2, package1)
		result.append(result_package2)
		return result

				# result_package1.append(single)

				# for single_dict_ofPackage2 in package2:
				# 	if ('name:' + str(single['name'])) in single_dict_ofPackage2:
				# 		single_dict_ofPackage2

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
			# for subsingle in list_toSearch:
			# 	if list_bool.count(False) > 0:
			# 		continue
			# 		# break
			#
			# 	if single['name'] not in subsingle['name']:
			# 		list_bool.append(True)
			# 		# result_package.append(single)
			# 	else:
			# 		list_bool.append(False)
			#
			# 	result_package.append(single)
		return result_package