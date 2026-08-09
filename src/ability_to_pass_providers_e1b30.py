import sys

def run(*args):
    return 'Hello from Ability To Pass Providers To Modules (built from demand: https://github.com/hashicorp/terraform/issues/24476)'

def cli(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    print(run(*argv)); return 0

if __name__ == '__main__':
    sys.exit(cli())
