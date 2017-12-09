import inspect
import os

from picker import Picker

class PickerFactory(object):

	def __init__(self):

		self._pickerClasses = {}


	def GetPickers(self):

		# print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		# switch to that directory
		curDir = os.getcwd() ### This isn't right, could be running from different directory
		newDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		print("Changing to ", newDir)
		os.chdir(newDir)
		for f in os.listdir(newDir):
			if not os.path.isfile(os.path.join(newDir, f)) or f.find(".py") == -1 or f == "__init__.py":
				continue

			# Load module (filename minus the .py)
			print("Importing ", f)
			mod = __import__(f[:f.rindex(".py")])
			# getmembers returns a list of tuples: (name, class)
			classes = inspect.getmembers(mod, lambda x: inspect.isclass(x) \
										 and issubclass(x, Picker) and x != Picker)
			for c in classes:
				self._pickerClasses[c[0]] = c[1]


		# switch back directories when done



	def CreatePicker(self, className):


		if not self._pickerClasses:
			self.GetPickers()

		if className not in self._pickerClasses:
			print("Invalid picker name: ", className)
			return None
		else:
			print(self._pickerClasses)
			print(self._pickerClasses[className])
			return self._pickerClasses[className]()