# Standard imports
import argparse # For parsing script arguments
from base64 import b64encode # For converting file to Base64 string
from pathlib import Path # Checks if file exists

# Third Party Imports
import pyperclip # For copying to clipboard

# Classes
class EncodeFile:

    def __init__(self):
        self.file_path = self.parse_args()

    def encode(self):
        """
            Tries reading in the file pointed to by the given file path; if
            successful, the script will then encode the file as a base64 string.
            The result is then copied to the clipboard.
            If unsuccessful, an error is raised indicating as such.

            Returns: None (result copied to clipboard), else Exception
        """
        # First check if file exists
        file_path = Path(self.file_path)
        try:
            file_check = file_path.is_file()
            if not file_check:
                raise Exception
        except Exception:
            error_message = (
                f"Given file path '{file_path}' either does not exist or the "
                "file path instead points to a directory"
            )
            raise FileNotFoundError(error_message)

        # We then attempt to encode it into a base64 format
        with file_path.open('rb') as opened_file:
            plain_string = opened_file.read() # Read file
            encoded_string = b64encode(plain_string) # Encode to base64 bytes
            decoded_string = encoded_string.decode('utf-8') # Decode to string
            pyperclip.copy(decoded_string) # Copy to clipboard

    def parse_args(self):
        """
            Parses arguments passed to the script to determine the file path to
            use.

            Returns: String representing file path
        """
        description = (
            "This script takes in a file path, after which the script then "
            "attempts to encode the file as a base64 string. The string is "
            "then copied to the clipboard."
        )
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            'file_path',
            type=str,
            help='Path to file to encode'
        )
        args = parser.parse_args() # Grabs script arguments

        return args.file_path

# Running main function
if __name__ == "__main__":
    try:
        file_encoder = EncodeFile()
        file_encoder.encode()
        print("Base64 string of provided file has been copied to clipboard")
    except Exception as error:
        error_message = f'Could not encode file. Error received was: {error}'
        print(f'Error! {error_message}\nExiting script...')