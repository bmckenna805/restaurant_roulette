# Restaurant Roulette

Chooses a number of results from a local config file.  In this case, lists of restaurants in the Des Moines metro area. Original intent was to break deadlocks when deciding where to eat when going out on dates.

The script defaults to pulling one result unless you issue the flag `--results` followed by a number.

It also defaults to the entire list of configs unless you specify one, so for us it would default to the entire Des Moines metro unless you opt to select a specific city with the `--config` flag.

The `--help` flag will give instructions on these flags via the command line as well.

# Tests

There is a simple test suite included to help verify function of the functions.  It could probably use more work.

# The future?

I wouldn't mind extending this to be more than just a CLI but I have a lot going on and haven't gotten back to it.  Adding it to the list of incomplete projects sitting here in github.

