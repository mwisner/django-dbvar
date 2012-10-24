from models import Variable


def variable_set(key, value):
    '''
    this looks pretty worthless.
    '''
    return Variable.set(key, value)


def variable_get(key, default):
    '''
    this looks pretty worthless.
    '''
    return Variable.get(key, default)


def variable_set_with_scope(scope, pk, key, value):
    '''
    cheating because I suck
    '''
    return variable_set(scope+"_"+pk+"_"+key, value)

def variable_get_with_scope(scope, pk, key, default):
    '''
    cheating because I still suck.
    '''
    return variable_get(scope+"_"+pk+"_"+key, default)
