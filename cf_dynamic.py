#!/usr/bin/env python3

import os
import requests

CF_BASEPATH = "https://api.cloudflare.com/client/v4"

def cf_get(token, path, query=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "bearer " + token
    }
    return requests.get(CF_BASEPATH + path, params=query, headers=headers)

def cf_patch(token, path, data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "bearer " + token
    }
    return requests.patch(CF_BASEPATH + path, json=data, headers=headers)

CF_TOKEN = os.getenv("CF_TOKEN")

def get_zone_id(zone_name):
    endpoint = "/zones"
    query = {"name": zone_name}

    response = cf_get(CF_TOKEN, endpoint, query)
    print(response.text)

def get_zone_details(zone_id):
    endpoint = "/zones/{}".format(zone_id)

    response = cf_get(CF_TOKEN, endpoint)
    print(response.text)

def get_dns_record_id(zone_id, dns_record_name):
    endpoint = "/zones/{}/dns_records".format(zone_id)
    query = {"name": dns_record_name}

    response = cf_get(CF_TOKEN, endpoint, query)
    print(response.text)

def get_dns_record_details(zone_id, dns_record_id):
    endpoint = "/zones/{}/dns_records/{}".format(zone_id, dns_record_id)

    response = cf_get(CF_TOKEN, endpoint)
    print(response.text)

def patch_dns_record_address(zone_id, dns_record_id, address):
    endpoint = "/zones/{}/dns_records/{}".format(zone_id, dns_record_id)
    params = {"content": address}

    response = cf_patch(CF_TOKEN, endpoint, params)
    print(response.text)
