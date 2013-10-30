# myclient.py -- Simple client to use textalytics.com 
#                Social Media Analysis service 
# 
# @version    -- 1.0 
# @author     -- cdepablo 
# @contact    -- http://www.textalytics.com (http://www.daedalus.es)
# @copyright  -- Copyright (c) 2013, DAEDALUS S.A. All rights reserved.

import smaclient
import argparse


def main(key, text, fields):
        ''' Analyze a text and extract relevant fields. A usage key for textalytics.com is required '''
	client = smaclient.SmaClient(key)
	client.fields= fields
	document = smaclient.Document("0", text)
	document.language = "es"
	document.source = "UNKNOWN"
        document.itf = "txt"

	response = client.analyze(document)
        if (isinstance(response,smaclient.Response)):
                printr(response.result)
        elif (isinstance(response,smaclient.Error)):
                print response
        else:
                print "Unknown error"
        

def printr(result):
        ''' Print API call results '''
        if hasattr(result, 'sentiment'):
                print u'\nSentiment'
                print result.sentiment

        if hasattr(result, 'categorization'):
                print u'\nCategorization'
                for c in result.categorization:
                        print u' '.join((c.code, u' - '.join (c.labels), str(c.relevance)))

        if hasattr(result, 'entities'):
                print u'\nEntities'
                for e in result.entities:
                        print u' '.join((e.form,'[',e.type, u','.join(e.variants), str(e.relevance),']'))
        
        if hasattr(result, 'concepts'):
                print u'\nConcepts'
                for c in result.concepts:
                        print u' '.join((c.form,'[', u','.join(c.variants), str(c.relevance),']'))

        if hasattr(result, 'timeExpressions'):
                print u'\nTime Expressions'
                for t in result.timeExpressions:
                        print u' '.join((t.form,u'[', getattr(t,'time',u''), getattr(t,'date',u''), u']'))

        if hasattr(result, 'moneyExpressions'):
                print u'\nMoney Expressions'
                for m in result.moneyExpressions:
                        print u' '.join((m.form, u'[', getattr(m,'amount',u''), getattr(m,'currency', u''), u']'))

        if hasattr(result, 'uris'):
                print u'\nUris'
                for uri in result.uris:
                        print u' '.join((uri.form, uri.type))

        if hasattr(result, 'phoneExpressions'):
                print u'\nPhone Expressions'
                for p in result.phoneExpressions:
                        print p.form


if __name__ == "__main__":
        ''' Parse arguments and invoke textalytics.com service'''
	parser = argparse.ArgumentParser("Process a document with Textalytics.com Social Media Analytics")
	parser.add_argument("key", help="service key")
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--text", help="Text to analyze")
        group.add_argument("--file", help="File with text to analyze")
	parser.add_argument("--fields", help="analysis fields to include in the output separated by commas")
	args = parser.parse_args()

	text = None
	if args.text:
		text = args.text
	if args.file:
		text = open(args.file).read()
    	
	print text
	
	if args.fields:
		fields = args.fields.replace(',','|')	
	else:
		fields=""

	main(args.key,text,fields)
