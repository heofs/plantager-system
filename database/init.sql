CREATE TABLE users(
    user_id CHAR(40) NOT NULL PRIMARY KEY UNIQUE,
    name CHAR(40),
    email CHAR(255),
    locale CHAR(10)
);

CREATE TABLE user_settings(
    type TEXT NOT NULL UNIQUE,
    setting JSON,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE sensor_metadata(
    id TEXT NOT NULL PRIMARY KEY,
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

insert into user_settings (type, setting) VALUES ('light_plan', 
'[{ "date": "start", "on": [9, 0], "off": [21, 0] }]');

insert into user_settings (type, setting) VALUES ('ui', 
'{ "title": "Your Grow" }');

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to db_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to db_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to db_user;