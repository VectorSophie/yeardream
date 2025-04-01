def min_validator(minimum):
    def helper(n):
        if type(n) is not int:
            return False
        
        if n < minimum:
            return False
        return True
    
    return helper

def max_validator(maximum):
    def helper(n):
        if type(n) is not int:
            return False
        
        if n > maximum:
            return False
        return True
    
    return helper


def validate(n, validators):
    for validator in validators:
        if not validator(n):
            return False
    
    return True