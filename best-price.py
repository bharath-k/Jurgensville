#!/usr/local/bin/python

"""
Author: Bharath Kumaran
Licensing: GNU General Public License (http://www.gnu.org/copyleft/gpl.html)
Description: Tool to identify a restaurant that charges the least amount for a given set of
menu items.

"""

from __future__ import (print_function, division, absolute_import,
                        with_statement)
from docopt import docopt, DocoptExit
import os
import sys
import csv
import collections
import itertools

DOC = """
Tool to identify a restaurant that charges the least amount for a given set of menu items.

Usage:
    best-price <file> <item>...
    best-price (-h | --help)

Arguments:
    file            Full path of data file containing information on all
                    restaurants, menu items and price in cvs format.
    item            Menu item.

Options:
    -h, --help                  Print help and exit
"""


def process(data_file, input_items):
    """
    Process arguments.
    """
    input_items = sorted(input_items)
    data_dict = populate_data(data_file, input_items)
    final_price = final_res_id = None
    # Iterate over items in data_dict to identify best price
    for res_id, items_dict in data_dict.iteritems():
        best_price = get_best_price(items_dict, input_items)
        if best_price and (not final_price or best_price < final_price):
            final_price = best_price
            final_res_id = res_id
    if final_price:
        print(final_res_id, ",", final_price)
    else:
        print('No restaurants found for given menu item(s).')


def get_best_price(items_dict, input_items):
    """
    Get the best price for the given input items.
    """
    # Possible scenarios:
    # 1. input_items has many elements with or without repeats.
    # 2. combo options present. The combo packs itself may or may not have
    #    repeats.
    if not any(len(item) > 1 for item in items_dict.keys()):
        # There are no combos. Life is simpler.
        total_price = 0.0
        for menu_item in input_items:
            # convert menu_item to a tuple.
            if (menu_item,) in items_dict:
                total_price += items_dict[(menu_item,)]
            else:
                # If we are not able to find any item, return immediately.
                # T0D0: Perhaps this can be determined ahead of time.
                return None
        return total_price
    return get_best_price_combo(items_dict, input_items)


def get_best_price_combo(items_dict, input_items):
    """
    Get the best price for the given input items that contains combos
    """
    # Try out combinations of menu items available in the restaurant.
    # T0D0: There might be a mathematical equation for this. Explore!!
    ret_val = 0.0
    # i = 1 checks conditions when one of the combos is exactly what we are looking
    # for. Unfortunately, even if a match is found here, the rest of the
    # combinations have to be verified since a combination of two items may
    # have a lesser value than a combo.
    # Look until the no. of items in combination equals input_items size.
    for i in range(1, len(input_items)+1):
        # Perform a combinations_with_replacement to identify all possible
        # combinations as opposed to plain combination or permutation.
        all_combinations = list(itertools.combinations_with_replacement(items_dict, i))
        for group in all_combinations:
            # Flatten the list and sort it.
            current_items = [item for sublist in group for item in sublist]
            current_items = sorted(current_items)
            # Combo packs might have repeat items. Do not remove duplicates!
            if (input_items == current_items or
                is_sublist(current_items, input_items)):
                # This means all elements are present and accounted for :)
                current_val = sum(items_dict[i] for i in group)
                # Identify if the found match is the least.
                if not ret_val or current_val < ret_val:
                    ret_val = current_val
        # Unfortunately, even if ret_value has a valid value, the for-loop
        # has to be completed because it is possible that some other
        # combination of more elements might lead to a lesser price.
    return ret_val


def populate_data(data_file, input_items):
    """
    Populate data into defaultdict(dict) and massage information as per
    consumption.
    """
    data_dict = collections.defaultdict(dict)
    with open(data_file, 'rb') as csv_handle:
        reader = csv.reader(csv_handle, skipinitialspace=True)
        for row in reader:
            menu_items = row[2:]
            # Remove menu items that do not have even one item in input_items
            # list. Also ignoring unnecessary items in combos.
            menu_items = [i for i in menu_items if i in input_items]
            if menu_items:
                tuple_items = tuple(sorted(menu_items))
                if tuple_items in data_dict[int(row[0])]:
                    current_val = data_dict[int(row[0])][tuple_items]
                    # Choosing the least value if reduced combo is equal to
                    # an existing menu item or combo.
                    if float(row[1]) < current_val:
                        data_dict[int(row[0])][tuple_items] = float(row[1])
                else:
                    data_dict[int(row[0])][tuple_items] = float(row[1])
    return data_dict


def is_sublist(source_list, pattern):
    """
    Check if all elements of pattern are present in source_list
    """
    new_list = source_list[:]
    for i in pattern:
        if i in new_list:
            new_list.remove(i)
        else:
            return False
    return True


def get_options():
    """
    Fetch options dictionary and validate file argument
    """
    opts = docopt(DOC)
    if not os.path.isfile(opts['<file>']):
        raise DocoptExit('file - %s does not exist' % opts['<file>'])
    return opts


def main():
    """
    Main entry point

    Returns 0 if command execution is successful.
    Returns non-zero integer if unsuccessful.
    """
    try:
        opts = get_options()
        return process(opts['<file>'], opts['<item>'])
    except KeyboardInterrupt:
        return 1


if __name__ == '__main__':
    sys.exit(main())
