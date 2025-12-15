#Pickling (Save object to file)
import pickle

data={
    'name':'elango',
    'age':20,
    'city':'bangalore' 
}
with open('data.pkl','wb') as f: 
    pickle.dump(data,f)

print('Data saved successfully')    