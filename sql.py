import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='546800asd',
    database='tdk'
)

'''Creating Tables'''
# tdk.execute('CREATE TABLE kelimeler (id int NOT NULL AUTO_INCREMENT, kelime varchar(255), koken varchar(255), PRIMARY KEY (id))')
# tdk.execute('CREATE TABLE anlamlar (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, anlam TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin, kelime_id int)')
# tdk.execute('CREATE TABLE ornekler (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, ornek TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin, ornek_id int, kaynak VARCHAR(255))')

def insert_values(query, values):
    # I don't know what I'm doing.
    tdk = cnx.cursor()
    tdk.executemany(query, values)
    cnx.commit()
    tdk.close()

def clear_duplicates(query):
    tdk = cnx.cursor()
    tdk.execute(query)
    cnx.commit()
    tdk.close()
    print('done')

# Need to run multiple times if you have duplicate counts of more than 2
delete_duplicates_query = """
DELETE FROM kelimeler_tr
WHERE id IN (
  SELECT sub.drop_id
  FROM (
    SELECT MIN(id) AS drop_id, kelime, koken, COUNT(kelime)
    FROM kelimeler_tr
    GROUP BY kelime, koken
    HAVING COUNT(kelime) > 1
  ) AS sub
);
"""

find_language_origins_query = """
SELECT lang, COUNT(*) AS frequency,  ROUND(COUNT(*) / 63075 * 100,2) as pct
FROM (
  SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(koken, ' ', numbers.n), ' ', -1) AS lang
  FROM kelimeler_tr
  JOIN (
    SELECT 1 AS n UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10
  ) AS numbers
  WHERE CHAR_LENGTH(koken) - CHAR_LENGTH(REPLACE(koken, ' ', '')) >= numbers.n - 1
) AS words
WHERE lang COLLATE utf8mb4_bin REGEXP '^[A-Z]'
GROUP BY lang
ORDER BY frequency DESC
LIMIT 10;
"""

find_author_occurances_query = """
SELECT final_part, count(final_part) as adet
FROM (
SELECT id,
CASE
    WHEN INSTR(anlam, ':\n      "') > 0
    THEN SUBSTRING_INDEX(SUBSTRING_INDEX(anlam, ':\n      "', -1), '" - ', 1)
    ELSE NULL
END AS last_part,
CASE
    WHEN INSTR(anlam, '" - ') > 0
    THEN SUBSTRING_INDEX(anlam, '" - ', -1)
    ELSE NULL
END AS final_part
FROM anlamlar) AS subquery
WHERE final_part IS NOT NULL
GROUP BY final_part
ORDER BY adet DESC;
"""

clear_duplicates(delete_duplicates_query)