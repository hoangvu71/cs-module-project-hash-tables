class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.table = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        count = 0
        for eachLine in self.table:
            if eachLine != None:
                count += 1

        load_factor = count / self.capacity
        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        node = HashTableEntry(key, value)
        index = self.hash_index(key)
        
        # Put so that no collison 
        # if there's node in that array, put this into a function to use recursive
        def no_collison_put(nodeF):
            if nodeF != None:
                # check if that node is the same as what we have
                    # if it is the same, update that node
                    next_node = nodeF.next
                    if nodeF.key == key:
                        #update node
                        nodeF.value = value
                        return nodeF
                    # if it is not the same and there's no node after that,
                    elif nodeF.key != key and nodeF.next == None:
                        #  add that node to the head
                        old_head = nodeF
                        nodeF = node
                        nodeF.next = old_head
                        self.table[index] = nodeF
                        return nodeF
                    # if it is not the same, go to the next node and repeat
                    elif self.table[index].key != key:
                        return no_collison_put(next_node)
        # if there's no node in that array
        if self.table[index] == None:
            # put that node in that array
            self.table[index] = node
       
        else:
            no_collison_put(self.table[index])


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        # if node is empty
        if self.table[index] == None:
            # return None
            return None
        
        # if node is not empty
        if self.table[index] != None:
        # if head.key is fit and there's no next
            if self.table[index].key == key and self.table[index].next == None:
            # make head = None
                self.table[index] = None
        
        # if head.key is fit and there's next
            elif self.table[index].key == key and self.table[index].next != None:
            # make head = currentNode.next
                self.table[index] = self.table[index].next
        
        # else key must fit in one of the node after
            else: 
        # put it in a function with previous and current node
                def no_collison_delete(previousNode, currentNode):
                    # if key fit and next node == None
                    if currentNode.key == key and currentNode.next == None:
                        # then previousnode.next == None
                        previousNode.next = None
                        return previousNode
                    
                    # if key fit and next node != None
                    elif currentNode.key == key and currentNode.next != None:
                        # then previousnode.next = currentnode.next
                        previousNode.next = currentNode.next
                        return previousNode
                    else:
                        next_node = currentNode.next
                        return no_collison_delete(currentNode, next_node)
        # no_collison_delete(previousNode, currentNode)
                no_collison_delete(self.table[index], self.table[index].next)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        # get all the value, include the ones that is in the linked list
        # check to see if there's anything in that index
        # if there is not
        if self.table[index] == None:
            # return None
            return None
        
        # if there is, put this into a function for a recursive call to next node
        else:
            def no_collison_get(node):
                if node != None:
                    # check the key
                    # if key is the same
                    next_node = node.next
                    if node.key == key:
                        # return the value
                        return node.value
                    # elif key is not the same and there's no next value in linkedlist:
                    elif node.key != key and node.next == None:
                        # return None
                        return None
                    # elif key is not he same and there's a next value in linkedlist
                    elif node.key != key and node.next != None:
                        # move to the next node
                        return no_collison_get(next_node)

            return no_collison_get(self.table[index])

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # copy the entire database to another table
        # make the capacity double
        # for each line in the copied_database, we get the node and put it into the new database

        # but first we need to make sure that the conditions are met
        # conditions are if the nodes take up to 0.7 of load factor
        # then we resize
       
        if self.get_load_factor() >= 0.7:
            copy_database = self.table
            self.capacity = new_capacity
            self.table = [None] * self.capacity

            for eachLine in copy_database:
                while eachLine != None:
                    self.put(eachLine.key, eachLine.value)
                    eachLine = eachLine.next


if __name__ == "__main__":
    # ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    
    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")

    ht = HashTable(4)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    return_value = ht.get("key-9")
    print(return_value)