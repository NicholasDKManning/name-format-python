# Write a program whose input is:
# firstName middleName lastName
# and whose output is:
# lastName, firstInitial.middleInitial

fullname = input().split()

if len(fullname) == 3:
    
    print(f'{fullname[2]}, {fullname[0][0]}.{fullname[1][0]}.')

else:
    
    print(f'{fullname[1]}, {fullname[0][0]}.')