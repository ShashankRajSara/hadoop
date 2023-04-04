from pyspark.sql import SparkSession
from pyspark.sql.types import TimestampType, StringType, StructField, StructType
from pyspark.sql.functions import *


spark = SparkSession.builder.master('local').appName('Streaming App').getOrCreate()

schema = StructType([ StructField("movieid", StringType(), True),
                      StructField("title", StringType(), True),
                      StructField("genres", StringType(), True)])

rdd_1 = spark.readStream\
    .schema(schema)\
    .option("maxFilesPerTrigger", 1)\
    .json("C:/Users/Miles/Documents/GitHub/hadoop/dataset/movies.csv")


#1
rdd2=rdd_1.map(lambda x: x.split('"')[0]+x.split('"')[1].\
            replace(',','')+x.split('"')[-1] if '"' in x else x).\
            collect()[1:]
rdd2 = sc.parallelize(rdd2)
rdd3 = rdd2.map(lambda x : x.split(","))

rdd4 = rdd3.map(lambda x : (x[1].split()[-1][1:5],x[2].split('|')))

rdd5 = rdd4.map(lambda x: ",".join(x[1]).replace(',', ' '+x[0]+',')+' '+x[0])

#b
rdd5.cache()

newrdd = rdd5.flatMap(lambda x: x.split(',')).\
    map(lambda x: ((x.split()[-1],x.split()[0]),1))\
    .reduceByKey(lambda x,y: x+y).map(lambda x: (x[0][0],[x[1],x[0][1]]))\
    .reduceByKey(lambda x,y: max(x,y))\
    .sortBy(lambda x: x[0],ascending=False)

for i in newrdd.collect()[12:]:
     print(i[0],i[1][1],i[1][0])

#2
newrdd1=newrdd.groupBy( \
    window(newrdd.time, "5 minutes", "60 seconds"),
    newrdd.genres
).count()

#console Output
query = (
  newrdd1
    .writeStream
    .format("console")
    .outputMode("complete")
    .start()
)


#3
newrdd2=newrdd.withWatermark("time", "10 minutes").\
    groupBy( \
    window(newrdd.time, "5 minutes", "60 seconds"),
    newrdd.genres
).count()

#console Output
query = (
  newrdd1
    .writeStream
    .format("console")
    .outputMode("complete")
    .start()
)


#4
query = (
  newrdd2
    .writeStream
    .format("json")
    .option("checkpointLocation", "checkpoint")
    .option("hdfs://localhost:9000/user/training/movie/movie-stream-analysis-out","output")
    .start()
)