calls = 0

def count_calls():
  global calls
  calls += 1

def string_info(string):
  count_calls()
  print(f"({len(string)}, '{string}', '{string.lower()}'")

def is_contains(string, list_to_search):
  count_calls()
  string = string.lower()
  for word in list_to_search:
    if string == word.lower():
      print(f"True")
      return True
  print(f"False")
  return False

string_info('CAPYBARA')
string_info('ARMAGEDDON')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)