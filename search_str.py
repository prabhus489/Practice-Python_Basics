DB_Collection = {'Name':['Prabhu','Ram','Lakshmi'],
          'Email':['prabhu.s@eattributes.com','ram@abcd.com','lakshmi@eattributes.com'],
          'address': ['34 Main Street, 212 First Avenue','54 Main Street, 212 Second Avenue','64 Main Street, 212 Third Avenue'],
          'Phone':['7401256086','8401358086','7256789086']}

input = str(input('enter string:'))

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None
print(search(DB_Collection,input))