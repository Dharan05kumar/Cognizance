import pandas as pd

dk = pd.read_csv("dataset.csv")
print("\nMissing values in the given csv file are: ")
print(dk.isnull().sum())

print("\nMissing values in LotFrontage: \n")
print(dk['LotFrontage'].isnull())
print("\nupdated LotFrontage values(changed '-99' values for the LotFrontage instead of NA): \n")
dk['LotFrontage'].fillna('-99',inplace = True)
print(dk['LotFrontage'])

print("\nMissing values in Alley: \n")
print(dk['Alley'].isnull())
print("\nupdated Alley values(changed 'empty' values for the Alley instead of NA): \n")
dk['Alley'].fillna('empty',inplace = True)
print(dk['Alley'])

print("\n",dk[dk['BsmtQual'].isnull()])

print("\nupdated BsmtQual values(changed 'empty1' values for the BsmtQual instead of NA): \n")
dk['BsmtQual'].fillna('empty1',inplace = True)
print(dk[dk['BsmtQual'].isnull()])

print("\n",dk[dk['BsmtQual'].isnull()])

print("\nupdated BsmtCond values(changed 'empty2' values for the BsmtCond instead of NA): \n")
dk['BsmtCond'].fillna('empty2',inplace = True)
print(dk[dk['BsmtCond'].isnull()])

print("\n",dk[dk['BsmtExposure'].isnull()])

print("\nupdated BsmtExposure values(changed 'empty3' values for the BsmtExposure instead of NA): \n")
dk['BsmtExposure'].fillna('empty3',inplace = True)
print(dk[dk['BsmtExposure'].isnull()])

print("\n",dk[dk['BsmtFinType1'].isnull()])

print("\nupdated BsmtFinType1 values(changed 'empty4' values for the BsmtFinType1 instead of NA): \n")
dk['BsmtFinType1'].fillna('empty4',inplace = True)
print(dk[dk['BsmtFinType1'].isnull()])

print("\n",dk[dk['BsmtFinType2'].isnull()])

print("\nupdated BsmtFinType2 values(changed 'empty5' values for the BsmtFinType2 instead of NA): \n")
dk['BsmtFinType2'].fillna('empty5',inplace = True)
print(dk[dk['BsmtFinType2'].isnull()])

print("\n\nUpdated final csv file: \n")
print(dk.isnull().sum())
