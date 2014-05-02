#!/bin/bash
hive -f ./drop_cba.sql
# Load file
echo Uploading source table...
hdfs dfs -rm -r -skipTrash cba/file.out
hdfs dfs -put file.out cba

# First create partitioned table
echo Creating source table...
hive -f ./create_source_payt_cmpn.sql

# create source table 
echo Creating text table...
hive -f ./create_payt_cmpn_text.sql
echo Inserting text table...
hive -f ./insert_payt_cmpn_text.sql

# Create parquet table
echo Creating parquet table...
hive -f ./create_payt_cmpn_parquet.sql
echo Inserting parquet table...
hive -f ./insert_payt_cmpn_parquet.sql

# Run some queries
time hive -e 'SELECT * from cba.payt_cpmn_text;'
time hive -e 'SELECT * from cba.payt_cpmn_parquet;'
