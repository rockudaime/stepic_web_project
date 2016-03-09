def simple_app(environ, start_response):
    status = '200 OK'
    query = environ[QUERY_STRING].split('&')
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return query