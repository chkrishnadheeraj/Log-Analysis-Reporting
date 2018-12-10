#!/usr/bin/env python3
import psycopg2

DBNAME = "news"

top_articles_query = """select title,count(*) as views
                        from articles,article_views
                        where articles.slug=article_views.substring
                        group by articles.title
                        order by views desc limit 3;"""

top_authors_query = """select auth.name,count(*) as num_views
                        from authors auth,articles art,article_views
                        where auth.id = art.author and
                        art.slug=article_views.substring
                        group by auth.name
                        order by num_views desc;"""

top_error_query = "select *  from error_view where \"Error Percentage\" > 1"

query_1_result = dict()
query_1_result['title'] = "\nTop 3 popular articles of all time:\n"

query_2_result = dict()
query_2_result['title'] = "\nMost popular article authors of all time:\n"

query_3_result = dict()
query_3_result['title'] = """\nThe days where requests error percentage was \
                          greater than 1:\n"""


# runs the sql queries
def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# prints the query results first and second
def print_query_results(query_result):
    print(query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + '----->' + str(result[1]) + ' views')


# prints the error results
def print_error_results(error_result):
    print(error_result['title'])
    for result in error_result['results']:
        print('\t' + str(result[0]) + '----->' + str(result[1]) + '% errors')

query_1_result['results'] = get_results(top_articles_query)
query_2_result['results'] = get_results(top_authors_query)
query_3_result['results'] = get_results(top_error_query)

print_query_results(query_1_result)
print_query_results(query_2_result)
print_error_results(query_3_result)
