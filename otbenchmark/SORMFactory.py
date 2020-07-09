# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:28:04 2020

@author: Jebroun
"""

import openturns as ot


class SORMFactory(ot.SORM):
    def __init__(self, problem):
        myEvent = problem.getEvent()
        inputVector = myEvent.getAntecedent()
        myDistribution = inputVector.getDistribution()
        solver = ot.AbdoRackwitz()
        super(SORMFactory, self).__init__(solver, myEvent, myDistribution.getMean())
        return None
