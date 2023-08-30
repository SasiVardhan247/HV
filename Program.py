class Program:
	def __init__(self):
		self.functions = {}		
	
	def addFunctionDetails(self,name, function):
		self.functions[name] = function

	def print(self):
		for funname, function in self.functions.items():
			function.print()

	def getMainFunction(self):
		for funname, function in self.functions:
			if(funname == 'main'):
				return function
    
	# def getFunctionDeatils(self, name):
	# 	if name in functions:
	# 		return functions[name]
	# 