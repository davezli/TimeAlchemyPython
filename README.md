# TimeAlchemyPython

* All files in resources/ are exported csv sheets from https://docs.google.com/spreadsheets/d/1K45DKKM0EhGo92Um5o6QC1cxqwMBNTz55TBEEAn5W5U/edit?usp=sharing
* Enter your desired items in `items` and inventory in `inventory_dict` in `main.py`, and run it.

## Example:
Inputs:
```
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
```

Output:
```
Craft List: {
    "Blood Ruby": 1,
    "Dark Soul Stone": 3,
    "Droplet of Strength": 10,
    "Black Scroll (Level 2)": 10,
    "Ice Crystal": 1,
    "Mana Shard": 6,
    "Black Scroll (Level 3)": 2,
    "Crystal of Dreams": 1,
    "Dream Stone": 6
}
Buy List: {
    "Topaz": 12,
    "Patchouli Seed Oil": 4,
    "Juniper Berry Flower Oil": 2,
    "Black Crystal": 9,
    "Power Crystal": 20,
    "NX": 10000000,
    "Meso": 100000000,
    "AquaMarine": 5,
    "Forever Unrelenting Flame": 3,
    "Dream Fragment": 141,
    "Unrelenting Flame": 1
}
Total Cost: 829322650
```


## To-Do:
* Test it. I have no idea if this actually works
* We can develop a tree and dynamically update costs in Python instead of doing it in Excel, but I'm lazy.
>>>>>>> Initial commit
