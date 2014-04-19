import json
import time


entry = {}
entry['comments_id'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8',
entry['title'] = 'Dive into history, 2009 edition'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['publish_date'] = time.strptime('Fri Mar 27 22:20:42 2009')
entry['published'] = True


def to_json(pyobj):
    if isinstance(pyobj, bytes):
        return {'__class__': 'bytes',
                '__value__': list(pyobj)}

    #if isinstance(pyobj, time.struct_time):
        #return {'__class__': 'time.asctime',
                #'__value__': time.asctime(pyobj)}

with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(entry, f, indent=2, default=to_json)
