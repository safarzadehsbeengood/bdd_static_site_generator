import os
import shutil
from markdown import *
from gencontent import *
from utils import *

static_path = "./static"
public_path = "./public"
template_file = "./template.html"
content_path = "./content"

def main():
    print("deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    print('copying static files to public directory...')
    copy_files(static_path, public_path)
    generate_pages_recursive(content_path, template_file, public_path)

main()
