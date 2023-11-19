quine = [
    'quine = [',
    ']',
    'def print_quine(quine):',
    ' print(quine[0])',
    ' for line in quine:',
    "  print('    ' + repr(line) + ',')",
    ' for line in quine[1:]:',
    '  print(line)',
    'print_quine(quine)',
]
def print_quine(quine):
 print(quine[0])
 for line in quine:
  print('    ' + repr(line) + ',')
 for line in quine[1:]:
  print(line)
print_quine(quine)