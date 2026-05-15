import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")
parser.add_argument("-r", "--recursive", action="store_true", default=False)
parser.add_argument("-d","--directory",dest="directories_only",action="store_true",default=False)
parser.add_argument("--files","-f",dest="files_only",action="store_true",default=False)
parser.add_argument("-s","--size",dest="show_size",action="store_true",default=False)
parser.add_argument("-e","--extension",dest="extension_filter",type=str,default=None)
parser.add_argument("--only-names",dest="only_names",action="store_true",default=False)
parser.add_argument("-o", "--output", dest="output_file", type=str, default=None)
parser.add_argument("--silent", dest="silent", action="store_true", default=False)

# Estas opciones faltan ser implementadas, son los comandos de ls de Linux, se pueden agregar como opciones adicionales para el usuario, pero no es necesario implementarlas todas, se pueden ir agregando poco a poco

parser.add_argument("-a", "--all", dest="show_all", action="store_true", default=False)
parser.add_argument("-A", "--almost-all", dest="show_almost_all", action="store_true", default=False)
parser.add_argument("--author", dest="show_author", action="store_true", default=False)
parser.add_argument("--sort", dest="sort", action="store_true", default=False)
parser.add_argument("-D", "--dired", dest="dired", action="store_true", default=False)
parser.add_argument("-f") #same as a and -U
parser.add_argument("-F", "--classify", dest="classify", action="store_true", default=False)
parser.add_argument("--file-type", dest="file_type", action="store_true", default=False)
parser.add_argument("--format", dest="format", type=str, default=None)
parser.add_argument("--full-time", dest="full_time", action="store_true", default=False)
parser.add_argument("-g") # like l but do not list owner
parser.add_argument("--group-directories-first", dest="group_directories_first", action="store_true", default=False)
parser.add_argument("-G", "--no-group", dest="no_group", action="store_true", default=False)
parser.add_argument("-h", "human_readable", nargs='?', default=False, const=True, help="Display sizes in human readable format")
parser.add_argument("--si", dest="si", nargs='?', default=False, const=True,
                    help="Use powers of 1000 instead of 1024")

parser.add_argument("-H", "--dereference-command-line", dest="dereference_command_line",
                    action="store_true",
                    help="Follow symbolic links listed on the command line")

parser.add_argument("--dereference-command-line-symlink-to-dir",
                    dest="dereference_command_line_symlink_to_dir",
                    action="store_true",
                    help="Follow command line symlinks that point to directories")

parser.add_argument("--hide", dest="hide", metavar="PATTERN",
                    help="Do not list entries matching PATTERN (overridden by -a or -A)")

parser.add_argument("--hyperlink", dest="hyperlink", nargs='?', const="auto",
                    help="Hyperlink file names (optional WHEN value)")

parser.add_argument("--indicator-style", dest="indicator_style", metavar="WORD",
                    help="Append indicator style: none, slash, file-type, classify")

parser.add_argument("-i", "--inode", dest="inode", action="store_true",
                    help="Print inode number of each file")

parser.add_argument("-I", "--ignore", dest="ignore", metavar="PATTERN",
                    help="Do not list entries matching PATTERN")

parser.add_argument("-k", "--kibibytes", dest="kibibytes", action="store_true",
                    help="Use 1024-byte blocks (only with -s)")

parser.add_argument("-l", dest="long_format", action="store_true",
                    help="Use long listing format")

parser.add_argument("-L", "--dereference", dest="dereference", action="store_true",
                    help="Show info of target file instead of symlink")

parser.add_argument("-m", dest="comma_format", action="store_true",
                    help="Fill width with comma-separated entries")

parser.add_argument("-n", "--numeric-uid-gid", dest="numeric_uid_gid",
                    action="store_true",
                    help="Show numeric UID and GID")

parser.add_argument("-N", "--literal", dest="literal", action="store_true",
                    help="Print names without quoting")

parser.add_argument("-o", dest="no_group", action="store_true",
                    help="Like -l but without group info")

parser.add_argument("-p", "--indicator-style", dest="indicator_style_slash",
                    action="store_const", const="slash",
                    help="Append / to directories")

parser.add_argument("-q", "--hide-control-chars", dest="hide_control_chars",
                    action="store_true",
                    help="Replace non-printable chars with ?")

parser.add_argument("--show-control-chars", dest="show_control_chars",
                    action="store_true",
                    help="Show control chars as-is")

parser.add_argument("-Q", "--quote-name", dest="quote_name",
                    action="store_true",
                    help="Enclose names in double quotes")

parser.add_argument("--quoting-style", dest="quoting_style", metavar="WORD",
                    help="Set quoting style for names")

parser.add_argument("-r", "--reverse", dest="reverse", action="store_true",
                    help="Reverse sort order")

parser.add_argument("-R", "--recursive", dest="recursive", action="store_true",
                    help="List subdirectories recursively")

parser.add_argument("-s", "--size", dest="size", action="store_true",
                    help="Print allocated size in blocks")

parser.add_argument("-S", dest="sort_size", action="store_true",
                    help="Sort by file size (largest first)")

parser.add_argument("--sort", dest="sort", metavar="WORD",
                    help="Change sorting method: name, size, time, etc.")

parser.add_argument("--time", dest="time", metavar="WORD",
                    help="Select timestamp type (atime, mtime, ctime, birth)")

parser.add_argument("--time-style", dest="time_style", metavar="TIME_STYLE",
                    help="Set date/time format for -l")

parser.add_argument("-t", dest="sort_time", action="store_true",
                    help="Sort by modification time (newest first)")

parser.add_argument("-T", "--tabsize", dest="tabsize", type=int,
                    help="Set tab width")

parser.add_argument("-u", dest="access_time", action="store_true",
                    help="Use access time for sorting/display")

parser.add_argument("-U", dest="no_sort", action="store_true",
                    help="Do not sort entries")

parser.add_argument("-v", dest="version_sort", action="store_true",
                    help="Natural version sort")

parser.add_argument("-w", "--width", dest="width", type=int,
                    help="Set output width (0 = no limit)")

parser.add_argument("-x", dest="by_lines", action="store_true",
                    help="List entries by lines")

parser.add_argument("-X", dest="sort_extension", action="store_true",
                    help="Sort by file extension")

parser.add_argument("-Z", "--context", dest="context", action="store_true",
                    help="Print security context")

parser.add_argument("--zero", dest="zero", action="store_true",
                    help="End lines with NUL instead of newline")

parser.add_argument("-1", dest="one_per_line", action="store_true",
                    help="One file per line")

parser.add_argument("--version", dest="version", action="store_true",
                    help="Show version information")


def list_path(**kwargs): 
    path = kwargs.get("path")
    recursive = kwargs.get("recursive", False)
    directories_only = kwargs.get("directories_only", False)
    files_only = kwargs.get("files_only", False)
    show_size = kwargs.get("show_size", False)
    extension_filter = kwargs.get("extension_filter", None)
    only_names = kwargs.get("only_names", False)
    output_file = kwargs.get("output_file", None)
    silent = kwargs.get("silent", False)

    print(f"Listing contents of: {path}")
    p = Path(path) 
    if not p.exists(): 
        print(f"Error: The path '{path}' does not exist.") 
        return 

    result = []

    for item in p.iterdir() if not recursive else p.rglob('*'): 
        if directories_only and not item.is_dir(): 
            continue 
        if files_only and not item.is_file(): 
            continue 
        if extension_filter and item.suffix != extension_filter: 
            continue 
        size_info = f" ({item.stat().st_size} bytes)" if show_size and item.is_file() else "" 
        item = item.name if only_names else str(item)
        result.append(f"{item}{size_info}")

        if silent:
            continue
        print(f"{item}{size_info}")

    if output_file: 
        with open(output_file, 'w') as f: 
            f.write("\n".join(result)) 
        print(f"Output written to {output_file}")
        
if __name__ == "__main__": 
    args = parser.parse_args() 
    list_path(**vars(args))