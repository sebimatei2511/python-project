# Project type C
# Realizați un script care să imite funcționalitatea utilitarului “rm” din Linux.
# INPUT: rm -rf --interactive ../*.*
# OUTPUT:

import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--force", action="store_true", help="force deletion")
parser.add_argument("-r", "--recursive", action="store_true", help="recursive deletion")
parser.add_argument("-i", "--verbose", action="store_true", help="interactive deletion")
parser.add_argument("path", help="file or directory to delete")
args = parser.parse_args()

# Daca path-ul dat ca input nu exista, afisam o eroare si oprim 
if not os.path.exists(args.path):
    print(f"ERROR rm: cannot remove '{args.path}': No such file or directory.")
    exit(1)

# Se afiseaza confirmarea daca optiunea --force nu a fost adaugata
if not args.force:
    if os.path.isdir(args.path):
        confirm = input(f"rm: remove folder and its subitems '{args.path}'? ")
    if os.path.isfile(args.path):
        confirm = input(f"rm: remove file '{args.path}'? ")
    if confirm != "y":
        print("rm: aborting")
        exit(0)

# Stergem fisierul sau folderul dat ca argument
if args.recursive:
    if args.verbose:
        print(f"rm -ri {args.path}")
    shutil.rmtree(args.path)
else:
    if args.verbose:
        print(f"rm {args.path}")
    os.remove(args.path)
