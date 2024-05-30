# What is HTTP?
# HTTP stands for the 'Hypertext Transfer Protocol,'. It is a set of protocols that are designed to enable communication between clients and servers. Between clients and servers, it works as a request-response protocol. To request a response from the server, we can request data from the server or submit data to be processed to the server.

# What Is Requests Module?
# The response data depends on our type of request. The requests module is not a built-in Python module; instead, we have to download it manually. Requests module is used to send all kinds of HTTP requests. It is also one of the most downloaded modules in Python because all the web-related software and programs must have it in them.


import requests
r=requests.get("https://site.financialmodelingprep.com/developer/docs/stock-market-quote-free-api")
print(r.text)
print(r.status_code)

x=requests.head("https://site.financialmodelingprep.com/developer/docs/stock-market-quote-free-api")
print(x.headers)


# url="www.something.com"
# data={
#     "p1":4,
#     "p2":5
# }
# r2=requests.post(url=url,data=data)


#i know only little for now,but i know when i will learn web development backend