import webbrowser
import urllib.parse
import sys  # needed for reading arguments from terminal
import argparse

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


def create_query_string():

    if args.explicit:
        return urllib.parse.quote(' '.join(args.query) + create_search_filter())
    elif args.single:
        return urllib.parse.quote(' '.join(args.query) + f'(site:{args.single})')
    else:
        return urllib.parse.quote(' '.join(args.query))


def create_url():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("Error: Enter a valid search query")
        return ""
    else:
        return base_url + create_query_string()


def start_search():
    final_url = create_url()
    if len(final_url) == 0:
        return
    print(final_url)
    webbrowser.open(final_url)
    return


parser = argparse.ArgumentParser(description="This tool is used to search google from your terminal")
parser.add_argument("-e", "--explicit", action="store_true", help=f'Includes only result from {valid_websites}')
parser.add_argument("-s", "--single", help="Include only results from given source.")

parser.add_argument("query", nargs=argparse.REMAINDER)

args = parser.parse_args()

if args.explicit and args.single:
    print("You can either use single or explicit search.")
    exit()

start_search()

