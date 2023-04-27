from similarity import cosineSim
from getQuery import text_to_query
from googleSearch import search_content
from pdf_report import PDF


def isPlagait(plagiat):
    if plagiat > 0.60:
        return True
    return False


def plagiat_query(query, type=1):
    content = search_content(query, type)
    content_queries = text_to_query(content)

    max = 0
    for content_query in content_queries:
        if len(content_query) < 60:
            continue
        temp = cosineSim(content_query, query)
        if(temp > max):
            max = temp

    return max


def result_plagait_query(query):
    max_plagiat_query = plagiat_query(query)

    if max_plagiat_query < 0.80:

        max_plagiat_query_2 = plagiat_query(query, 2)
        if max_plagiat_query_2 > max_plagiat_query:
            max_plagiat_query = max_plagiat_query_2

    max_plagiat = max_plagiat_query*max_plagiat_query

    result_query = [
        max_plagiat,
        query,
        isPlagait(max_plagiat)
    ]
    return result_query


def plagiat(text, pdf_name):

    pdf = PDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    queries = text_to_query(text)
    nbr_plagiat_query = 0
    result = []

    for query in queries:

        if len(query) < 60:
            pdf.set_content(query)
            continue

        result_query = result_plagait_query(query)
        result.append(result_query)

        if result_query[2]:  # is plagiat
            nbr_plagiat_query += 1
            pdf.set_content(query, "red")
        else:
            pdf.set_content(query, "green")

    path = pdf_name
    pdf.output(path)

    Percentage_plagiat = nbr_plagiat_query/len(result)

    return [result, Percentage_plagiat]


# text = """
# Wikipédia est un projet d’encyclopédie collective en ligne, universelle,
# """

# print(plagiat(text))
