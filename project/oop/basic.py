# project/oop/basic.py
class BasicBranches:
	URL_BASIC_API = "https://rdb.altlinux.org/api/"
	@classmethod
	def validate(cls, arg):
		return  type(arg) == list and len(cls.arg) > 0 and BasicBranches.check_list(arg)

	def __init__(self, pathnames: list):
		'''
		TODO: we get list of branch names in the entrypoint. It will be check in 'self.validate' - True it's mean that all elements has
		 'str' type or not
		:param pathnames: This's entrypoint. It's type 'list'
		:returns True or False
		'''
		self.pathnames = []
		if self.validate(pathnames):
			self.pathnames: list = pathnames
		else:
			raise ValueError('[Error]: What something wrong at "BasicPostman" from the "basic.py".')
	@staticmethod
	def check_list(arg):
		true_false = []
		for i in range(0, len(arg) - 1):
			if type(arg[i]) != str:
				true_false.append(False)
				continue
			else:
				true_false.append(True)
		if true_false.count(False) == 0:
			return True
		else:
			return False
