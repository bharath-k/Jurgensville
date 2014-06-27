Expected output for test cases

data4 - value in combo is lesser.
data5 - direct match for combo.
data6 - combo present, but no match.
data7 - combo pack two of the same item.

$ python best-price.py data1.csv burger
1 , 4.0

$ python best-price.py data1.csv burger tofu_log
2 , 11.5

$ python best-price.py data2.csv chef_salad wine_spritzer
No restaurants found for given menu items.

$ python best-price.py data3.csv fancy_european_water extreme_fajita
6 , 11.0

$ python best-price.py data4.csv burger
2 , 3.5

$ python best-price.py data5.csv burger tofu_log
2 , 7.0

$ python best-price.py data6.csv burger tofu_log
2 , 8.0

# Two of the same menu items.
$ python best-price.py data6.csv burger burger
2 , 6.0

$ python best-price.py data7.csv burger burger
2 , 5.0

$ python best-price.py data8.csv burger burger burger burger burger coffee macaroni pizza
2 , 26.0
