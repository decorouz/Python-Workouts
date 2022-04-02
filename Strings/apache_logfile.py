import sys


def read_apache_404_error(filename):
    """Read through an Apache logfile. 
        If there is a 404 error—you can just search for
        ' 404 ', if you want—display the IP address, which should be the first element.

    Args:
        filename (txt): Apache logfile
    """
    for one_line in open(filename):
        if "404" in one_line:
            print(one_line.split()[0])


file = sys.argv[1]
read_apache_404_error(file)
