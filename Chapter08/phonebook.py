
class phonebook:
    """
    A phonebook has the following characteristics:
      - A dictionary of contacts, where each contact has a name and a phone number
    
    Phonebook Interface:
      - reset: Signature:  -> None
               Purpose: Reset the phonebook
               Effect: The dictionary is made empty
      - addContact: Signature: str natnum -> None
                    Purpose: Add a contact with the given name and phone number
                    Effect: Adds a contact to the phonebook
      - getContact: Signature: str -> natnum
                    Purpose: Retrieve the phone number of a contact by name
    """
    contacts = None

    def __init__(self):
        self.contacts = {}

    def reset(self):
        self.contacts = {}

    def addContact(self, name, phone_number):
        self.contacts[name] = phone_number

    def getNumber(self, name) -> int:
        return self.contacts.get(name, None)

def test_phonebook():
    pb = phonebook()

    assert pb.getNumber("Lidia") is None, "Test 0 failed"
    assert pb.getNumber("Luis") is None, "Test 1 failed"
    assert pb.getNumber("Walter") is None, "Test 2 failed"

    pb.addContact("Lidia", 1234567890)
    pb.addContact("Luis", 9876543210)

    assert pb.getNumber("Luis") == 9876543210, "Test 3 failed"
    assert pb.getNumber("Lidia") == 1234567890, "Test 4 failed"
    assert pb.getNumber("Walter") is None, "Test 5 failed"

    pb.reset()

    assert pb.getNumber("Lidia") is None, "Test 6 failed"
    assert pb.getNumber("Luis") is None, "Test 7 failed"
    assert pb.getNumber("Walter") is None, "Test 8 failed"

test_phonebook()

