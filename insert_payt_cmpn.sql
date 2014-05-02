USE cba;
SET dfs.blocksize=32m;
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.exec.max.dynamic.partitions.pernode = 1000;
INSERT INTO TABLE payt_cmpn
PARTITION (year, month)
SELECT *, substr(evnt_crat_d, 1, 4) as year, substr(evnt_crat_d, 6, 3) as month 
FROM payt_cmpn_source;
