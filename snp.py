import argparse

# Find and replace function
def find_and_replace(file_path, search_text, replace_text, output_file):
    with open(file_path, "r") as file:
        content = file.read() # Initialize content

    for search, replace in zip(search_text, replace_text):
        print(f">>> replacing {search} with {replace}")
        content = content.replace(search, replace) # Update content.

    with open(output_file, "w") as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(
        prog='searchNreplace',
        description='Search and replace text',
        epilog='Simple script for searching and replacing text'
    )
    parser.add_argument('-f', '--file', type=str, required=True, help='The file path to be parsed.')
    parser.add_argument('-s', '--search', type=str, required=True, nargs='+', help='The word to be searched.')
    parser.add_argument('-r', '--replace', type=str, required=True, nargs='+', help='The word to be used as replacement.')
    parser.add_argument('-o', '--output', type=str, required=True, help='The output file to be used.')

    args = parser.parse_args()

    if len(args.search) != len(args.replace):
        parser.error("The number of search operators need to match the number of replacement operators.")

    find_and_replace(args.file, args.search, args.replace, args.output)

if __name__ == "__main__":
    main()
