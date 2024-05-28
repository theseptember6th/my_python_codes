def simple_coroutine():
    print("Coroutine started")
    text = (yield)  # Execution pauses here #yield is the checkpoint
    print(f"Received: {text}")

# Initialize the coroutine
coroutine = simple_coroutine()

# Start the coroutine
next(coroutine)  # Output: "Coroutine started"

# Send a value to the coroutine
coroutine.send("Hello")  # Output: "Received: Hello"

#coroutine.close() #no need to close the coroutine because we have reached the end of coroutine
