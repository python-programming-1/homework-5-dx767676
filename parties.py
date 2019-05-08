import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the noisiest city and borough and their respective metrics

    num_city_calls = {}
    num_borough_calls = {}
    for entry in data:
        if (not entry['city'] in num_city_calls.keys()):
            if (entry['city'] != 'City'):
                num_city_calls.update({entry['city']: 0})
        else:
            num_city_calls[entry['city']] += int(entry['num_calls'])
        if (not entry['borough'] in num_borough_calls.keys()):
            if (entry['borough'] != 'Borough' and entry['borough'] != 'Unspecified'):
                num_borough_calls.update({entry['borough']: 0})
        else:
            num_borough_calls[entry['borough']] += int(entry['num_calls'])

    city_max = max(num_city_calls.keys(),  key = lambda x: num_city_calls[x])
    borough_max = max(num_borough_calls.keys(), key = lambda x: num_borough_calls[x])
    noisiest_city_and_borough = {'city': city_max, 'borough': borough_max, 'num_city_calls': num_city_calls[city_max], 'num_borough_calls': num_borough_calls[borough_max]}
    
    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the quietest city and borough and their respective metrics

    num_city_calls = {}
    num_borough_calls = {}
    for entry in data:
        if (not entry['city'] in num_city_calls.keys()):
            if (entry['city'] != 'City'):
                num_city_calls.update({entry['city']: 0})
        else:
            num_city_calls[entry['city']] += int(entry['num_calls'])
        if (not entry['borough'] in num_borough_calls.keys()):
            if (entry['borough'] != 'Borough' and entry['borough'] != 'Unspecified'):
                num_borough_calls.update({entry['borough']: 0})
        else:
            num_borough_calls[entry['borough']] += int(entry['num_calls'])

    city_min = min(num_city_calls.keys(),  key = lambda x: num_city_calls[x])
    borough_min = min(num_borough_calls.keys(), key = lambda x: num_borough_calls[x])
    quietest_city_and_borough = {'city': city_min, 'borough': borough_min, 'num_city_calls': num_city_calls[city_min], 'num_borough_calls': num_borough_calls[borough_min]}

    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    # print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
