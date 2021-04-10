import pandas as pd
df = pd.DataFrame(				#dataFrames
			{"a" : [1,2,3],
			 "b" : [7,8,9],
			 "c" : [10,11,12],
			 "d" : [11,21,12]},
			 index=[1,2,3])
print(df)



data=pd.read_csv('file.csv')
print(data.to_string()) 


print(pd.__version__)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
	}
myvar = pd.DataFrame(mydataset)
print(myvar)

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])
print(myvar[2])

myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

print(myvar["y"])
print(myvar["x"])
print(myvar["z"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print(myvar[1])

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
d1 = pd.DataFrame(data)

print(d1) 
