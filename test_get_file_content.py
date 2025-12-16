from functions.get_file_contents import get_file_content
from config import MAX_CHARS

def main():
    contents = get_file_content("calculator", "lorem.txt")
    print(f"file lorem.txt:")
    print(f"length: {len(contents)}")
    if len(contents) > MAX_CHARS:
        print(f"Ends with: {contents[-51:]}")
        if contents.endswith(f'[...File "lorem.txt" truncated at 10000 characters]'):
            print(f"passed")
        else:
            print(f"failed")
    
    contents = get_file_content("calculator", "main.py")
    print(f"file main.py:")
    print(f"length: {len(contents)}")
    print(f"output: {contents}")

    contents = get_file_content("calculator", "pkg/calculator.py")
    print(f"file main.py:")
    print(f"length: {len(contents)}")
    print(f"output: {contents}")

    contents = get_file_content("calculator", "/bin/cat")
    print(f"file main.py:")
    print(f"length: {len(contents)}")
    print(f"output: {contents}")

    contents = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"file main.py:")
    print(f"length: {len(contents)}")
    print(f"output: {contents}")


if __name__ == "__main__":
    main()