# Python

## How to use Dict

### Making a dictionary ###

data = {}
# OR
data = dict()

### Initially adding values ###

data = {'a':1,'b':2,'c':3}
# OR
data = dict(a=1, b=2, c=3)

### Inserting/Updating value ###

data['a']=1  # updates if 'a' exists, else adds 'a'
# OR
data.update({'a':1})
# OR
data.update(dict(a=1))
# OR
data.update(a=1)

### Merging 2 dictionaries ###

data.update(data2)  # Where data2 is also a dict.

### Deleting items in dictionary ###

del data[key] #Remove specific element in a dictionary
data.pop(key) #Removes the key & returns the value
data.clear() #Clear entire dictionary

[Ref](http://stackoverflow.com/questions/1024847/add-key-to-a-dictionary-in-python)

## DocString

- [PEP 0257](https://www.python.org/dev/peps/pep-0257/)
