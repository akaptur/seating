import csv

def add_IDs(people):
    '''
    Adds a unique ID for each camper
    '''
    i=1
    for person in people:
        person["id"] = i
        i +=1
    return people

def people_dicts(filename):
    '''
    Creates a list of dictionaries, where each dict represents 1 camper
    Format: { First Name: Bob, Last Name: Jones, Category: Nurse, Mon: , Tue: 2, }
    '''
    reader = csv.DictReader(open(filename,"rwU"))
    people = [row for row in reader]
    return add_IDs(people)


def initialize_seatee_lists(tables):
    for t in tables:
        for (key, value) in t.iteritems():
            if key != 'Table Name':
                opt_value = t[key]
                t[key] = {}
                t[key]['opt'] = opt_value
                t[key]['people'] = []
    return tables


def table_dicts(filename):
    '''
    Creates a list of dictionaries, where each dict represents 1 table
    Format: { Table Name: Table-one, Mon: 8, Tue: 8, Wed: 7 }
    '''
    reader = csv.DictReader(open(filename,"rwU"))
    tables = [row for row in reader]
    return initialize_seatee_lists(tables)


def days_list(filename):
    reader = csv.reader(open(filename, "rwU"))
    header = reader.next()
    days_list = [day for day in header if day != 'Table Name']
    return days_list


def write_to_csv(people, filename):
    fieldnames = ['id','Category', 'Last Name', 'First Name', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    output_file = open(filename,'wb')
    csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
    for p in people:
        csvwriter.writerow(p)
    output_file.close()
