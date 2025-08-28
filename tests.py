from functions.get_files_info import get_files_info

def main():
    test_1 = get_files_info("calculator", ".")
    test_2 = get_files_info("calculator", "pkg")
    test_3 = get_files_info("calculator", "/bin")
    test_4 = get_files_info("calculator", "../")
    print(f"TEST_1\n{test_1}")
    print(f"TEST_2\n{test_2}")
    print(f"TEST_3\n{test_3}")
    print(f"TEST_4\n{test_4}")

if __name__ == '__main__':
    main()