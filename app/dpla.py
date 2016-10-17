import requests
import math
import yaml

keys = yaml.load(open('keys.yaml', 'r'))
key = keys['dpla_key']


def get_results(search_term):
    url_string = 'http://api.dp.la/v2/items?q={0}&page_size=10&page=1&provider.@id=http://dp.la/api/contributor/' \
             'tn&api_key={1}'.format(search_term, key)
    s = requests.get(url_string)
    results = s.json()
    count = results['count']
    pages_of_results = math.ceil(count / 10)
    return pages_of_results


def show_results(current_page, search_term):
    url_string = 'http://api.dp.la/v2/items?q={0}&page_size=12&page={2}&provider.@id=http://dp.la/api/contributor/' \
             'tn&api_key={1}&facets=dataProvider'.format(search_term, key, current_page)
    s = requests.get(url_string)
    results = s.json()
    number = current_page * 10 - 9
    things = []
    facets = get_facets(results)
    for doc in results['docs']:
        try:
            data_provider = doc['dataProvider']
        except:
            data_provider = 'Unknown'
            pass
        preview = doc['object']
        thumbnail = preview.replace('crossroads.rhodes.edu:9090/', 'fedora.crossroadstofreedom.org/')
        things.append({'link': doc['isShownAt'], 'image': thumbnail, 'dataProvider': data_provider, 'title': doc['sourceResource']['title'][0]})
        number += 1
    new_results = [things, facets]
    return new_results


def print_url(current_page, search_term):
    url_string = 'http://api.dp.la/v2/items?q={0}&page_size=10&page={2}&provider.@id=http://dp.la/api/contributor/' \
             'tn&api_key={1}'.format(search_term, key, current_page)
    return url_string


def get_facets(data):
    facets = []
    for doc in data['facets']['dataProvider']['terms']:
        place = doc['term']
        total_results = doc['count']
        facets.append({'place': place, 'results': total_results})
    return facets


def limit_results(facet, search_string):
    url_string = 'http://api.dp.la/v2/items?q={0}&page_size=12&provider.@id=http://dp.la/api/contributor/' \
             'tn&api_key={1}&dataProvider={2}'.format(search_string, key, facet)
    s = requests.get(url_string)
    results = s.json()
    number = 1 * 10 - 9
    things = []
    for doc in results['docs']:
        try:
            data_provider = doc['dataProvider']
        except:
            data_provider = 'Unknown'
            pass
        preview = doc['object']
        thumbnail = preview.replace('crossroads.rhodes.edu:9090/', 'fedora.crossroadstofreedom.org/')
        things.append({'link': doc['isShownAt'], 'image': thumbnail, 'dataProvider': data_provider, 'title': doc['sourceResource']['title'][0]})
        number += 1
    new_results = things
    return new_results


if __name__ == "__main__":
    print(key)