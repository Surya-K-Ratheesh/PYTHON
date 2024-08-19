#4. Combine two files

def main():
    f1 = input("Enter a file name: ")
    f2 = input("Enter the second file: ")
    
    f3 = input("Enter the output file name: ")
    
    combine(f1,f2,f3)
    
    
    
def combine(file1_path, file2_path, out_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()
            
        combined_content = content1 + content2
        
        with open(out_path, 'w') as out_file:
            out_file.write(combined_content)
            
    except Exception as e:
        print(f"Exception as {e}")
    
    
if __name__ == "__main__":
    main()
    