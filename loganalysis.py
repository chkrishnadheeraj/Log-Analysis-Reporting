import psycopg2
import bleach

DBNAME = "news"

top_articles_query = "select title,views from article_views limit 3"
top_authors_query = """select authors.name,sum(article_views.views) as views from authors,article_views 
where authors.id = article_views.author group by authors.name order by views desc"""
top_error_query = "select *  from error_view where \"Error Percentage\" > 1"


query_1_result = dict()
query_1_result['title'] = "\nThe 3 most popular articles of all time:\n"

query_2_result = dict()
query_2_result['title'] = "\nThe most popular article authors of all time:\n"

query_3_result = dict()
query_3_result['title'] = "\nThe days where requests error percentage was greater than 1:\n"

#runs the sql queries
def get_results(query):
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results 

#prints the query results first and second
def print_query_results(query_result):
    print(query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + '----->' + str(result[1]) + ' views')

#prints the error results
def print_error_results(error_result):
    print(error_result['title'])
    for result in error_result['results']:
        print('\t' + str(result[0]) + '----->' + str(result[1]) + '%' )

query_1_result['results'] = get_results(top_articles_query)
query_2_result['results'] = get_results(top_authors_query)
query_3_result['results'] = get_results(top_error_query)

print_query_results(query_1_result)
print_query_results(query_2_result)
print_error_results(query_3_result)


