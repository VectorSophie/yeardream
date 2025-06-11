from validators import validate_email

class User:
    
    def __init__(self, email, password, name, gender):
    
        if not validate_email(email):
            raise ValueError("이메일 재작성 필요")
        self.email = email
        
        if len(password) < 8:
            raise ValueError("비번 재작성 필요")
        self.password = password
    
        if name == "":
            raise ValueError("이름 재작성 필요")
        self.name = name
     
        if gender not in ["M", "F", "O"]:
            raise ValueError("성별 재작성 필요")
        self.gender = gender
        
        self.friends = []

User("test@elice.io", "nevegonnagiveyouup", "Jack", "M")