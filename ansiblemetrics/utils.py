def keyValueList(d, key=None): 
    """ 
    This function iterates over all the key-value pairs of a dictionary and returns a list of tuple (key, value) where the key contain only primitive value (i.e., no list or dict), e.g., string, number etc.
    d -- a dictionary to iterate through
    """
    if not isinstance(d, dict) and not isinstance(d, list):
        return []
    
    keyvalues = []
    
    if isinstance(d, list):
        for entry in d:
            if isinstance(entry, dict):
                keyvalues.extend(keyValueList(entry))
            else:
                keyvalues.append((key, entry))
    else:
        for k, v in d.items():
            if k is None or v is None:
                continue
            if not isinstance(v, dict) and type(v) != list:
                keyvalues.append((k,v))
            elif isinstance(v, list):
                keyvalues.extend(keyValueList(v, k))
            else:
                keyvalues.extend(keyValueList(v))
                
    return keyvalues


def allKeys(d): 
    """ 
    Returns a list of all the keys of a dictionar (duplicates included)
    d -- a dictionary to iterate through
    """
    if d is None or not isinstance(d, dict) and not isinstance(d, list):
        return []
    
    keys = []
    
    if isinstance(d, list):
        for entry in d:
            keys.extend(allKeys(entry))
    else:
        for k, v in d.items():
            if k is None or v is None:
                continue
            
            keys.append(k)
            keys.extend(allKeys(v))
                
    return keys

def allValues(d): 
    """ 
    Returns a list of all the primitive values of a dictionary (duplicates included)
    d -- a dictionary to iterate through
    """
    if d is None:
        return []

    if not isinstance(d, dict) and not isinstance(d, list):
        return [d]
    
    values = []
    
    if isinstance(d, list):
        for entry in d:
            values.extend(allValues(entry))
    else:
        for k, v in d.items():
            values.extend(allValues(v))

    return values