cc=input(' enter a password : ')

''' creat a function tomaskify the number or word'''
def maskify(cc):
    new_string = ''
    if len(cc) > 4:
        new_string += '#' * (len(cc) - 4) + cc[-4:]
    else:
        return cc
    return new_string

print(maskify(cc))