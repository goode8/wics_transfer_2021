from college import College
import csv

"""
*****************************************************************************************
Filename:       topColleges.py
Author:         Edgar Aguilar
Date:           April 22, 2021

Description:    This module represents the TopCollege class.
******************************************************************************************
"""


class TopCollege:
    """
    A class to represent top colleges.
    Methods:
        __init__(self, file_name):  Instantiates a TopCollege object
        return_by_num(self): Returns a list of state abbreviations, from most to least number of colleges per state
        return_by_type(self, school_type): Returns a generator of all schools, either public or private
        return_by_sal(self, min_sal): Returns a generator of college info for all schools above a minimum salary
        return_by_match5(self, school_name="None", state_list=None): Returns a list of all schools matching a given
            name and/or state
    Class attribute:  input_file: The data file to be read
    """
    input_file = "topcolleges.csv"

    def __init__(self, file_name=input_file):
        """
        ********************************************************************************************************
        Method:         __init__(self, name, state, pub_priv, cost, alum_sa):
        Parameters:     self, file_name (defaults to topcolleges.csv"
        Instance var's: _file_name, the file to be read; _dict1, a dictionary of state abbreviations as keys,
                        and a list of colleges as the value; _college_list; a list of college objects; and
                        list_of_states, a list sorted by most to least number of colleges per state
        Outputs:        none
        Returns:        none
        Author:         Edgar Aguilar
        Date:           April 8, 2021
        Modification:
        Description:    This constructor instantiates a TopCollege object by reading the input file, creating a
                        college object for each line, and appending the college object to both _college_list
                        and _dict1
        *******************************************************************************************************
        """
        self._file_name = file_name
        self._dict1 = {}                # How to use collections.defaultdict(list) here (question during class)??

        # fields = []
        rows = []
        self._college_list = []

        with open(self._file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
                rank = int(row[0])
                name = row[1]
                # city = row[2]
                state = row[3]
                pub_priv = row[4]
                # pop1 = row[5]
                # pop2 = row[6]
                # net_price = row[7]
                # grant_aid = row[8]
                cost = row[9]
                alum_sal = row[10]
                # accept_rate = row[11]
                # lo_SAT = row[12]
                # hi_SAT = row[13]
                # lo_ACT = row[14]
                # hi_ACT = row[15]
                # website = row[16]

                # Create a college object
                college = College(name, state, pub_priv, cost, alum_sal)
                self._college_list.append(college)

                # Add the college to the state list
                if state in self._dict1:
                    # self._dict1.get(state).append(name)
                    self._dict1[state].append(college)
                else:
                    state_list = []
                    self._dict1[state] = state_list
                    state_list.append(college)

        # Create a list of states sorted by most to least number of colleges per state
        sorted_dict = sorted(self._dict1, key=lambda state: len(self._dict1[state]), reverse=True)
        self.list_of_states = []
        for k in sorted_dict:
            self.list_of_states.append(k)

    def get_name(self, index):
        return self._college_list[index].get_name()

    def get_state(self, index):
        return self._college_list[index].get_state()
