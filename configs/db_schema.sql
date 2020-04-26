
/* Users Table */

CREATE TABLE `users` (
  `user_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


/* Lists Table */

CREATE TABLE `lifelists` (
  `lifelist_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(1000) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `description` varchar(1000) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `author_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`lifelist_id`),
  FOREIGN KEY (author_id) REFERENCES `users`(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


/* Tasks Table */

CREATE TABLE `tasks` (
  `task_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `lifelist_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(1000) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `idx` int(11) unsigned NOT NULL,
  PRIMARY KEY (`task_id`),
  FOREIGN KEY (lifelist_id) REFERENCES `lifelists`(lifelist_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


/* Favourites Table */

CREATE TABLE `favourites` (
  `user_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `lifelist_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
    PRIMARY KEY (user_id, lifelist_id),
    UNIQUE INDEX (user_id, lifelist_id),
    FOREIGN KEY (user_id) REFERENCES `users`(user_id) ON DELETE CASCADE,
    FOREIGN KEY (lifelist_id) REFERENCES `lifelists`(lifelist_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


/* Votes Table */

CREATE TABLE `votes` (
  `user_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `lifelist_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
    PRIMARY KEY (user_id, lifelist_id),
    UNIQUE INDEX (user_id, lifelist_id),
    FOREIGN KEY (user_id) REFERENCES `users`(user_id),
    FOREIGN KEY (lifelist_id) REFERENCES `lifelists`(lifelist_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

