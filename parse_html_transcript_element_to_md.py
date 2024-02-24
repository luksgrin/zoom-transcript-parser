import argparse
from src.html_to_md import HTML_to_md
from bs4 import BeautifulSoup

def parser():

    parser = argparse.ArgumentParser(
        prog="Parse HTML Zoom Transcript Element to Markdown",
        description="Turns a file containing the HTML outer element into a formatted Markdown"
    )

    parser.add_argument(
        "input_file",
        type=str,
        help="Intput HTML file path"
    )

    return parser.parse_args()

def main():

    args = parser()

    with open(args.input_file) as file:
        print(
            HTML_to_md.get_audio_transript(
                file.read()
            )
        )
    
if __name__ == "__main__":
    main()