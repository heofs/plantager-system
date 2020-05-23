-- Get all rows one hour back in time
SELECT sensor_id, value FROM `sensor-data` A WHERE A.created_at > (strftime('%s','now') - 3600);

-- Insert and update if already existing
insert into user_settings (name, value) VALUES ('grow_title', 
'Your Grow') ON CONFLICT (name) DO UPDATE SET value = excluded.value;

-- Insert to relational tables
INSERT INTO sensor_metadata (id, type, location) VALUES ('123abc', 'temperature', 'canopy');
INSERT INTO sensor_data (sensor_id, location, value) VALUES ('123abc', 'canopy', 19.2);

-- SELECTING USING JOIN
SELECT md.id, md.type, sd.location, sd.value, sd.created_at FROM 
sensor_metadata AS md INNER JOIN sensor_data as sd ON (md.id=sd.sensor_id);