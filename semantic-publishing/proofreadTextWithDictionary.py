 # -*- coding: utf-8 -*-
 
""" 
 Use Semantic Publishing API to proofread a text including a user-defined dictionary.  
 
 The examples creates a dictionary and add three entries: two entities and a concept.
  
 Text is analyzed including the user-defined dictionary.
  
 Error and their types are printed as well as suggestions to improve the text. Entities defined in the dictionary are taken as known words and are not reported as errors.
 
 Finally, the dictionary is deleted - you don't need to do this every time. 
 
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
from Domain import Dictionary, Model, Category, Entity, Concept


textalytics = SemPubClient(KEY)

try: 
	dictionary = Dictionary('got', 'en', 'Entities and concepts from A Song of Ice and Fire.');
	textalytics.createDictionary(dictionary)

	kingsLanding = Entity('01', "King's Landing")
	kingsLanding.setType('Top>Location>GeoPoliticalEntity>City')
	kingsLanding.addTheme('Top>Society>Military')
	kingsLanding.addTheme('Top>Society>Politics')
	textalytics.createEntity(kingsLanding, dictionary)

	jon = Entity('02', "Jon Snow")
	jon.setType('Top>Person>FullName')
	jon.addAlias("Ned Stark's bastard")
	jon.addAlias('Bastard of Winterfell')
	jon.addTheme('Top>Society>Military')
	jon.addTheme('Top>Society>Politics')
	textalytics.createEntity(jon, dictionary)


	direwolf = Concept('03', "direwolf")
	direwolf.setType('Top>LivingThing>Animal>Vertebrate>Mammal')
	direwolf.addAlias('direwolves')
	textalytics.createConcept(direwolf, dictionary)

	text = "On Tuesday, author George R.R. Martin stated that his novels take place in an universe meant to be a completely alternate and separate world not linked to our own in any way . It's easy to tell the difference when the plot concerns direwolves, dragons or skinchangers, but the power games that take place in King's Landing could very well be taken from any of the European royal families in Middle Ages, down to the abundance — and associated taint — of children conceived out of marriage, as we see with Ned Stark's bastard."; 

	result = textalytics.checkText(text,'en', 0, dictionary)

	print 'Issues -------------------------------'
	for issue in  result['issue_list']:
		print issue['text'] + " : " +issue['type']
		for suggestion in  issue['sug_list']:
			print '\t==> ' + suggestion['form'] + " (confidence: " + suggestion['confidence'] +")"
		print
	print 

except SemPubException as e:
	print 'Error: ' + str(e)
finally: 
	textalytics.deleteDictionary(dictionary)
