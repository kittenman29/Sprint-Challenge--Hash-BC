#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
        # this prints the index that you want
        print(hash_table_retrieve(ht, weights[i]))

    for i in range(length):
        if hash_table_retrieve(ht, limit - weights[i]):

            # put the biggest index first
            if i > hash_table_retrieve(ht, limit - weights[i]):
                print()
                return (i, hash_table_retrieve(ht, limit - weights[i]))

            else:
                return (hash_table_retrieve(ht, limit-weights[i]), i)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# print_answer('21')
weights_3 = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights_3, 5, 21)

# get_indices_of_item_weights([9])
