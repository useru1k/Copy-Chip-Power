import os
import argparse
import tkinter as tk

# ----------- Copy the Text from the File ------------
def copy_from_line(file_path,line):
    with open(file_path,'r') as f:
        lines = f.readlines()
    text = lines[line -1]
    copy_to_chip(text)
    print("[+] Copied to Chipboard [+]")

def copy_from_range(file_path,start,end):
    with open(file_path,'r') as f:
        lines = f.readlines()
    text = ""
    for i in range(start,end+1):
        text += lines[i-1]
    copy_to_chip(text)
    print("[+] Copied to Chipboard [+]")

def copy_full(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    text = ''.join(lines)
    copy_to_chip(text)
    print("[+] Copied to Chipboard [+]")

# ----------- Copy to Chipboard ---------------
def copy_to_chip(text):
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()

# ---------- Main module ----------
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Copy the text from file to Cilpboard.')
    parser.add_argument('--file',required=True)
    parser.add_argument('--line', type=int)
    parser.add_argument('--start', type=int)
    parser.add_argument('--end', type=int)
    parser.add_argument('--full', action='store_true', help='Do full copy')

    args = parser.parse_args();

    if args.line:
        copy_from_line(args.file,args.line)
    if args.start and args.end:
        copy_from_range(args.file,args.start,args.end)
    if args.full:
        copy_full(args.file)
    #print("Hola form ChipPower")

    #if len(sys.argv) < 4:
    #   print("Usage: python copychip.py <file> <start_line> [<end_line]")
    #   sys.exit(1) 

#print("End of the project")
