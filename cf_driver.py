import os
import requests

CF_BASEPATH = "https://api.cloudflare.com/client/v4"

def cf_get(token, path, query=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    return requests.get(CF_BASEPATH + path, params=query, headers=headers)

def cf_patch(token, path, data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    return requests.patch(CF_BASEPATH + path, json=data, headers=headers)

def get_zone_id(token, zone_name):
    endpoint = "/zones"
    query = {"name": zone_name}

    response = cf_get(token, endpoint, query)
    print(response.text)

def get_zone_details(token, zone_id):
    endpoint = "/zones/{}".format(zone_id)

    response = cf_get(token, endpoint)
    result = response.json()["result"]
    return result

def get_dns_record_id(token, zone_id, dns_record_name):
    endpoint = "/zones/{}/dns_records".format(zone_id)
    query = {"name": dns_record_name}

    response = cf_get(token, endpoint, query)
    result = response.json()["result"]
    return result[0]["id"]

def get_dns_record_details(token, zone_id, dns_record_id):
    endpoint = "/zones/{}/dns_records/{}".format(zone_id, dns_record_id)

    response = cf_get(token, endpoint)
    result = response.json()["result"]
    return result

def patch_dns_record_address(token, zone_id, dns_record_id, address):
    endpoint = "/zones/{}/dns_records/{}".format(zone_id, dns_record_id)
    params = {"content": address}

    response = cf_patch(token, endpoint, params)
