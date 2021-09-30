student = {
  'name': 'Anil',
  'class': '7',
  'roll_id': '104'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Anil'})
print(student.keys() >= {'roll_id', 'name'})
