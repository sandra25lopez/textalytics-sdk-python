# -*- coding: utf-8 -*-

"""
 Analyzes a text with the Semantic Tagging service. 
 Extract document categories, relevant entities, concepts and time expressions
 
 Check out the documentation to extract additional data like quotations, 
 money expressions, uris, phones and even links to Linked Data.  
 
 To run this example, the license key  for the Semantic Publishing API must be included
 in the KEY variable  in 'config.py' file. 
 If you don't know your key, check your personal area at Textalytics (https://textalytics.com/personal_area)
 
 @author     Textalytics
 @version    1.0 -- 03/2014
 @contact    http://www.textalytics.com (http://www.daedalus.es)
 @copyright  Copyright (c) 2014, DAEDALUS S.A. All rights reserved.
"""

from config import KEY
from SemPubClient import SemPubClient
from SemPubException import SemPubException

text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves, dragons or skinchangers, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

try:
	textalytics = SemPubClient(KEY)
	result = textalytics.analyzeText(text,'en')

	print 'Categorization----------------------------'
	for category in  result['category_list']:
		print ' - '.join(category['label_list']) + " : " + category['relevance']
	print 

	print 'Entities -------------------------------'
	for entity in  result['entity_list']:
		print entity['form'] + " : " +entity['type']
	print 

	print 'Concepts --------------------------------'
	for concept in  result['concept_list']:
		print concept['form'] + " : " + concept['type']
	print 

	print 'Time expressions ------------------------'
	for timex in  result['time_expression_list']:
		print timex['form'] 
	print 
except SemPubException as e:
	print 'Error: ' + str(e)
