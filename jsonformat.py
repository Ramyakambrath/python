from collections import OrderedDict
import json

def next_node(node, key):
    result = None
    children = node.setdefault('children', [])
    for child in children:
        if child['name'] == key:
            result = child
    if not result:
        result = OrderedDict(name=key)	
        children.append(result)
    return result


fake_csv = [ '1099 Pro,"1099 Pro, Inc. 1099 Pro 2010 Enterprise 2016.07.25 Enterprise",Core,10,FALSE,0,10,0,0,,,Unknown,0',
'16 Software,16 Software Breevy 3.28 3.35,Instance,15,FALSE,13,2,13,0',
'1E,1E PXE Lite Local 2,Instance,7,FALSE,7,0,7,0',
'Microsoft,Microsoft Office 2013 Professional Plus,Instance,1,FALSE,0,1,0,0,,,Unknown,0',
'Microsoft,Microsoft Office 2016 Professional,Instance,20,FALSE,5,15,5,2,,,Unknown,0',
'Microsoft,Microsoft Office 2016 Professional Plus,Instance,50,FALSE,11,39,11,14,,,Unknown,0'
]

tree_root = OrderedDict(name='flare')	
		 
for line in fake_csv:
    categories = line.split(',')
    print(categories)
    node = tree_root
    for cat in categories:
        print(cat)
        node = next_node(node, cat)
	
