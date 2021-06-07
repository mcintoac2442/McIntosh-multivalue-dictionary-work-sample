'''
This module allows the use of the MultiValueDictionary class. No outside functions or variables exist in this module.

Classes:
--------
    MultiValueDictionary
'''

# The base data structure is a generic dictionary, since keys should still be unique.
# Each member is represented as a set, since values are unique and unordered.
class MultiValueDictionary:
    '''
    A class to act similarly to a typical Python dictionary. However each key can hold multiple unique values.

    Attributes
    ----------
        _multivalue_dict : dict
            Used internally as the primary data structure for keys. Members are stored as sets inside of here.

    Methods
    -------
        KEYS():
            Prints and returns a set of keys.
        MEMBERS(key):
            Prints and returns a set of members for a given key
        ADD(key, member)
            Adds member to the set for a given key if not already a member.
        REMOVE(key, member)
            Removes the member from the given key. If it is the only member, the key is also removed.
        REMOVEALL(key)
            Removes all members from the given key. Also removes key.
        CLEAR()
            Removes all keys and all members from the dictionary.
        KEYEXISTS(key)
            Returns whether a key exists or not.
        MEMBEREXISTS(key, member)
            Returns whether a member exists with a key. Returns false if the key does not exist.
        ALLMEMBERS()
            Prints and returns all members in the dictionary in the form of a list.
        ITEMS()
            Prints all individual key-value pairs in the dictionary.
    '''

    def __init__(self):
        '''
        Constructs the internal dictionary for the MultiValueDictionary object

        Parameters
        ----------
            None
        '''
        self._multivalue_dict = {}

    def KEYS(self):
        '''
        Prints and returns a set of keys. Order is not guaranteed.

        If no keys exist, prints empty set and returns None.

        Parameters
        ----------
            None

        Returns
        -------
            keys: a set of all keys in the dictionary
        '''
        keys = self._multivalue_dict.keys()
        if not keys:
            print("(empty set)\n")
            return
        else:
            index = 1
            for key in keys:
                print("{}) {}".format(index, key))
                index += 1
        print()
        return keys

    def MEMBERS(self, key):
        '''
        Prints and returns a set of members for a given key. Return order is not guaranteed.

        Prints an error and returns None if the key does not exist.

        Parameters
        ----------
            key: The key to gather members from.

        Returns
        -------
            members_set: A set of all members for the given key.
        '''
        members_set = self._multivalue_dict.get(key)
        if members_set is None:
            print("ERROR, key does not exist\n")
            return
        else:
            index = 1
            for member in members_set:
                print("{}) {}".format(index, member))
                index += 1
        print()
        return members_set

    def ADD(self, key, member):
        '''
        Adds member to the set for a given key if not already a member.

        Prints an error and returns None if the member already exists for the key.

        Parameters
        ----------
            key: The key to add the member to.
            member: The member to be added.

        Returns
        -------
            self: This MultiValueDictionary object.
        '''
        members_set = self._multivalue_dict.get(key)
        if members_set is None:
            self._multivalue_dict[key] = {member}
            print("Added\n")
        else:
            if member in members_set:
                print("ERROR, member already exists for key\n")
                return
            else:
                members_set.add(member)
                self._multivalue_dict[key] = members_set
                print("Added\n")
        return self

    def ADDMANY(self, key, *members):
        '''
        Adds an arbitary amount of members to a given key if not already a member.

        If any members are already a member of the given key, they will not be added.

        If all members already exist for a given key, an error will be displayed and
        None will be returned.

        If members is empty, an error will be displayed and None will be returned.

        Parameters
        ----------
            key: The key to add the members to.
            members: An arbitary sized amount of members to be added.

        Return
        ------
            self: This MultiValueDictionary object.
        '''
        added = False
        members_set = self._multivalue_dict.get(key)
        if not members: #members list is empty
            print("ERROR, must include at least one member to add.")
            return
        if members_set is None: #adding a new key
            self._multivalue_dict[key] = {*members}
            added = True
        else:
            for member in members:
                if member in members_set: #member already exists for key
                    print("ERROR, {} already exists for key. Skipping add.\n".format(member))
                else:
                    members_set.add(member)
                    added = True
            self._multivalue_dict[key] = members_set
        if added:
            print("Added.\n")
            return self
        else:
            print("ERROR, all members already exist for key.")
            return None

    def REMOVE(self, key, member):
        '''
        Removes the member from the given key. If it is the only member, the key is also removed.

        If the given key or member does not exist, an error message is printed and None is returned.

        Parameters
        ----------
            key: The key to remove a member from.
            member: The member to be removed.

        Returns
        -------
            self: This MultiValueDictionary object.
        '''
        members_set = self._multivalue_dict.get(key)
        if members_set is None:
            print("ERROR, key does not exist\n")
            return
        else:
            try:
                members_set.remove(member)
                if len(members_set) is 0:
                    self._multivalue_dict.pop(key)
                else:
                    self._multivalue_dict[key] = members_set
            except(KeyError):
                print("ERROR, member does not exist\n")
                return
            print("Removed\n")
        return self

    def REMOVEALL(self, key):
        '''
        Removes all members from the given key. Also removes key.

        If the key does not exist, prints an error message and returns None.

        Parameters
        ----------
            key: The key to remove all members from, and remove from the dictionary.

        Returns
        -------
            self: This MultiValueDictionary object.
        '''
        members_set = self._multivalue_dict.get(key)
        if members_set is None:
            print("Error, key does not exist\n")
            return
        else:
            self._multivalue_dict.pop(key)
            print("Removed\n")
        return self

    def CLEAR(self):
        '''
        Removes all keys and all members from the dictionary.

        Parameters
        ----------
            None

        Returns
        -------
            self: This MultiValueDictionary object.
        '''
        self._multivalue_dict.clear()
        print("Cleared\n")
        return self

    def KEYEXISTS(self, key):
        '''
        Returns whether a key exists or not.

        Parameters
        ----------
            key: The key to check the existance of.

        Returns
        -------
            True or False
        '''
        if key in self._multivalue_dict:
            print("true\n")
            return True
        else:
            print("false\n")
            return False
        
    def MEMBEREXISTS(self, key, member):
        '''
        Returns whether a member exists with a key. Returns false if the key or member does not exist.

        Parameters
        ----------
            key: The key to which the member should belong.
            member: The member to check for.

        Returns
        -------
            True of False
        '''
        members_set = self._multivalue_dict.get(key)
        if members_set is None or member not in members_set: #Due to short circuiting, we only need one if statement
            print("false\n")
            return False
        else:
            print("true\n")
            return True
            
    def ALLMEMBERS(self):
        '''
        Prints and returns all members in the dictionary in the form of a list.

        Prints empty set and returns None if no members exist. Order is not guaranteed.

        Parameters
        ----------
            None
            
        Returns
        -------
            members_list: A list of all members for every key in the dictionary.
        '''
        members_sets = self._multivalue_dict.values() #Returns a list of sets, avoids using .get calls
        if not members_sets:
            print("(empty set)\n")
            return
        else:
            index = 1
            members_list = [] #Lists allow duplicates, combines all sets, used for return
            for members_set in members_sets:
                for member in members_set:
                    members_list.append(member)
                    print("{}) {}".format(index, member))
                    index += 1
        print()
        return members_list

    def ITEMS(self):
        '''
        Prints all individual key-value pairs in the dictionary.

        Returns None if the dictionary is empty, otherwhise returns a set of all tuple pairs.
        Order is not guaranteed.

        Parameters
        ----------
            None

        Returns
        -------
            all_tuples_set: A set of all one to one (one key to one value) tuples in the dictionary
        '''
        items = self._multivalue_dict.items() #Returns a list of tuples, tuple[0] = key, tuple[1] = set, avoids using .get calls
        if not items:
            print("(empty set)\n")
            return
        else:
            all_tuples_set = set() #Since tuples should be unique, use set. For each
            index = 1
            for item in items:
                for member in item[1]:
                    print("{}) {}: {}".format(index, item[0], member))
                    all_tuples_set.add((item[0], member))
                    index += 1
        print()
        return all_tuples_set