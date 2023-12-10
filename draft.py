def minify_html(input_file, output_file):
    with open(input_file, 'r') as file:
        html_content = file.read()

    minified_html = ' '.join(html_content.split())

    with open(output_file, 'w') as file:
        file.write(minified_html)

# Example usage
minify_html('fund-nav.html', 'output.html')
