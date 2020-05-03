-- SQLite

-- Get all rows one hour back in time
SELECT sensor_id, value FROM `sensor-data` A WHERE A.created_at > (strftime('%s','now') - 3600);

