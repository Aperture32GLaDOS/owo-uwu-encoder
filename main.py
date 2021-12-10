def bytesToOwo(data: bytes) -> str:
    binaryData = int().from_bytes(data, "big")  # Turn the data into an integer
    binaryData = bin(binaryData)[2:]  # Convert said integer into a binary string (i.e. 00110101...)
    owoString = " ".join(list(binaryData))
    owoString = owoString.replace("0", "owo").replace("1", "uwu")  # Owo the binary string
    return owoString

def owoToBytes(owoString: str) -> bytes:
    binaryData = owoString.replace(" ", "").replace("uwu", "1").replace("owo", "0")  # Un-owo the binary string
    length = (len(binaryData) // 8) + 1  # Calculate the length of the resultant bytes object
    binaryData = int(binaryData, 2)  # Calculate the integer from the owos
    return binaryData.to_bytes(length, "big")  # Convert the integer into the original data
