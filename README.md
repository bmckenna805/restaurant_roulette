# Restaurant Roulette

Chooses a number of results from a local config file.  In this case, lists of restaurants in the Des Moines metro area. Original intent was to break deadlocks when deciding where to eat when going out on dates.

The script defaults to pulling one result unless you issue the flag `--results` followed by a number.

It also defaults to the entire list of configs unless you specify one, so for us it would default to the entire Des Moines metro unless you opt to select a specific city with the `--config` flag.

The `--help` flag will give instructions on these flags via the command line as well.

Example
```
➜  restaurant-roulette git:(main) ✗ python3 restaurant_roulette.py
INFO:root:list of restaurants:
['Chopsticks', 'Taki Steakhouse', "Charlotte's Kitchen", 'Kathmandu', '5 Borough Bagels', 'Mi Patria', 'Hana Ramen Sushi', "Persi's Biryani Indian Grill", 'Grazianos', 'Lucky Lotus', 'Exile Brewing', 'Big Grove Brewing', 'Lua Brewing', 'The Cheese Bar', 'Olympic Flame', 'Royal Mile', 'Malo', 'Open Sesame', 'Hessen Haus', 'Guadalajara', 'Flame Cantina', 'El Mocajete', 'Silk Elephant', "Magee's Pub", 'Wasabi', 'District 36', 'Flavory Bistro', 'Waterfront', "Georgio's Greek Grill", 'Wig and Pen', 'Trailside Tap', "Siam's Table", "Ben's Burgers"]
INFO:root:random choices:
["Charlotte's Kitchen"]
```

## Flags

The flags
```
➜  restaurant-roulette git:(main) ✗ python3 restaurant_roulette.py --help
usage: restaurant_roulette.py [-h] [--config CONFIG] [--results RESULTS]

options:
  -h, --help         show this help message and exit
  --config CONFIG    Name of the city config to load
  --results RESULTS  How many options to return
```
Altering how many results to return
```
➜  restaurant-roulette git:(main) ✗ python3 restaurant_roulette.py --results 3
INFO:root:list of restaurants:
['Chopsticks', 'Taki Steakhouse', "Charlotte's Kitchen", 'Kathmandu', '5 Borough Bagels', 'Mi Patria', 'Hana Ramen Sushi', "Persi's Biryani Indian Grill", 'Grazianos', 'Lucky Lotus', 'Exile Brewing', 'Big Grove Brewing', 'Lua Brewing', 'The Cheese Bar', 'Olympic Flame', 'Royal Mile', 'Malo', 'Open Sesame', 'Hessen Haus', 'Guadalajara', 'Flame Cantina', 'El Mocajete', 'Silk Elephant', "Magee's Pub", 'Wasabi', 'District 36', 'Flavory Bistro', 'Waterfront', "Georgio's Greek Grill", 'Wig and Pen', 'Trailside Tap', "Siam's Table", "Ben's Burgers"]
INFO:root:random choices:
['District 36', 'Chopsticks', '5 Borough Bagels']
```
Limiting the selection to one configuration file
```
➜  restaurant-roulette git:(main) ✗ python3 restaurant_roulette.py --config ankeny
INFO:root:list of restaurants:
['Guadalajara', 'Flame Cantina', 'El Mocajete', 'Silk Elephant', "Magee's Pub", 'Wasabi', 'District 36', 'Flavory Bistro', 'Waterfront', "Georgio's Greek Grill", 'Wig and Pen', 'Trailside Tap', "Siam's Table", "Ben's Burgers"]
INFO:root:random choices:
['Flavory Bistro']
```

## Tests

There is a simple test suite included to help verify function of the functions.  It could probably use more work.

## The future?

I wouldn't mind extending this to be more than just a CLI but I have a lot going on and haven't gotten back to it.  Adding it to the list of incomplete projects sitting here in github.

I would also like to add the option to query google maps APIs for local restaurants, specifying a review level, in a city and get a list of restaurants that way.  The configs are still useful for your local favorites, but this would make the program a little more useful if you're traveling.
