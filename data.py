import pandas as pd

def findText(str):
  if str is None:
    return ''
  d = ''.join(x for x in str if x.isdigit())
  if d == '':
    if str.find('yes') != -1:
      d = 'yes'
    elif str.find('no') != -1:
      d = 'no'
  return d

df_json = pd.read_json("providerjason.json")
df_json['wheelChairImg'] = df_json['wheelChairImg'].map(findText)
df_json['dirqImg'] = df_json['dirqImg'].map(findText)
df_json.to_excel("providerdata.xlsx")
