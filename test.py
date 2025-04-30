from Library import register, reserve_book, search_book, login, view_reserve, lib, books

def test_cases():
    books.clear()
    lib.clear()
    res1 = register("gayathri", "gayathri@gmail.com", "12345678")
    assert res1 == "Registeration successfull"

    res2 = login("gayathri@gmail.com", "12345678")
    assert res2 == "Welcome back gayathri"

    res3 = login("gayathri@gmail.com", "12345")
    assert res3 == "Invalid password"

    res4 = search_book("Romeo and juliet", "gayathri@gmail.com")
    assert res4 == "Book found"

    res5 = search_book("XYZ", "gayathri@gmail.com")
    assert res5 == "Book not available"

    res6 = view_reserve('gayathri@gmail.com')
    assert res6 == "No book is reserved"

    res7 = reserve_book("Romeo and juliet", "gayathri@gmail.com")
    assert res7 == "romeo and juliet book reserved by gayathri"

    res8 = view_reserve('gayathri@gmail.com')
    assert res8 == "Books reserved by gayathri : ['romeo and juliet']"


test_cases()