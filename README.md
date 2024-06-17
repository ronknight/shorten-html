# HTML Shortener

This Python script uses the BeautifulSoup library to shorten HTML files by removing certain tags or attributes. It reads an HTML file, performs the desired modifications, and writes the shortened HTML content to a new file.

## Usage

1. Make sure you have BeautifulSoup installed. You can install it using pip:

```bash
pip install beautifulsoup4
```

2. Prepare your input HTML file and place it in the same directory as the script.

3. Run the script:

```python
python shorten.py
```

The script will read the `input.html` file, remove all `<span>` tags (for demonstration purposes), and write the modified HTML content to `output.html`.

## Customization

To modify the HTML shortening logic, open the `shorten.py` file and edit the following section:

```python
python shorten.py
```

# Shorten the HTML
#### For example, remove certain tags or attributes
#### For demonstration purposes, let's remove all <span> tags
```html
for span_tag in soup.find_all('span'):
    span_tag.unwrap()  # Remove the <span> tags while keeping the content
```