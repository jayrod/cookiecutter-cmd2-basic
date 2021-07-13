""" Entry point of cmd2 application """
from {{cookiecutter.project_slug}}.app import App
from {{cookiecutter.project_slug}} import commands 

def main():

    c = App()
    c.cmdloop()
