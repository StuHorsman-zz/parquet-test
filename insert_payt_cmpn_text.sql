USE cba;
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.exec.max.dynamic.partitions.pernode = 1000;
SET hive.exec.compress.output=true;
SET mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec;
SET mapred.output.compression.type=BLOCK;
INSERT INTO TABLE payt_cmpn_text
PARTITION (year, month)
SELECT *, substr(evnt_crat_d, 1, 4) as year, substr(evnt_crat_d, 6, 3) as month 
FROM payt_cmpn_source;
