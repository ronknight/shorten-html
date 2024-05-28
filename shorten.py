from bs4 import BeautifulSoup

def shorten_html(input_file, output_file):
    with open(input_file, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    # Shorten the HTML
    # For example, remove certain tags or attributes
    # For demonstration purposes, let's remove all <span> tags
    for span_tag in soup.find_all('span'):
        span_tag.unwrap()  # Remove the <span> tags while keeping the content

    with open(output_file, 'w') as f:
        f.write(str(soup))

if __name__ == "__main__":
    input_file = "input.html"
    output_file = "output.html"
    shorten_html(input_file, output_file)
    print("HTML shortened successfully. Output written to output.html.")
