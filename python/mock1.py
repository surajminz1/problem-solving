# Implement a function to reverse a linked list (you don't need to define a full linked list class, just the logic).
# Complexity: 
# Desired time: 
# Time taken to solve: 

def get_table_name(query):
    token = query.split()
    res = []
    for i in range(len(token)):
        if (token[i] == "from" or token[i] == "join") and ( token[i+1] != "(" ):
            res.append(token[i+1])
    return res

print(get_table_name("select * from table1")) # table1
print(get_table_name("select * from ( select * from table1 )")) # table1
print(get_table_name("select * from table1 inner join table2")) # [table1, table2]


def one_element_removed(full, missing):
    i,j = 0,0
    while i < len(full) and j < len(missing):
        if full[i] != missing[j]:
            return full[i]
        else:
            i += 1
            j += 1
    return full[i]

print(one_element_removed([1,2,3,4,5], [1,2,3,5])) # -> 4
print(one_element_removed([1,2,3,5], [1,2,3])) # -> 5
print(one_element_removed([1], []))  # -> 1
print(one_element_removed([1,2,3,4,4,5], [1,2,3,4,5])) # -> 4


def aggregate_reviews_best_index_safety(platforms, seven_day_data):
    agg_lst = []
    for platform in platforms:
        if platform in seven_day_data:
            platform_data = seven_day_data[platform]
            #print(platform,platform_data)

            for i, value in enumerate(platform_data):
                if len(agg_lst) > i:
                    agg_lst[i] += value
                else:
                    agg_lst.append(value)

    return agg_lst

print(aggregate_reviews_best_index_safety(['ios', 'android', 'web'],
{'ios': [1, 2, 3, 4, 5, 6, 7], 'android': [8, 7, 6, 5, 4, 3, 2], 'web': [0, 1, 2, 3, 4, 5, 6]},
)) # [9, 10, 11, 12, 13, 14, 15]

print(aggregate_reviews_best_index_safety(['android', 'web'],
{'ios': [1, 2, 3, 4, 5, 6, 7], 'android': [8, 7, 6, 5, 4, 3, 2], 'web': [0, 1, 2, 3, 4, 5, 6]},
)) # [8, 8, 8, 8, 8, 8, 8]

print(aggregate_reviews_best_index_safety(['android', 'web'],
{'ios': [1, 2, 3, 4, 5, 6, 7], 'android': [8, 7, 6, 5, 4, 3], 'web': [0, 1, 2, 3, 4, 5, 6]},
)) # [8, 8, 8, 8, 8, 8, 6]

print(aggregate_reviews_best_index_safety([],
{'ios': [1, 2, 3, 4, 5, 6, 7], 'android': [8, 7, 6, 5, 4, 3, 2], 'web': [0, 1, 2, 3, 4, 5, 6]},
)) # []
