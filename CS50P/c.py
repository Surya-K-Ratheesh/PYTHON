def main():
    x = input("Enter a no.: ")
    print(f"{x} squared is", square(x))
    
def square(x):
    #return x + x
    return x * x

if __name__ == "__main__":
    main()