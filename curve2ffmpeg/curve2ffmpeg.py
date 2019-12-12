#!/usr/bin/env python3

# import
import sys, re, os, getopt, os.path, mimetypes
from datetime import datetime 

# script usage
def usage():
    '''script usage
    
    display script usage when the -h or --help option is used
    '''
    usage = """
-h --help display help
-i gimp curve file

curve2ffmpeg -i <gimpe curve>
    """
    print(usage)

def checkfile(infile):
    ''' check first argument passed to script
    
    check if first argument passed to script, 
    is a text file and if so open it and read the contents,
    and set the variable infile to equal the contents of the text file.
    then check if the string is a url
    '''
    if os.path.isfile(infile):
        if mimetypes.guess_type(infile)[0] == 'text/plain':
            with open(infile, 'r') as file:
                infile = file.read()
            file.close()          
            return infile
    
# argv
argv = sys.argv[1:]

# main
def main(argv):
    ''' main function
    
    check number of arguments passed to script
    '''

    if len(argv) == 0: # no arguments passed to script
        print("No arguments passed to script")
        usage()    # display script usage
        sys.exit() # exit
    elif len(argv) > 2: # too many arguments passed to script
        print("Too many arguments passed to script")
        usage()    # display script usage
        sys.exit() # exit
        
    try:
        opts, args = getopt.getopt(argv, "hi:", ["help", "infile"])
    except getopt.GetoptError as err: 
        print(err)  # will print something like "option -x not recognized"
        usage()     # display script usage
        sys.exit(2) # exit

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # -h or --help = display help
            usage()
            sys.exit()
        elif opt == ("-i") and len(argv) == 2:
            # -i and url or text file
            return result

        else:
            assert False, "unhandled option"


#=================================================#
# slice off script name from arguments
#=================================================#

def entry():
    main(sys.argv[1:])

    #make generator
    lower=0
    upper=1
    length=256
    zerotoonestepped256gen = [lower + x*(upper-lower)/length for x in range(length)]

    def formatForFFMPEG(values):
        serializedValues = values.split(' ')
        list = []
        for i in range (len(serializedValues)):
            if not list or zerotoonestepped256gen[i] - float(re.match(r"^[^////]*",list[-1]).group(0)) > 0.01:
                list.append('%s/%s' % (zerotoonestepped256gen[i], serializedValues[i]))
        return list
    
    home = os.path.expanduser('~')
    desktop = 'Desktop'
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = 'txt'
    outfile = os.path.join(home, desktop, 'infile-{}.{}'.format(time, ext))
    
#    if sys.platform.startswith('linux'):
#    elif sys.platform.startswith('freebsd'):
#    elif sys.platform.startswith('win32'):
#        home = os.path.expanduser('~').replace('\\', '/')
#        desktop = '//Desktop//'
#        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#        ext = '.txt'
#        outfile = home + desktop + 'infile-' + time + ext
#    elif sys.platform.startswith('darwin'):

    # checkfile
    checkfile(argv[1])

    #get filename
    #file = input('Please input the absolute path to the GIMP Color Curve Preset File: ')
    
    #Open the curves file
    #curvesfile = open(file,"r")
    #curvesString = curvesfile.read()
    #foundValues = re.findall(r'(?<=samples 256) [\d. ]*',curvesString)

    foundValues = re.findall(r'(?<=samples 256) [\d. ]*',infile)
    
    masterValues = formatForFFMPEG(foundValues[0][1:])
    redValues = formatForFFMPEG(foundValues[1][1:])
    greenValues = formatForFFMPEG(foundValues[2][1:])
    blueValues = formatForFFMPEG(foundValues[3][1:])
    alphaValues = formatForFFMPEG(foundValues[4][1:])
    
    commandPrelim = 'curves=master="'
    
    command = commandPrelim + ' '.join(masterValues) + '":red="' + ' '.join(redValues) +'":green="' + ' '.join(greenValues) + '":blue="' + ' '.join(blueValues) + '"'

    # save file
    with open(outfile, 'w') as out:
        out.write(command)
