## What is a blockchain and how does it work?

At it's core is't just a linked list but instead of pointers for the previous element you use the previous block hash.

Blockchains can store objects of any data.

The chain is forged by people mining with a proof of work algorithm. This algorithm is an assymetric cryptographic proof which can only be solved by brute forcing a solution to an arbitrarily hard math problem which is brute forced by ASICs.

The chain is agreed upon through a process called consensus. Consensus is the process of relaying messages to nodes in the network that tell each other which blocks have been mined. The nodes agree upon consensus by following a longest valid chain rule in which the longest chain that has been mined and includes transactions which have not been double spent is considered the tip of the blockchain.

---

---

## What is an array and how does it work?

An array is a sequence of elements of the SAME TYPE stored in the same size of CONTIGUOUS MEMORY.

Arrays are so commonly used because accessing elements within them can be done in constant run time and they are space efficient because they don't take up any more space than the memory than they request.

Arrays are initialized when you request the size of the array in bits from your computer and it initializes that memory and returns the memory address of the start of the reserved block of memory.

Accessing each element in an array can be done by index \* sizeOf(type) + start_address

---

---

## What is a hash table and how does it work?

Hash tables are used to implement tons of different data types in computer science like objects, dictionaries, caches, and memoization.

Hash tables store a key: value pair in contiguous memory, but often time require more memory blocks of memory than elements in the hash table.

They are the fastest data structure with an average constant big O runtime for search, insertion and deletion and a worst case runtime of linear time.

Elements are stored as integers in the hash table by converting the key to an index integer via a hash function. The hash function converts the key into an integer by doing some bitwise operation or math and taking the modulo of the return value.

A good hash table will have an even distribution of elements across the indices to reduce collisions.

A collision is when two element hashes result in the same index. When this happens the elements are stored at that same index value but are connected to the primary element at that index via a linked list.
