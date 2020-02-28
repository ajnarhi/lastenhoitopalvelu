# Käyttötapauksia


### Välitystoimistona voin tarkastella yksittäisen lastenhoitajan työvuoroja.

**SQL-kysely:**

SELECT time FROM workingtimes WHERE nanny_id=nanny.id;



### Välitystoimistona voin lisätä toimistooni kuuluvia lastenhoitajia, jotta olisi enemmän työntekijöitä.

**SQL-kysely:**

INSERT INTO nanny (name, age, phonenumber) VALUES (?,?,?);



### Välitystoimistona voin poistaa lastenhoitajia omasta toimistostani, jos he eivät enää voi työskennellä, jotta "haamuhoitajat" eivät jää listoilleni.

**SQL-kysely:**

DELETE FROM nannyagencynanny WHERE nannyagency_id=nannyagency.id AND nanny_id=nanny.id; 



### Välitystoimistona voin varata lastenhoitajan tiettynä aikana, jotta asiakas saa hoitajan kotiinsa.

**SQL-kysely:**

UPDATE workingtimes SET reserved=True WHERE id=?; 



### Välitystoimistona voin tarkastella toimistooni liittyviä tilastotietoja.

SQL-kyselyt, joista Statistics sivun tiedot ovat seurausta:


Toimiston vapaiden aikojen määrä: 

SELECT COUNT(Workingtimes.id) FROM Workingtimes
LEFT JOIN Nanny ON workingtimes.nanny_id = nanny.id
JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user
WHERE NOT Workingtimes.reserved;


Toimiston varattujen vuorojen määrä:

SELECT COUNT(Workingtimes.id) FROM Workingtimes
LEFT JOIN Nanny ON workingtimes.nanny_id = nanny.id
JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user
WHERE Workingtimes.reserved;


Lastenhoitaja, jolla eniten vapaita aikoja:

SELECT Nanny.id, Nanny.name, count(workingtimes.id) AS workingtimesamount FROM Nanny
LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id
JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user
WHERE NOT Workingtimes.reserved
GROUP BY Nanny.id
HAVING COUNT(Workingtimes.id) > 0
ORDER BY workingtimesamount DESC LIMIT; 


Lastenhoitaja, jolla eniten varauksia:

SELECT Nanny.id, Nanny.name, count(workingtimes.id) AS workingtimesamount FROM Nanny
LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id
JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user
WHERE Workingtimes.reserved
GROUP BY Nanny.id
HAVING COUNT(Workingtimes.id) > 0
ORDER BY workingtimesamount DESC LIMIT 1;


Lastenhoitajat, joilla varattavia aikoja:

SELECT Nanny.id, Nanny.name FROM Nanny
LEFT JOIN Workingtimes ON workingtimes.nanny_id = nanny.id
JOIN AgencyNanny ON agencynanny.nanny_id = nanny.id AND agency_id=:c_user
WHERE NOT Workingtimes.reserved
GROUP BY Nanny.id
HAVING COUNT(Workingtimes.id) > 0;



### Välitystoimistona voin päivittää lastenhoitajiini liittyviä tietoja.

**SQL-kysely:**


UPDATE nanny SET name=?, age=?, phonenumber=? WHERE Nanny.id=?;



### Välitystoimistona voin poistaa toimistoni tietokannasta.

**SQL-kysely:**

DELETE FROM agency  WHERE Agency.id=?;



### Välitystoimistona voin päivittää salasanani.

**SQL-kysely:**

UPDATE agency SET password=? WHERE agency.id=?;


### Välitystoimistona voin listata lastenhoiajani.

**SQL-kysely:**

SELECT * FROM Nanny WHERE agency.id=?;
