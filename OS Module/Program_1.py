#Pratik Sanjay Belhekar
#Program 1
#python 2.7

import sys
import argparse
import os,time
import glob
from stat import ST_MTIME
parser = argparse.ArgumentParser(description="""This application takes a string and navigates the file system looking for either a file or directory.  """)

parser.add_argument("-f","--file", type = str, nargs='+', help = "Gives only list of files.")

parser.add_argument("-d","--directory", type = str, nargs='+', help = "Gives only list of directories.")

parser.add_argument("-m","--last-modified", type = str, nargs='+', help = "The time the file/directory was last modified.")

parser.add_argument("root",type = str, nargs='*', help = "Start looking into root directory.for eg: c:/user/username")

parser.add_argument("string", type = str, nargs='*', help = "Use to search for file or directory.for eg *.py or foldername")
#print parser.print_help()
if __name__=="__main__":
    args = parser.parse_args()
    try:
        if args.root != " " or args.string != " ":
            allargv = sys.argv[1:]

            '''File operation'''
            if allargv[0] == "-f" or allargv[0] == "--file" :
                if os.path.isfile(allargv[2]):
                    for rot, dir, file in os.walk(allargv[1]):
                        for files in glob.glob(os.path.join(rot,allargv[2])):
                            print "    ", os.path.abspath(files)
                else:
                    print "Enter File name or file extension"\

                    '''Directory Operation'''
            elif allargv[0] == "-d" or allargv[0] == "--directory" :
                if os.path.isdir(allargv[2]):
                    for rot, dir, file in os.walk(allargv[1]):
                        for dirs in glob.glob(os.path.join(rot,allargv[2])):
                            print "    ", os.path.abspath(dirs)
                else:
                    print "Enter directory name to search for directory"

                    '''Last-Modified Operation'''
            elif allargv[0] == "-m" or allargv[0] == "--last-modified" :
            #print os.getcwd()
            # #print os.listdir('.')
                 if os.path.isdir(allargv[2]):
                     for rot, dir, file in os.walk(allargv[1]):
                         #print "Root : - ", rot,"\n"
                         for dirs in glob.glob(os.path.join(rot,allargv[2])):
                             dst = os.stat(dirs)
                             print "    ","Directory : - ", os.path.abspath(dirs)
                             print "    ","    ","Last Modified",time.asctime(time.localtime(dst[ST_MTIME])),"\n"
                 else:
                     for rot, dir, file in os.walk(allargv[1]):
                         for files in glob.glob(os.path.join(rot, allargv[2])):
                             fst = os.stat(files)
                             print  "    ", "File: - ", os.path.abspath(files)
                             print "    ","    ","\t","Last Modified",time.asctime(time.localtime(fst[ST_MTIME])),"\n"
                             #print  "last-modified Operation"

                             '''Both File and Directory operation'''
            else:
                #print allargv[0]
                for rot, dir, file in os.walk(allargv[0]):
                    print "\n","Root : - ", rot
                    for dirs in dir:
                        print "    ","Directory : - ", os.path.abspath(dirs)
                        for files in glob.glob(os.path.join(rot, allargv[1])):
                            print "    ", "Files : - ", os.path.abspath(files)
        else:
            print parser.print_help()
    except IndexError:
        print "\n IndexError -- Pass Both the arguments with operation Eg:- -f root string","\n"
        print  parser.print_help()



