Jurgensville
============

Script to identify a restaurant that charges the least amount for a given set of menu items.

Problem Statement
-----------------

Because it is the Internet Age, but also it is a recession, the Comptroller of the town of Jurgensville
has decided to publish the prices of every item on every menu of every restaurant in town,
all in a single CSV file (Jurgensville is not quite up to date with modern data serializationmethods).
In addition, the restaurants of Jurgensville also offer Value Meals, which are groups of several items,
at a discounted price. The Comptroller has also included these Value Meals in the file. The file's format is:

for lines that define a price for a single item:

restaurant ID, price, item label

for lines that define the price for a Value Meal (there can be any number of items in a value meal):

restaurant ID, price, item 1 label, item 2 label, ...

All restaurant IDs are integers, all item labels are lower case letters and underscores, and the price is a decimal number.

Because you are an expert software engineer, you decide to write a program that accepts the town's price file,
and a list of item labels that someone wants to eat for dinner, and outputs the restaurant they should go to,
and the total price it will cost them. It is okay to purchase extra items, as long as the total cost is minimized.

Here are some sample data sets, program inputs, and the expected result:

Data File data.csv

1, 4.00, burger

1, 8.00, tofu_log

2, 5.00, burger

2, 6.50, tofu_log

Program Input:

program data.csv burger tofu_log

Expected Output:
=> 2, 11.5



Data File data.csv

3, 4.00, chef_salad

3, 8.00, steak_salad_sandwich

4, 5.00, steak_salad_sandwich

4, 2.50, wine_spritzer

Program Input:

program data.csv chef_salad wine_spritzer

Expected Output

=> nil (or null or false or something to indicate that no matching restaurant could be found)


Data File data.csv

5, 4.00, extreme_fajita

5, 8.00, fancy_european_water

6, 5.00, fancy_european_water

6, 6.00, extreme_fajita, jalapeno_poppers, extra_salsa

Program Input:

program data.csv fancy_european_water extreme_fajita

Expected Output

=> 6, 11.0
