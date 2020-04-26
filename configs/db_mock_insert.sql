
/* Mock Users */

INSERT INTO users (user_id) VALUES ("3021575131219191");

/* Mock Life Lists */

INSERT INTO lifelists (lifelist_id, title, description, author_id)
VALUES ("LL_0000001", "Corona Preparation",
        "List preparing for corona virus - includes shopping, and sanitization",
        "3021575131219191");

INSERT INTO lifelists (lifelist_id, title, description, author_id)
VALUES ("LL_0000002", "Bathroom Cleaning",
        "List to make your bathroom spotless",
        "3021575131219191");

INSERT INTO lifelists (lifelist_id, title, description, author_id)
VALUES ("LL_0000003", "Sanitization List",
        "List to make sure you stay clean and healthy",
        "3021575131219191");


/* Mock Tasks */

INSERT INTO tasks (task_id, lifelist_id, title, idx) VALUES ("TSK_0000001", "LL_0000001", "Get Toilet Paper", 1);

INSERT INTO tasks (task_id, lifelist_id, title, idx) VALUES ("TSK_0000002", "LL_0000001", "Get Tinned Foods", 2);

INSERT INTO tasks (task_id, lifelist_id, title, idx) VALUES ("TSK_0000003", "LL_0000002", "Clean Sink", 1);

INSERT INTO tasks (task_id, lifelist_id, title, idx) VALUES ("TSK_0000004", "LL_0000002", "Clean Toilet", 2);

INSERT INTO tasks (task_id, lifelist_id, title, idx) VALUES ("TSK_0000005", "LL_0000003", "Wash hands for 20 seconds", 1);

INSERT INTO tasks (task_id, lifelist_id, title, idx) VALUES ("TSK_0000006", "LL_0000003", "Dont touch face", 2);


/* Mock Favourites */

INSERT INTO favourites (user_id, lifelist_id) VALUES ("3021575131219191", "LL_0000001");
INSERT INTO favourites (user_id, lifelist_id) VALUES ("3021575131219191", "LL_0000002");


/* Mock Votes */

INSERT INTO votes (user_id, lifelist_id) VALUES ("3021575131219191", "LL_0000002");
INSERT INTO votes (user_id, lifelist_id) VALUES ("3021575131219191", "LL_0000003");
