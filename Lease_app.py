import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests
import datetime

def menu(username="batch243", lease_count=30):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
-----------------------------------
LEASE ABSTRACT
-----------------------------------
Welcome {username}!
There are {lease_count} leases in the database.
    operation | description
    --------- | ------------------
    'List'    | Display a list of all leases.
    'Show'    | Show information about a lease.
    'Add'     | Add a new lease.
    'Update'  | Edit an existing lease.
    'Delete ' | Delete an existing lease.
    'Reset'   | Reset CSV File
Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def lease_not_found():
    print("OOPS. Couldn't find a lease  with that identifier. Try listing leases to see which ones exist.")

def lease_area_not_valid():
    print(f"OOPS. That lease area is not valid. Please enter in numeric format...ie. '5000'.")

csv_headers = ["recordid", "leaseid", "suite", "name", "status", "start", "end", "area", "baserent", "frequency", "steps", "freerent", "recoveries", "lc", "ti", "expiration"]

###DEFINING READING & WRITING#####
def read_leases_from_file(filename="leases.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING LEASES FROM FILE: '{filepath}'")
    leases = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            leases.append(dict(row))
    return leases

def write_leases_to_file(filename="leases.csv", leases=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(leases)} LEASES")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["recordid", "leaseid", "suite", "name", "status", "start", "end", "area", "baserent", "frequency", "steps", "freerent", "recoveries", "lc", "ti", "expiration"])
        writer.writeheader()
        for l in leases:
            writer.writerow(l)

###RESET###
def reset_leases_file(filename="leases.csv", from_filename="leases_default.csv"):
    print("RESETTING DEFAULTS")
    leases = read_leases_from_file(from_filename)
    write_leases_to_file(filename, leases)

###DEFINE PRODUCTS, AUTO-INCREMENT & ATTRIBUTES###
def find_lease(lease_id, all_leases):
    matching_leases = [l for l in all_leases if int(l["leaseid"]) == int(lease_id)]
    matching_lease = matching_leases[0]
    return matching_lease

def auto_incremented_lease_id(leases):
    if len(leases) == 0:
        return 1
    else:
        lease_ids = [int(l["recordid"]) for l in leases]
        return max(lease_ids) + 1

def editable_lease_attributes():
    attribute_names = [attr_name for attr_name in csv_headers if attr_name != "recordid"]
    return attribute_names

def is_valid_area(my_area):
    try:
        float(my_area)
        return True
    except Exception as e:
        return False

def user_selected_lease(all_leases):
    try:
        lease_id = input("OK. Please specify the lease ID: ")
        lease = find_lease(lease_id, all_leases)
        return lease
    except ValueError as e: return None
    except IndexError as e: return None

###DEFINE OPERATIONS###
def list_leases(leases):
    print("-----------------------------------")
    print(f"LISTING {len(leases)} LEASES:")
    print("-----------------------------------")
    for lease in leases:
        print(str(lease["leaseid"]) + ": " + lease["name"]+ "||" + " Suite:" + lease["suite"] + "||" + " Area:" + lease["area"]+ "||" + " Start Date:" + lease["start"] + "||" + " Expiration Date:" + lease["end"] + "||" + " Base Rent:" + lease["baserent"])

def show_lease(lease):
    print("-----------------------------------")
    print("SHOWING A LEASE:")
    print("-----------------------------------")
    print(lease)

def create_lease(new_lease, all_leases):
    print("-----------------------------------")
    print("CREATING A NEW LEASE:")
    print("-----------------------------------")
    print(new_lease)
    all_leases.append(new_lease)

def update_lease(lease):
    print("-----------------------------------")
    print("UPDATED A LEASE:")
    print("-----------------------------------")
    print(lease)

def delete_lease(lease, all_leases):
    print("-----------------------------------")
    print("DELETING A LEASE:")
    print("-----------------------------------")
    print(lease)
    del all_leases[all_leases.index(lease)]

###RUNNING PROGRAM###
def run() :
    leases = read_leases_from_file()
    my_menu = menu(username="batch243", lease_count=len(leases))
    operation = input(my_menu)
    operation = operation.title()

    if operation == "List":
        list_leases(leases)

    elif operation == "Show":
        lease = user_selected_lease(leases)
        if lease == None: lease_not_found()
        else: show_lease(lease)

    elif operation == "Add":
        new_lease = {}
        new_lease["recordid"] = auto_incremented_lease_id(leases)
        for attribute_name in editable_lease_attributes():
            new_val = input(f"OK. Please input the lease's '{attribute_name}': ")
            if attribute_name == "area" and is_valid_area(new_val) == False:
                lease_area_not_valid()
                return
            new_lease[attribute_name] = new_val
        create_lease(new_lease, leases)

    elif operation == "Update":
        lease = user_selected_lease(leases)
        if lease == None: lease_not_found()
        else:
            for attribute_name in editable_lease_attributes():
                new_val = input(f"OK. What is the leases new '{attribute_name}' (currently: '{lease[attribute_name]}'): ")
                if attribute_name == "area" and is_valid_area(new_val) == False:
                    lease_area_not_valid()
                    return
                lease[attribute_name] = new_val
            update_lease(lease)

    elif operation == "Delete":
        lease = user_selected_lease(leases)
        if lease == None: lease_not_found()
        else: delete_lease(lease, leases)

    elif operation == "Reset":
        reset_leases_file()

    else:
        print("Didn't recognize that operation. Please try again with either 'List', 'Show', 'Add', 'Update', 'Delete', or 'Reset'")

#WRITE PRODCUTS TO CSV AFTER INPUTS ARE MADE###
    write_leases_to_file(leases=leases)


###DEFINE WHAT TO RUN FROM COMMAND LINE###
if __name__ == "__main__":
    run()
