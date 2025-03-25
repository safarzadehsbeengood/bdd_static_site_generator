import os
import shutil
from markdown import *
from gencontent import *
from utils import *
import sys

static_path = "./static"
public_path = "./docs"
template_file = "./template.html"
content_path = "./content"

def main():
    basepath = '/'
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]

    print("deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print('copying static files to public directory...')
    copy_files(static_path, public_path)

    print("generating pages...")
    generate_pages_recursive(content_path, template_file, public_path, basepath)

main()
