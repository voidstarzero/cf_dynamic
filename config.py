import os

class Zone:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def __repr__(self):
        return "<Zone {}>".format(self.name)

class Record:
    def __init__(self, name, rectype):
        self.name = name
        self.rectype = rectype

    def __repr__(self):
        return "<Record {} {}>".format(self.name, self.rectype)

def parse_file(config_path):
    zones = []
    active_zone = None
    active_record = None

    with open(config_path, 'r') as config_file:
        for line in config_file:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            print(tokens)

            cmd = tokens[0]
            if cmd == 'zone':
                if active_zone is not None:
                    if active_record is not None:
                        active_zone.add_record(active_record)
                    zones.append(active_zone)
                active_zone = Zone(tokens[1])
            elif cmd == 'id':
                active_zone.cf_id = tokens[1]
            elif cmd == 'token':
                method = tokens[1]
                if method == 'text':
                    active_zone.cf_token = tokens[2]
                elif method == 'file':
                    with open(tokens[2], 'r') as tokfile:
                        active_zone.cf_token = tokfile.read().strip()
                elif method == 'env':
                    active_zone.cf_token = os.environ[tokens[2]]
            elif cmd == 'record':
                if active_record is not None:
                    active_zone.add_record(active_record)
                name = tokens[1]
                rectype = tokens[2]
                active_record = Record(name, rectype)
            elif cmd == 'content':
                method = tokens[1]
                if method == 'static':
                    active_record.content = tokens[2]
            elif cmd == 'noexist':
                create = tokens[1] == 'create'
                active_record.create = create

    if active_zone is not None:
        if active_record is not None:
            active_zone.add_record(active_record)
        zones.append(active_zone)
    return zones
