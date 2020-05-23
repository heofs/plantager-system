CREATE TABLE user_settings(
    name TEXT PRIMARY KEY,
    value JSON,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE sensor_metadata(
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL,
    location TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE sensor_data(
    sensor_id TEXT REFERENCES sensor_metadata(id),
    location TEXT NOT NULL,
    value REAL NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);

insert into user_settings (name, value) VALUES ('light_plan', 
'[{ "date": "start", "on": [9, 0], "off": [21, 0] }]');
insert into user_settings (name, value) VALUES ('ui', 
'{ "title": "Your Grow" }');
insert into user_settings (name, value) VALUES ('active_sensors', '[]');
insert into user_settings (name, value) VALUES ('monitoring', '{}');

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to db_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to db_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to db_user;