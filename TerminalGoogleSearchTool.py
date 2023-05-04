import webbrowser
import urllib.parse
import sys  # needed for reading arguments from terminal

base_url = "https://www.google.com/search?q="

valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'docs.microsoft.com',
    'microsoft.com',
    'medium.com'
]

not_defined_message = "is not a defined argument. Use -help to see a available arguments."
help_message = "Available arguments: \n\n-explicit....only show defined websites"


def create_search_filter():
    website_filter = '('
    for i, website in enumerate(valid_websites):
        website_filter += ' site:' + website
        if i == len(valid_websites) - 1:
            website_filter += ')'
        else:
            website_filter += ' OR '
    return website_filter


def create_query_string(explicit_search):
    query_input = sys.argv[1:]
    if explicit_search:
        del query_input[0]
        return urllib.parse.quote(' '.join(query_input) + create_search_filter())
    else:
        return urllib.parse.quote(' '.join(query_input))


def argument_matcher(arguments):
    match arguments[0]:
        case "-explicit":
            print(base_url + create_query_string(True))
            return base_url + create_query_string(True)
        case "-help":
            print(help_message)
            return ""
        case _:
            print(f'{arguments[0]} ' + not_defined_message)
            return ""


def create_url():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("Error: Enter a valid search query")
        return ""
    elif arguments[0][0] == "-":
        return argument_matcher(arguments)
    else:
        print(base_url + create_query_string(False))
        return base_url + create_query_string(False)


def start_search():
    final_url = create_url()
    if len(final_url) == 0:
        return
    webbrowser.open(final_url)
    return


start_search()

