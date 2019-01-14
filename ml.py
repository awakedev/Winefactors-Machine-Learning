from sklearn import datasets

wine = datasets.load_wine()

features = wine.data
labels = wine.target

print ("Number of entries: " ,len(features), )

for featurename in wine.feature_names:
     print (featurename[:10], "\t", end='')


for feature, label in zip(features,labels):
    for f in feature:
        print (f, "\t",  end=''),
        print (label,  end='')
