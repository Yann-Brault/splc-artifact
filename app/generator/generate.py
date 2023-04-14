import nbformat as nbf

NOTEBOOKS_DIR_PATH = './static/Notebooks'


def generate_nb(name: str):
    nb = nbf.v4.new_notebook()
    text = """\
    # My first automatic Jupyter Notebook
    This is an auto-generated notebook."""

    code = """print('hello world')"""

    nb['cells'] = [nbf.v4.new_markdown_cell(text),
                   nbf.v4.new_code_cell(code)]
    fname = f'{name}.ipynb'
    path = f'{NOTEBOOKS_DIR_PATH}/{fname}'

    with open(fname, 'w') as f:
        nbf.write(nb, path)
