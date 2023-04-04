from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local').appName("Walmart Sales Data").getOrCreate()

df = spark.\
        read.\
        option('header','true').\
        option('inferschema','true').\
        csv("C:/Users/Miles/Documents/GitHub/hadoop/dataset/WalmartSales.csv")

print(df.show(1,truncate=False))

df.printSchema()

#1
df.select('country').show()


#2
df.select("country","Units Sold","Total Revenue","Total Profit") \
  .where("country == 'Malaysia'") \
  .show()

# Create Temp Table
df.createOrReplaceTempView('sales')

# 3
print(spark.sql("SELECT Country, SUM(`Units Sold`) AS sumOfSum \
                FROM sales \
                GROUP BY Country \
                ORDER BY sumOfSum DESC ").show())

#4
print(spark.sql("SELECT Country, ROUND(SUM(`Total Profit`)) AS sumOfProfit \
                FROM sales \
                GROUP BY Country \
                ORDER BY sumOfProfit DESC ").show())
