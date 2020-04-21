#!/usr/bin/env python3

import config
import cf_driver

import sys

if __name__ == '__main__':
    zones = config.parse_file('test.conf')

    for zone in zones:
        for record in zone.records:
            rec_id = cf_driver.get_dns_record_id(
                zone.cf_token,
                zone.cf_id,
                record.name
            )

            if rec_id is not None:
                cf_driver.patch_dns_record_address(
                    zone.cf_token,
                    zone.cf_id,
                    rec_id,
                    record.content
                )
