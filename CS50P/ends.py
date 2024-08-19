#Enter file name with extension
file = input("Enter File name: ").strip().lower()


#Determining the file media type by its extension
if file.endswith("jpg") or file.endswith("jpeg"):
    print("image/jpeg")

elif file.endswith("gif"):
    print("image/gif")

elif file.endswith("png"):
    print("image/png")

elif file.endswith("pdf"):
    print("application/pdf")

elif file.endswith("txt"):
    print("text/plain")

elif file.endswith("zip"):
    print("application/zip")

else:
    print("application/octet-stream")