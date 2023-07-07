# Build Image
- Build base image:
`cd base`
`docker build -t bim8192/hadoop-base:3.2.1 .`

- Build namenode image:
`cd namenode`
`docker build -t bim8192/hadoop-namenode:3.2.1 .`

- Build datanode image:
`cd datanode`
`docker build -t bim8192/hadoop-datanode:3.2.1 .`

# Copy file txt sample vào container
`docker cp <path file txt> <namenode id>:/opt`

# Upload txt file to HDFS
`hadoop fs -mkdir hdfs://namenode:9000/week_1`
`hadoop fs -put /opt/sample3.txt hdfs://namenode:9000/week_1`

# Run spark cluster
`docker compose up -d --sclae spark-worker=3`
# Run Pyspark job wordcount
`docker exec -it <spark master> /bin/bash`
`cd app && python3 main.py`

# Run BTL
`docker compose up -d --scale spark-worker=2`
Tạo Folder csv và spark trong folder BTL. Copy file csv vào folder BTL/csv
Đường dẫn đọc file khi chạy code là: /opt/bitnami/spark/app/<tên file>