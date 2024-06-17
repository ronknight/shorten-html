<p><a target="_blank" href="https://app.eraser.io/workspace/U2XKelwn1JR80JrbU2vP" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

<h1 align="center"><a href="https://github.com/ronknight/shorten-html">HTML Shortener</a></h1>
<h4 align="center">This Python script uses the BeautifulSoup library to shorten HTML files by removing certain tags or attributes. It reads an HTML file, performs the desired modifications, and writes the shortened HTML content to a new file.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/shorten-html/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/shorten-html/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#usage">Usage</a> •
  <a href="#customization">Customization</a> •
  <a href="#diagrams">Diagrams</a> •
</p>

---

## Usage
1. Make sure you have BeautifulSoup installed. You can install it using pip:
```bash
pip install beautifulsoup4
```
1. Prepare your input HTML file and place it in the same directory as the script.
2. Run the script:
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
#### For demonstration purposes, let's remove all  tags
```html
for span_tag in soup.find_all('span'):
span_tag.unwrap()  # Remove the <span> tags while keeping the content
```



<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-HTML Shortener Process-1.eraserdiagram" data-element-id="IbLzj9TlF_DULNh8i2UB0"><img src="/.eraser/U2XKelwn1JR80JrbU2vP___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----34d3f855ab0e56062ee8643c4dd09a69-HTML-Shortener-Process.png" alt="" data-element-id="IbLzj9TlF_DULNh8i2UB0" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/U2XKelwn1JR80JrbU2vP --->