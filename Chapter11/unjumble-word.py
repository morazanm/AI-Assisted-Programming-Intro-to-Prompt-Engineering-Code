
import nltk
from nltk.corpus import words

"""
A one-string is a string of length 1 in [a-zA-Z]

A word is either:
  1. [one-string]
  2. [one-string, word]

Template for a function on a word:
  def f_on_word(word ...):
      <prompt}
      if word == []:
          return base_case
      else:
          return combine(f(word[1:]), word[0])
  def test_f_on_word():
      <prompt>
      assert f_on_word(<one-string> ...) == base_case, "Test 0 failed"
      assert f_on_word(<word> ...) == ..., "Test 1 failed"
      assert f_on_word(<word> ...) == ..., "Test 2 failed"

A list of words, low, is either:
  1. []
  2. [word, low]

Template for a function on a low:
  def f_on_low(low ...):
      <prompt>
      if low == []:
          return base_case
      else:
          return combine(f_on_word(low[0]), f_on_low(low[1:]))
  def test_f_on_low():
      <prompt>
      assert f_on_low([]) == base_case, "Test 0 failed"
      assert f_on_low([<low>]) == ..., "Test 1 failed"
      assert f_on_low([<low>]) == ..., "Test 2 failed"
"""

def insertEverywhereInWord(a, wrd):
    """
    Signature: one-string word -> low
    Purpose: Insert a in every position of wrd
    Design Idea:
      Call function make_words("", wrd) to make the words
      Use the template for a function on a word to define make_words
        Header: make_words(prefix, suffix)
        Accumulate a prefix for a as wrd is traversed
        Accumulator Invariant: wrd = prefix + suffix
        If suffix is empty, return the list containing prefix + a
        otherwise, return the list containing prefix + a + suffix and
          the result of recursively processing prefix+suffix[0] and suffix[1:]
    """
    def make_words(prefix, suffix):
        if suffix == "":
            return [prefix + a]
        else:
            first_letter = suffix[0]
            rest_of_suffix = suffix[1:]
            return [prefix + a + suffix] + make_words(prefix + first_letter, rest_of_suffix)
    return make_words("", wrd)

def test_insertEverywhereInWord():
    """
    Signature:  -> None
    Purpose: Test the insertEverywhereInWord function
    Design Idea:
      Use the template for a function on a word
      Insert different letters in words of lengths 0-3
    """
    assert insertEverywhereInWord('a', '') == ['a'], "Test 0 failed"
    assert insertEverywhereInWord('a', 'b') == ['ab', 'ba'], "Test 1 failed"
    assert insertEverywhereInWord('a', 'bc') == ['abc', 'bac', 'bca'], "Test 2 failed"
    assert insertEverywhereInWord('x', 'y') == ['xy', 'yx'], "Test 3 failed"
    assert insertEverywhereInWord('a', 'bcd') == ['abcd', 'bacd', 'bcad', 'bcda'], "Test 4 failed"

test_insertEverywhereInWord()

def insertEverywhereInEveryWord(letter, words):
    """
    Signature: one-string, low -> low
    Purpose: Insert the one-string in every position of every word in the low
    Design Idea: 
      Use the template for a function on a low
      if words == [], return the empty list
      otherwise insert letter in every position of words[0] and add to the result of recursively processing the rest of the words
      Use insertEverywhereInWord(letter, words[0]) to insert the letter in every position of the first word
      Do not locally define insertEverywhereInWord
    """
    if words == []:
        return []
    else:
        first_word = words[0]
        rest_words = words[1:]
        return insertEverywhereInWord(letter, first_word) + insertEverywhereInEveryWord(letter, rest_words)
    
def test_insertEverywhereInEveryWord():
    """
    Signature:  -> None
    Purpose: Test the insertEverywhereInEveryWord function
    Design Idea: 
      Use the template for a function on a low
      Test the base case with an empty low
      Test the case with a single word
      Test the case with multiple words
    """
    assert insertEverywhereInEveryWord('a', []) == [], "Test 0 failed"
    assert insertEverywhereInEveryWord('a', ['b']) == ['ab', 'ba'], "Test 1 failed"
    assert insertEverywhereInEveryWord('a', ['bc']) == ['abc', 'bac', 'bca'], "Test 2 failed"
    assert insertEverywhereInEveryWord('x', ['y']) == ['xy', 'yx'], "Test 3 failed"
    assert insertEverywhereInEveryWord('a', ['b', 'c']) == ['ab', 'ba', 'ac', 'ca'], "Test 4 failed"
    
test_insertEverywhereInEveryWord()

def perms(word):
    """
    Signature: word -> low
    Purpose: Return the permutations of the given word
    Design Idea: 
      Structure the code using the template for a function on a word
      if the word=="", return the list containing the empty word
      else insert the first letter in every position of every word in the permutations of the rest of the word
      Use insertEverywhereInEveryWord(word[0], perms(word[1:])) to insert the first letter in every position of every word in the permutations of the rest of the word
      Do not locally define insertEverywhereInEveryWord
    """
    if word == "":
        return [""]
    else:
        first_letter = word[0]
        rest_of_word = word[1:]
        return insertEverywhereInEveryWord(first_letter, perms(rest_of_word))
    
def test_perms():
    """
    Signature: ()
    Purpose: Test the perms function
    Design Idea: 
      Use the template for a function on a word
      Test the base case with an empty word
      Test the case with a single letter word
      Test the case with a two-letter word
      Test the case with a three-letter word
    """
    assert perms("") == [""], "Test 0 failed"
    assert perms("a") == ["a"], "Test 1 failed"
    assert perms("ab") == ["ab", "ba"], "Test 2 failed"
    assert perms("abc") == ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'], "Test 3 failed"

test_perms()

def is_english_word(s):
    """
    Signature: string -> Boolean
    Purpose: Determine if the given string is an English word
    Design Idea:
      Convert s to lowercase
      Convert nltk's list of English words to a set to perform efficient searches
      Determine if the converted s in in the set
    """
    return s.lower() in set(words.words())

def test_is_english_word():
    """
    Signature:  -> Boolean
    Purpose: Test is_english_word
    Design Idea:
      Tests strings representing English words
      Tests strings not representing English words
    """
    assert is_english_word('atc') == False, "Test 0 failed"
    assert is_english_word('tgilep') == False, "Test 1 failed"
    assert is_english_word('cleesip') == False, "Test 2 failed"
    assert is_english_word('cat') == True, "Test 3 failed"
    assert is_english_word('act') == True, "Test 3 failed"
    assert is_english_word('piglet') == True, "Test 3 failed"
    assert is_english_word('eclipse') == True, "Test 3 failed"

test_is_english_word()


def unjumble(jword):
    """
    Signature:  word -> low
    Purpose:  Return English words in the permutations of given word
    Design Idea:
      Use the data definition for a word to structure this function
      Convert jword to lowercase
      Evaluate (perms jword) to generate permutations of jword 
      Filter the strings to include only valid English words using is_english_word
      return the valid words
    """
    jword = jword.lower()
    permsList = perms(jword)
    return [w for w in permsList if is_english_word(w)]

def test_unjumble():
    """
    Signature:  -> None
    Purpose: Test the unjumble function
    Design Idea:
      Use the template for a function on a low
      Use the following test jumbled words:
        - atc should return [act,'cat']
        - rea should return ['ear', 'are', 'era']
        - ptnu should return ['punt']
        - tgilep should return ['piglet']
    """
    assert unjumble('atc') == ['act', 'cat'], "Test 0 failed"
    assert unjumble('rea') == ['rea', 'era', 'ear', 'are', 'aer'], "Test 1 failed"
    assert unjumble('ptnu') == ['punt'], "Test 2 failed"
    assert unjumble('tgilep') == ['piglet'], "Test 3 failed"

test_unjumble()    


