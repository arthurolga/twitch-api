drop database if exists Twitch;
drop database if exists twitch;
create database if not exists twitch;
CREATE TABLE IF NOT EXISTS twitch.streamer (
streamer_id INT NOT NULL,
streamer_login VARCHAR(50) NULL,
streamer_display_name VARCHAR(50) NULL,
streamer_type VARCHAR(50) NULL,
streamer_broadcaster_type VARCHAR(50) NULL,
streamer_profile_image_url VARCHAR(1000) NULL,
streamer_view_count INT NULL,
PRIMARY KEY(streamer_id)
);

CREATE TABLE IF NOT EXISTS twitch.game (
game_name VARCHAR(32) NULL,
game_id INT,
PRIMARY KEY (game_id)
);

CREATE TABLE IF NOT EXISTS twitch.stream (
stream_id BIGINT,
stream_user_id INT,
stream_user_name VARCHAR(90) NULL,
stream_game_id INT,
stream_type VARCHAR(90) NULL,
stream_title VARCHAR(480) NULL,
stream_viewer_count INT NULL,
stream_started_at VARCHAR(90) NULL,
stream_request_time TIMESTAMP,
stream_language VARCHAR(90) NULL,


PRIMARY KEY (stream_id,stream_request_time),
FOREIGN KEY (stream_user_id) REFERENCES streamer(streamer_id),
FOREIGN KEY (stream_game_id) REFERENCES game(game_id)
);