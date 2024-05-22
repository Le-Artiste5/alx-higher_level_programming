-- Lists the temperature of cities
-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
SELECT `city`, AVG(`value`) AS avg_temp  FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
