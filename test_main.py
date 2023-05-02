# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:00:08 2023

@author: Renato Marino Henz

Unit tests for the created system

"""

# Importing dependencies
import unittest

# Importing the function to be tested
from main import answer_question

# Defining the context to be used in the tests
with open('data/ipcc.txt', 'r', encoding='utf8') as f:
    context = f.read()

# Defining the main test cases
class TestAnswerIPCC(unittest.TestCase):
    def test_definition(self):
        res = answer_question(context, question="What is the IPCC?")
        self.assertIn('scientific intergovernmental body under', res['answer'])
    
    def test_creation_request(self):
        res = answer_question(context, question="Who requested the IPCC creation?")
        self.assertIn('member governments', res['answer'])
    
    def test_organization_part(self):
        res = answer_question(context, question="What organization is the IPCC a part of?")
        self.assertEqual('United Nations', res['answer'])
    
    def test_organization_established(self):
        res = answer_question(context, question="What UN organizations established the IPCC?")
        self.assertIn('WMO', res['answer'])
        self.assertIn('UNEP', res['answer'])
    
    def test_objective(self):
        res = answer_question(context, question="What does the UN want to stabilize?")
        self.assertIn('greenhouse gas concentrations', res['answer'])
    
    def test_established_at(self):
        res = answer_question(context, question="When was IPCC first established?")
        self.assertEqual('1988', res['answer'])
    
    def test_membership(self):
        res = answer_question(context, question="Who can be a member of IPCC?")
        self.assertEqual('all members of the WMO and UNEP', res['answer'])

# Running the tests
if __name__=='__main__':
	unittest.main()
