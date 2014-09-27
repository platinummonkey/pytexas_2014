
def groupCountToObjValueMap(gc):
    result = {}
    for v in gc.values():
        result[v['_key']] = v['_value']
    return result