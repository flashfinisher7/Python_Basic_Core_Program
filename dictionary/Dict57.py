student = [{'id': 1, 'success': True, 'name': 'Anil'},
 {'id': 2, 'success': False, 'name': 'Kumar'},
 {'id': 3, 'success': True, 'name': 'Hello'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))