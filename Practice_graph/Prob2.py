#mark visited

edge=[['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]
   
#list to json format
graph= {
    'i': ['j', 'k'],
    'j': ['i','k'],
    'k': ['i', 'm', 'l','j'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'], 
    'n': ['o']
}