lib = {

}

books = {
    "romeo and juliet" : {"author":"William Shakespeare", "status":"available"},
    "abc" : {"author":"ravi", "status":"available"},
    "xyz" : {"author":"Ayush", "status":"Not available"}
}

def register(name, email, password):
    if not email.endswith("@gmail.com"):
        return "Invalid email"
    
    if not len(password) >= 8:
            return "Password must be 8 characters long"
    
    if email in lib:
        return "Email already exists"
    
    lib[email] = {"name":name, "password":password, "reserved" : []}
    return "Registeration successfull"


def login(email, password):
    if not email in lib:
        return "Invalid email"
    if lib[email]["password"] == password:
        return f"Welcome back {lib[email]["name"]}"
    return "Invalid password"


def search_book(title, email):
    title = title.lower()
    if not email in lib:
        return "Email not registered"
    if title in books:
        if books[title]["status"] == "available":
            return "Book found"
        else: 
            return "Book not available"
    else:
        return "Book not found"


def reserve_book(title, email):
    title = title.lower()
    if not email in lib:
        return "Email not registered"
    if title in books and books[title]["status"] == "available":
            lib[email]["reserved"].append(title)
            return f"{title} book reserved by {lib[email]["name"]}"
    return "Book not found"


def view_reserve(email):
    if not email in lib:
        return "Invalid email"
    l = lib[email]["reserved"]
    if len(l) == 0:
        return "No book is reserved"
    else:
        return f"Books reserved by {lib[email]["name"]} : {lib[email]["reserved"]}"
     
     


print(register("gayathri", "gayathri@gmail.com", "12345678"))

print(login("gayathri@gmail.com", "12345678"))

print(login("gayathri@gmail.com", "12345"))

print(search_book("Romeo and juliet", "gayathri@gmail.com"))

print(search_book("XYZ", "gayathri@gmail.com"))

print(view_reserve('gayathri@gmail.com'))

print(reserve_book("Romeo and juliet", "gayathri@gmail.com"))

print(view_reserve('gayathri@gmail.com'))