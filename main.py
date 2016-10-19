#Supongo que los archivos del microscopio se encuentran en el mismo directorio que el script.
from os import listdir
import re

directory = "."

for fileName in listdir(directory):
	if( re.search(".*out",fileName)):
	
		file = open(directory  + "/" + fileName)
		try:
			regexNumberSpecies = re.compile("NumberOfSpecies\s+[0-9]+")
			lineNumberSpecies = regexNumberSpecies.search(file.read()).group()
			numberSpecies = re.search("[0-9]+", lineNumberSpecies).group()
		except:
			continue
		print "File name: " + fileName
		print "Number of species: " + numberSpecies

		file.seek(0)
		
		totalValenceCharge = 0
		regexValenceCharge = re.compile("valence\scharge.\s+[0-9]+.[0-9]+")
		
		valenceChargeList = regexValenceCharge.findall(file.read())

		for lineValenceCharge in valenceChargeList:
			valenceCharge = re.search("[0-9]+.[0-9]+", lineValenceCharge).group()
			totalValenceCharge += float(valenceCharge)
		print "Total Valence Charge: " + str(totalValenceCharge)
		print "------------------------------------------------------"
		close(file)