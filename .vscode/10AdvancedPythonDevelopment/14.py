import re
email = 'jose@tajdkf.com'
expression = '[a-z\.]+'
matches = re.findall(expression,email)
print(matches)