def producto(text):
    if text in '=\'\"[]^,{}+-':
        return False
    else:
        return True
    
def precio(text):
    try:
        float(text)
        return True
    except Exception as ex:
        return False
    
def entero(text):
    try:
        int(text)
        return True
    except Exception as ex:
        return False