from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///PlayingSpark/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
ratings.collect()
print(ratings.printTreeString().show())


# sortedResults = collections.OrderedDict(sorted(result.items()))
# for key, value in sortedResults.items():
#     print("%s %i" % (key, value))
