 # -*- coding: utf-8 -*-

"""  
 Use Semantic Publishing API to proofread a text. 
 
 Error and their types are printed as well as suggestions to improve the text  
 
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

textalytics = SemPubClient(KEY)

try: 
	result = textalytics.checkText(text,'en')

	print 'Issues -------------------------------'
	for issue in  result['issue_list']:
		print issue['text'] + " : " +issue['type']
		for suggestion in  issue['sug_list']:
			print '\t==> ' + suggestion['form'] + " (confidence: " + suggestion['confidence'] +")"
		print
	print 
except SemPubException as e:
	print 'Error: ' + str(e)