drop database if exists Twitch;
drop database if exists twitch;
create database if not exists twitch;
CREATE TABLE IF NOT EXISTS twitch.streamer (
streamer_id INT NOT NULL,
streamer_login VARCHAR(5) NULL,
streamer_display_name VARCHAR(5) NULL,
streamer_type VARCHAR(0) NULL,
streamer_broadcaster_type VARCHAR(7) NULL,
streamer_description VARCHAR(66) NULL,
streamer_profile_image_url VARCHAR(96) NULL,
streamer_offline_image_url VARCHAR(119) NULL,
streamer_view_count INT NULL,
PRIMARY KEY(streamer_id)
);

CREATE TABLE IF NOT EXISTS twitch.game (
game_name VARCHAR(32) NULL,
game_popularity INT NULL,
game_id INT,
game_giantbomb_id INT NULL,
game_box_large VARCHAR(90) NULL,
game_box_template VARCHAR(99) NULL,
game_logo_large VARCHAR(91) NULL,
game_localized_name VARCHAR(32) NULL,
game_locale VARCHAR(5) NULL,
PRIMARY KEY (game_id)
);

CREATE TABLE IF NOT EXISTS twitch.stream (
stream_id BIGINT,
stream_user_id INT,
stream_user_name VARCHAR(14) NULL,
stream_game_id INT,
stream_type VARCHAR(4) NULL,
stream_title VARCHAR(132) NULL,
stream_viewer_count INT NULL,
stream_started_at VARCHAR(20) NULL,
stream_language VARCHAR(2) NULL,
stream_thumbnail_url VARCHAR(87) NULL,
stream_tag_ids VARCHAR(36) NULL,

PRIMARY KEY (stream_id),
FOREIGN KEY (stream_user_id) REFERENCES streamer(streamer_id),
FOREIGN KEY (stream_game_id) REFERENCES game(game_id)
);
