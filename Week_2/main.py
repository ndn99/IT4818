import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

spark=SparkSession.builder\
    .master("local[*]")\
    .appName("WordCount")\
    .getOrCreate()

sc=spark.sparkContext
textFile = sc.textFile("hdfs://192.168.1.47:9000/data/create_cerrtificate.txt")