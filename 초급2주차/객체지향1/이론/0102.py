import string

def validate_name(name):
    # name이 문자열인지 확인합니다.
    if type(name) is str:
        pass
    
    # name이 숫자를 포함하는지 확인합니다.
    if any(i in string.digits for i in name):
        return False
    
    # name이 특수기호를 포함하는지 확인합니다.
    if any(i in string.punctuation for i in name):
        return False
    
    return True