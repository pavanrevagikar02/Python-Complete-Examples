#/s - space character

import re
matches=re.finditer('\s','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())

#/S - except space character

import re
matches=re.finditer('\S','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())

#/d- only digits

import re
matches=re.finditer('\d','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())

#/D- except digits

import re
matches=re.finditer('\D','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())

#/w- alpha numeric

import re
matches=re.finditer('\w','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())

#/W- except alpha numeric

import re
matches=re.finditer('\W','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())

#. - Everything will be printed

import re
matches=re.finditer('.','A8b @9hz* K')
for m in matches:
    print(m.start(),'....',m.group())