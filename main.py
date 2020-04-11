#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


def load_recipes():
    recipe_dict = {}
    with open('resources/recipes.csv', mode='r') as infile:
        for row in csv.DictReader(infile, skipinitialspace=True):
            item = {}
            itemName = ""
            for k, v in row.items():
                if v == "":
                    continue
                elif k == "Item":
                    itemName = v
                else:
                    item[k] = int(v)
            recipe_dict[itemName] = item
    return recipe_dict


def load_prices():
    price_dict = {}
    with open('resources/raw-prices.csv', mode='r') as infile:
        for row in csv.DictReader(infile, skipinitialspace=True):
            price_dict[row['Item']] = int(row['Cost (Mesos)'].replace(",", ""))
    return price_dict


def load_summary():
    summary = {}
    with open('resources/summary.csv', mode='r') as infile:
        for row in csv.DictReader(infile, skipinitialspace=True):
            item = {}
            itemName = ""
            for k, v in row.items():
                if k == "Item":
                    itemName = v
                else:
                    item[k] = v
            summary[itemName] = item
    return summary


def get_base_ingredients(item, amount, recipe_dict, summary, inventory, craft_list):
    ingredients = Counter()

    if item not in summary:
        raise AssertionError(f"Summary is missing item {item}")

    if item in inventory:
        if amount < inventory[item]:
            inventory[item] -= amount
            return ingredients
        else:
            amount -= inventory[item]
            inventory[item] = 0

    if summary[item]['Craft or Buy'] == "BUY":
        ingredients[item] += amount
    else:
        craft_list[item] += amount
        for key, value in recipe_dict[item].items():
            ingredients += get_base_ingredients(key, amount * value, recipe_dict, summary, inventory, craft_list)

    return ingredients


def main():
    """ Main program """
    recipe_dict = load_recipes()
    price_dict = load_prices()
    summary = load_summary()

    items = {
        'Blood Ruby': 1,
        'Crystal of Dreams': 1,
        'Dark Soul Stone': 2
    }

    inventory_dict = {
        'Droplet of Strength': 2,
        'Dream Stone': 9,
        'Garnet': 229,
        'Elixir of Purity': 700,
        'Black Scroll (Level 1)': 282,
        'Basic Spell Essence': 379,
        'Unrelenting Flame': 5,
        'Wisdom Crystal': 37,
        'Depleted Crystal': 284,
        'Mana Crystal': 1305,
        'Forever Unrelenting Flame': 1,
        "Dream Fragment": 15
    }
    inventory = Counter(inventory_dict)

    recipe_ingredients = Counter()
    craft_list = OrderedCounter()

    for key, value in items.items():
        recipe_ingredients += get_base_ingredients(key, value, recipe_dict, summary, inventory, craft_list)

    print(f"Craft List: {json.dumps(craft_list, indent=4)}")
    print(f"Buy List: {json.dumps(recipe_ingredients, indent=4)}")

    total_cost = 0
    for key, value in recipe_ingredients.items():
        total_cost += int(summary[key]['End Cost'].replace(",", "")) * value

    print(f"Total Cost: {total_cost}")

    return 0


if __name__ == "__main__":
    main()
