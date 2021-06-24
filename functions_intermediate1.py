x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

(x[1][0]) = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30



students2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for k in some_list:
            print(f"first_name - {k['first_name']}, last_name -{k['last_name']}")
iterateDictionary(students2)


def iterate_dictionary2(key_name, some_list):
    for j in some_list:
        print(j[key_name])
iterate_dictionary2('first_name', students2)

def iterate_dictionary2(key_name, some_list):
    for j in some_list:
        print(j[key_name])
iterate_dictionary2('last_name', students2)



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterateDic(dict):


    for j in dict:
        print(str(len(dict[j])) + ' ' + j.upper())
        for k in dict[j]:
            print(k)

        
iterateDic(dojo)



