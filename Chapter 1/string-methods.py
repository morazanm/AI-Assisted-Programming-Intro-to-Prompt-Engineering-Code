def count_as(str):
    return str.casefold().count("a")

def test_count_as():
    empty = ""
    name = "AI-Assisted Program Design"
    cheer = "Here's to you, cheers!"
    justA = "AAAAAA AAA AA AAAA"
    justa = "a aaaaa aa"
    assert count_as(empty) == 0, "count_as: Test 0 failed"
    assert count_as(name) == 3, "count_as: Test 1 failed"
    assert count_as(cheer) == 0, "count_as: Test 2 failed"
    assert count_as(justA) == 15, "count_as: Test 3 failed"
    assert count_as(justa) == 8, "count_as: Test 4 failed"

test_count_as()


