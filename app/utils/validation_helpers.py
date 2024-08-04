def represents_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
