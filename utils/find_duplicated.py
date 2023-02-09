import json
import requests
import collections


URL = 'https://a9.wms.ocs.oraclecloud.com/corona/wms/lgfapi/v10/entity/order_hdr/?facility_id=257&company_id=198&order_type_id=97&ordering=id&create_ts__range=2021-08-10T23:35:58,2021-08-11T17:35:58'
HEADERS = {'Authorization': 'Basic d21zX2ludGVncmF0aW9uX3VzZXI6Y3YuLDIwMTQ='}

NBRS = []


def get_orders():
    response = json.loads(requests.get(URL, headers=HEADERS).content)
    NBRS.extend([order['order_nbr'] for order in response['results']])
    next = response['next_page']

    while next != '' or next is not None:
        response = json.loads(requests.get(next, headers=HEADERS).content)
        NBRS.extend([order['order_nbr'] for order in response['results']])
        next = response['next_page']

        duplicated = [item for item, count in collections.Counter(
            NBRS).items() if count > 1]
        if len(duplicated) > 0:
            print('------------- DUPLICATED ----------')
            print(duplicated)
            print(f'TOTAL: {len(duplicated)}', end='\n')


get_orders()
