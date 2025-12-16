from functions.get_files_info import get_files_info

def main():
    contents = get_files_info("calculator", ".")
    print(f"result for current directory:")
    print(f"{contents}")

    contents = get_files_info("calculator", "pkg")
    print(f"result for 'pkg' directory:")
    print(f"{contents}")
    
    contents = get_files_info("calculator", "/bin")
    print(f"results for '/bin' directory:")
    print(f"{contents}")

    contents = get_files_info("calculator", "../")
    print(f"results for '../' directory:")
    print(f"{contents}")

if __name__ == "__main__":
    main()
    