point1 = (12, 13)
(point := (13, 14))

print(point)
print(point1)

resp1 = {"data": "Data being received!"}
resp2 = {"data": None}
resp3 = {"Error": "Error 222!"}
response = resp3


match response:
    case {"Error": msg}:
        print(f"Error {msg}")
    case {"data": data} if data is not None:
        print(f"Data is received! {data}")
    case _:
        print("Other")


match response:
    case {"Error": msg}:
        print(f"Error {msg}")
    case {"data": data} if data is not None:
        print(f"Data is received! {data}")
    case _:
        print("Other")

