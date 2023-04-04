from pyspark import SparkContext

sc = SparkContext('local','Walmart Sales-VS')

rdd1=sc.textFile("C:/Users/Miles/Documents/GitHub/hadoop/dataset/WalmartSales.csv")

head =rdd1.first()
rdd2 = rdd1.filter(lambda row:row != head) #filtering records without header

rdd3 = rdd2.map(lambda x: x.split(','))

rdd3.cache()

# 1. Display the number of countries present in the data(Using Hive)

print(rdd3.map(lambda x: x[1]).first())