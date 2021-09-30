my_dict = {'C1':[1,4,7],'C2':[2,5,8],'C3':[3,6,9]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)