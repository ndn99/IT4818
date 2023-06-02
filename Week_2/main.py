from pyspark.sql import SparkSession


def create_spark_session(URL):
    spark = SparkSession.builder.master(URL).appName("Week 2")
    return spark.getOrCreate()


if __name__ == "__main__":
    SPARK_MASTER_URL = "spark://spark:7077"
    spark = create_spark_session(SPARK_MASTER_URL)
    text_file = spark.read.text("hdfs://192.168.0.102:9000/data/demo.txt").rdd.map(lambda x: x[0])

    # Tách các từ trong tập tin văn bản
    words = text_file.flatMap(lambda line: line.split(" "))

    # Đếm số lần xuất hiện của các từ
    word_counts = words.countByValue()

    # In kết quả
    for word, count in word_counts.items():
        print("{}: {}".format(word, count))

    # Dừng Spark context
    spark.stop()
