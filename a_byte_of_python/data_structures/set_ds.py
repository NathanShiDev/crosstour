bri = set(['brazil', 'russia', 'india'])

if 'india' in bri:
    print('india exists in bri')
else:
    print('india does not exist in bri')

if 'usa' in bri:
    print('usa exists in bri')
else:
    print('usa does not exist in bri')

bric = bri.copy()
bric.add('china')
print('issuperset:', bric.issuperset(bri))
bri.remove('russia')
print('bri and bric:', bri & bric)
