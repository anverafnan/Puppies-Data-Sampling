import numpy as np

np.random.seed(42)
puppies=np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p=puppies.mean()
print("Mean:",p)
print("standard deviation",puppies.std())
print("variance",puppies.var())

np.random.choice(puppies,size=(1,5),replace=True)
np.random.choice(puppies,size=(1,5),replace=True).mean()

print("\nsampling Distribution with size 5 \n")
sample_props=[]
for i in range(10000):
    sample=np.random.choice(puppies,5,replace=True)
    sample_props.append(sample.mean())
sample_props=np.array(sample_props)

twenty_sample_props=[]
for i in range(10000):
 sample=np.random.choice(puppies,20,replace=True)
 twenty_sample_props.append(sample.mean())
twenty_sample_props=np.array(twenty_sample_props)

print("new Mean",twenty_sample_props.mean())
print("new standard Deviaton",twenty_sample_props.std())
print("new variance",twenty_sample_props.var())