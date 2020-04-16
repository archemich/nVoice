from getToken import getIAMToken

OATH_TOKEN = "AgAAAAAsX9JLAATuwQCGu0TMUU2kl2oyjf2vlD4"
FOLDER_ID = "b1g888iudohmdqgobtgp"

iam = getIAMToken(OATH_TOKEN)
print(iam)
