# Gryps Tech Interview Challenge
Warmup) Write a function called `warmup(count)` that prints numbers starting a 1 to `count` including count.

1) Write a function called `left_join(left_dict, right_dict, left_key_to_match, right_key_to_match, keys_to_include)` in `left_join.py`  
    A) That takes the input dicts and assumes each key in the dicts contains an array. The function should perform a left join operation. A left join should perform a join starting with `left_dict` and including any keys in `keys_to_include`. Then, it should fetch any keys from `right_dict` in `keys_to_include` where `left_key_to_match == right_key_to_match`. Keys in `keys_to_include` with no match should have None in the returned item.   

    B) For further info see: https://www.mysqltutorial.org/mysql-left-join.aspx

    C) Write a unit test for this

    D) Example
```
Left_dict = {“id”: [10, 11, 12, 13], “item_id”: [1,2,2,6], “values1”: [“c”, “d”, “e”, “l”]}
Right_dict = {“item_id”: [1,2,3,4], “values2”: [“z”, “x”, “y”, “w”]}
Left_key_to_match = “item_id”
Right_key_to_match = “item_id”
Keys_to_include = [“id”, “item_id”,  “values2”]
Returns: {“id”: [10, 11, 12, 13], “item_id”: [1, 2, 2, 6], “values2”: [“z”, “x”, “x”, None]}
```

2) *The following are based on the result from “1”*  
    A) Using the `Threading` or `Multiprocessing` libraries, create a program that submits to left_join asynchronously. `left_join.py`  
    B) Write an integration test for this  
3) *The following are based on the result from “1”*  
    A) Using `Flask`, write a completely different service that processes the data in JSON via a POST request  
    B) Write an integration test for this using `Requests` (or another appropriate library)
4) Write a function called `filter_string(list_of_strings, regex_filter)`. The function should return all items in `list_of_strings` that match `regex_filter`.  
    A) Write a unit test for this
5) Write a class with the following functions `basic_class.py`:  
    A) `Insert(item)`: Insert the item into the class storage container. Should it have a return value?  
    B) `Retrieve(<something>)`: Retrieve an item from the class by some mechanism  
    C) `Check(item)`: Check if an item is already in the object  
    D) Write a unit test for the class  
    E) Discuss the performance of the class and whether anything could be more efficient  

