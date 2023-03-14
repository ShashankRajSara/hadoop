import pyspark

from pyspark.sql import SparkSession

from pyspark.sql.functions import *
from pyspark.sql import Window
from datetime import datetime

spark = SparkSession.builder.master('local').appName('New App').getOrCreate()


# a.
movies_df = spark.read.csv("/mnt/c/Users/Miles/Documents/Github/hadoop/Test/ml-latest-small/movies.csv",header=True,inferSchema=True,sep=',')

get_yor = udf(lambda x : x.split(' ')[-1][1:5])

df_movies = movies_df.withColumn('Yor', get_yor(movies_df["title"])).withColumn('time_stamp', lit(datetime.now()))

print(df_movies.show())

df_movies.write.mode('overwrite').save('hdfs://localhost:9000/user/training/movie/movies1.csv')


# b.

df_movies.toJSON().saveAsTextFile('hdfs://localhost:9000/user/training/movie/movies1.json')
