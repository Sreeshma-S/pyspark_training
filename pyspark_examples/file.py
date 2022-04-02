from pyspark import SparkContext
from pyspark import SparkFiles
finddistance = "/home/Desktop/aadhar.pdf"
finddistancename = "aadhar.pdf"
sc = SparkContext("local", "SparkFile App")
sc.addFile(finddistance)
print ("Absolute Path -> %s" % SparkFiles.get(finddistancename))

