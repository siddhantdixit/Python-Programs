import glob
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_printable_size(byte_size):
    """
    A bit is the smallest unit, it's either 0 or 1
    1 byte = 1 octet = 8 bits
    1 kB = 1 kilobyte = 1000 bytes = 10^3 bytes
    1 KiB = 1 kibibyte = 1024 bytes = 2^10 bytes
    1 KB = 1 kibibyte OR kilobyte ~= 1024 bytes ~= 2^10 bytes (it usually means 1024 bytes but sometimes it's 1000... ask the sysadmin ;) )
    1 kb = 1 kilobits = 1000 bits (this notation should not be used, as it is very confusing)
    1 ko = 1 kilooctet = 1000 octets = 1000 bytes = 1 kB
    Also Kb seems to be a mix of KB and kb, again it depends on context.
    In linux, a byte (B) is composed by a sequence of bits (b). One byte has 256 possible values.
    More info : http://www.linfo.org/byte.html
    """
    BASE_SIZE = 1024.00
    MEASURE = ["B", "KB", "MB", "GB", "TB", "PB"]

    def _fix_size(size, size_index):
        if not size:
            return "0"
        elif size_index == 0:
            return str(size)
        else:
            return "{:.3f}".format(size)

    current_size = byte_size
    size_index = 0

    while current_size >= BASE_SIZE and len(MEASURE) != size_index:
        current_size = current_size / BASE_SIZE
        size_index = size_index + 1

    size = _fix_size(current_size, size_index)
    measure = MEASURE[size_index]
    return size + measure


def run():
    x = filter(os.path.isfile,glob.glob('**/*',recursive=True))

    myf = {}
    cnt=0
    for i in x:
        cnt+=1
        myf[str(i)] = os.stat(i).st_size

    sorted_dt = {key: value for key, value in sorted(myf.items(), key=lambda item: item[1])}

    print('\n'*2)
    print(bcolors.HEADER+'  GIGANTIC LOOP '+bcolors.ENDC)
    print('\n'*2)

    for k, v in sorted_dt.items():
        # print ("{:<15} {:<10}".format(get_printable_size(v), k))
        print(bcolors.OKGREEN,end="")
        print ("{:<15}".format(get_printable_size(v)),end="")
        print(bcolors.OKCYAN,end="")
        print ("{:<10}".format(k))
        

    print(bcolors.ENDC)

    print('\n'*3)