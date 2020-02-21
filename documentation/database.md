# Tietokannan luontilauseet

CREATE TABLE nanny ( id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, name VARCHAR(144) NOT NULL, age INTEGER NOT NULL,phonenumber INTEGER NOT NULL, PRIMARY KEY (id) );

CREATE TABLE nannyagency ( id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, name VARCHAR(144) NOT NULL,username VARCHAR(144) NOT NULL, password VARCHAR(144) NOT NULL, PRIMARY KEY (id));

CREATE TABLE nannyagencynanny (	id INTEGER NOT NULL, date_created DATETIME, date_modified DATETIME, nannyagency_id INTEGER NOT NULL, nanny_id INTEGER NOT NULL,	PRIMARY KEY (id), FOREIGN KEY(nannyagency_id) REFERENCES nannyagency (id), FOREIGN KEY(nanny_id) REFERENCES nanny (id));


CREATE TABLE workingtimes ( id INTEGER NOT NULL, date_created DATETIME,	date_modified DATETIME,	time DATETIME,reserved BOOLEAN NOT NULL, nanny_id INTEGER NOT NULL, PRIMARY KEY (id), CHECK (reserved IN (0, 1)), FOREIGN KEY(nanny_id) REFERENCES nanny (id));
