# Käyttötapauksia


Välitystoimistona voin tarkastella yksittäisen lastenhoitajan työvuoroja.

**SQL-kysely:**

**SELECT time FROM workingtimes WHERE nanny_id=nanny.id;**



Välitystoimistona voin lisätä toimistooni kuuluvia lastenhoitajia, jotta olisi enemmän työntekijöitä.

**SQL-kysely:**

**INSERT INTO nanny (name, age, phonenumber) VALUES (?,?,?);**



Välitystoimistona voin poistaa lastenhoitajia omasta toimistostani, jos he eivät enää voi työskennellä, jotta "haamuhoitajat" eivät jää listoilleni.

**SQL-kysely:**

**DELETE FROM nannyagencynanny WHERE nannyagency_id=nannyagency.id AND nanny_id=nanny.id** 



Välitystoimistona voin varata lastenhoitajan tiettynä aikana, jotta asiakas saa hoitajan kotiinsa.

**SQL-kysely:**

**UPDATE workingtimes SET reserved=True WHERE id=?;** 



Välitystoimistona voin tarkastella toimistooni liittyviä tilastotietoja.

SQL-kysely: tämän sivun tulevat SQL-kyselyt näkyvät koodin seassa ja niiden selitykset myös.



Välitystoimistona voin päivittää lastenhoitajiini liittyviä tietoja. *Toiminto tulossa*



Välitystoimistona voin tarkastaa ketkä lastenhoitajista voivat työskennellä, jo$

SQL-kysely: *toiminto tulossa*



