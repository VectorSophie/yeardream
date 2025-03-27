def validate_email(email):

    if type(email) is not str:
        return False

    if email.count("@")!=1:
        return False

    domain = email.split("@")[1]

    if domain.count(".")<1:
        return False

    parts = domain.split(".")
    for part in parts:
        if part == "":
            return False
    
    return True