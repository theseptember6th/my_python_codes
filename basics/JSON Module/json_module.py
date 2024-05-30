import json
data='{"var1":"kristal","var2":"shrestha"}'
#here data is a string
parsed=json.loads(data)
#parsed is now a dictionary
print(parsed)
print(type(parsed))
print(parsed["var1"])

data2={
    "name":"kristal shrestha",
    "cars":["bmw","ferrari","honda"],
    "foods":("momo","choewmein","Noddles"),
    "isbad":False
}
jscomp=json.dumps(data2)
print(jscomp)