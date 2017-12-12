import inspect
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from picker import Picker

class PickerFactory(object):

	def __init__(self):

		self._pickerClasses = {}


	def GetPickers(self):

		# switch to that directory
		print("Factory: populating Picker classes")
		packageDir = os.path.dirname(os.path.abspath(__file__))
		for f in os.listdir(packageDir):
			if not os.path.isfile(os.path.join(packageDir, f)) or f.find(".py") == -1 or f == "__init__.py":
				continue

			# Load module (filename minus the .py)
			print("\tImporting module ", f)
			mod = __import__(f[:f.rindex(".py")])
			# getmembers returns a list of tuples: (name, class)
			classes = inspect.getmembers(mod, lambda x: inspect.isclass(x) \
										 and issubclass(x, Picker) and x != Picker)
			for c in classes:
				print("\t\tAdding class ", c[0])
				self._pickerClasses[c[0]] = c[1]


	def CreatePicker(self, className, **kwargs):


		if not self._pickerClasses:
			self.GetPickers()

		if className not in self._pickerClasses:
			print("Invalid picker name: ", className)
			return None
		else:
			print(self._pickerClasses)
			print(self._pickerClasses[className])
			return self._pickerClasses[className](**kwargs)