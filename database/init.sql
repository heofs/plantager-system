CREATE TABLE users(
    user_id CHAR(40) NOT NULL PRIMARY KEY UNIQUE,
    name CHAR(40),
    email CHAR(255),
    locale CHAR(10)
);

CREATE TABLE user_settings(
    name TEXT NOT NULL UNIQUE,
    value JSON,
    created_at TIMESTAMP DEFAULT now()
);

insert into user_settings (name, value) VALUES ('light_cycle', 
'[{
    "date": "start",
    "on": [9, 0],
    "off": [21, 0]
}]') ON CONFLICT (name) DO UPDATE SET value = excluded.value;




GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to db_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to db_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to db_user;