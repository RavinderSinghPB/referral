from django.contrib.auth import authenticate
from app.models import ReferCode

from app.forms import SignUpForm as sf

# data = {
#     'username': 'zaa2bsv5fl',
#     'email': 'ravindersi@gmail.com',
#     'password1': 'abcd1234',
#     'password2': 'abcd1234',
#     'referCode': 'abcde',
#
# }
#
# print(sf)
# f = sf(data)
# print(f.is_valid())
# print(f.errors)
# print(f.cleaned_data)
# username = f.cleaned_data.get('username')
# password1 = f.cleaned_data.get('password1')
# code = f.cleaned_data.get('referCode')
# print(code)
# # referrer_codeObj = ReferCode.objects.get(code=code)
#
# # f.used_refer_code = referrer_codeObj
# # f.used_refer_code = code
# f.save()
# user = authenticate(username=username, password=password1)
#
# # user.used_refer_code = referrer_codeObj
# user.used_refer_code = code
# user.save()
# print(user)

f = sf()

for e in f:
    print(e)
