import sys
import os
import mysql.connector


def search(category):
    cnx = mysql.connector.connect(user='mysql', password='mysql',host='127.0.0.1',database='sakila')
    cursor = cnx.cursor()
    sql = "SELECT c.name AS category, Count(fc.film_id) AS film_num FROM category AS c INNER JOIN film_category AS fc ON fc.category_id = c.category_id WHERE lcase(c.name) = '%s'" % (category.lower())
    cursor.execute(sql)
    results = cursor.fetchall()
    print 'Number of films in ', category
    try:
        for row in results:
            print '%s' % (row[1])
    except:
        print 'Error'

    cursor.close()
    cnx.close()

def main():
    if len(sys.argv) != 2:
        print 'invalid parameters'
        exit(1)
    search(sys.argv[1])

if __name__ == '__main__':
    main()

