from pyspark import SparkContext

sc = SparkContext('local','VS Code Shell')

rdd_1 = sc.textFile("C:/Users/Miles/Documents/GitHub/hadoop/dataset/movies.csv")

rdd2=rdd_1.map(lambda x: x.split('"')[0]+x.split('"')[1].\
            replace(',','')+x.split('"')[-1] if '"' in x else x).\
            collect()[1:]
rdd2 = sc.parallelize(rdd2)
rdd3 = rdd2.map(lambda x : x.split(","))

rdd4 = rdd3.map(lambda x : (x[1].split()[-1][1:5],x[2].split('|')))

rdd5 = rdd4.map(lambda x: ",".join(x[1]).replace(',', ' '+x[0]+',')+' '+x[0])

#b
rdd5.cache()

rdd_count = rdd5.flatMap(lambda x: x.split(',')).\
    map(lambda x: ((x.split()[-1],x.split()[0]),1))\
    .reduceByKey(lambda x,y: x+y).map(lambda x: (x[0][0],[x[1],x[0][1]]))\
    .reduceByKey(lambda x,y: max(x,y))\
    .sortBy(lambda x: x[0],ascending=False)

for i in rdd_count.collect()[12:]:
     print(i[0],i[1][1],i[1][0])