# import re
# s=re.finditer('a','abaabaaab')
# for m in s:
#     print(m.start(),'.....',m.group())
#
# import re
# s=re.finditer('a+','abaabaaab')
# for m in s:
#     print(m.start(),'.....',m.group())
#
# import re
# s=re.finditer('a*','abaabaaab')
# for m in s:
#     print(m.start(),'.....',m.group())
#
# import re
# matcher=re.finditer('a{3}','abaabaaab')
# for m in matcher:
#     print(m.start(),'.....',m.group())

import re
matcher=re.finditer('a{1,3}','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())


# import re
# matcher=re.finditer('a$','abaabaaaba')
# for m in matcher:
#     print(m.start(),'.....',m.group())
