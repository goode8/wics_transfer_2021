"""
*****************************************************************************************
Filename:       college.py
Author:         Edgar Aguilar
Date:           April 22, 2021

Description:    This module represents the College class.
******************************************************************************************
"""


class College:
    """
    A class to represent a college object.
    Methods:
        __init__(self, name, state, pub_priv, cost, alum_sal):  Instantiates a College object
        __str__(self): Returns a string with the college data
        get_name(self): Returns the college name
        get_state(self): Returns the college state
        get_pub_priv(self): Returns the college type (public or private)
        get_cost(self): Returns the college cost
        get_alum_sal(self): Returns the alumni salary
    """
    def __init__(self, name, state, pub_priv, cost, alum_sal):
        """
        ********************************************************************************************************
        Method:         __init__(self, name, state, pub_priv, cost, alum_sa):
        Parameters:     self, name, state, pub_priv, cost, alum_sal
        Outputs:        none
        Returns:        none
        Author:         Edgar Aguilar
        Date:           April 8, 2021
        Modification:
        Description:    This constructor instantiates a college with the given fields
        *******************************************************************************************************
        """
        self._name = name
        self._state = state
        self._pub_priv = pub_priv
        self._cost = cost
        self._alum_sal = alum_sal

    def __str__(self):
        return "Name: %s, %s\nSchool type: %s\nCost: $%s\nAlumni salary: $%s\n" % \
               (self._name, self._state, self._pub_priv, "{:,}".format(int(self._cost)), "{:,}".format(int(self._alum_sal)))

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def get_pub_priv(self):
        return self._pub_priv

    def get_cost(self):
        return self._cost

    def get_alum_sal(self):
        return self._alum_sal

