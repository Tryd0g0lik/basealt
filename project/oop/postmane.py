import aiohttp as aiohttp

from project.oop.basic import BasicBranches
from asyncio import *

class Postmen(BasicBranches):

	def __init__(self, pathnames: list, ):
		super().__init__(pathnames)
		self.datas: list = []

	async def get_api_request(self, urls:str) -> list:
		async with aiohttp.ClientSession() as session:
			for pathname in self.pathnames.copy():
				url = urls + pathname
				try:
					async with session.get(url) as response:
						if response.status == 200:
							data_json = await response.json()

							await sleep(2)
							self.datas.append(data_json)

						else:
							raise ValueError(f"[Error]: {response.status} - {response.text} from the 'index.py'")
					return (self.datas).copy()
				except Exception as ex:
					raise ValueError(f"[Error.message]: {ex}")
