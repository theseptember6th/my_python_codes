def printk(string):
    return f"this is the string you passed= {string} you passed"

def add(a, b):
    return a + b

print("the function is getting executed by",__name__)

if __name__ == '__main__':
    print(printk("kristal"))
    print(add(2, 3))
