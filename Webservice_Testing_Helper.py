import sys
import re
import os.path
import itertools

def extractor(folder,d):
    
    for filename in os.listdir (folder):
        
        if '_c.txt' in filename:
            filetxt=open(folder+'\\'+filename,'r')
            g1=filetxt.read()
            if re.search(r'SOAPAction:',g1,re.IGNORECASE)==None:
                print "Not a soap request"
                continue
            #this is for the 1st line of the request...which contains the url(including the service that is called)
            m=re.findall(r'POST([\w / . : ]+) HTTP/1.1',g1,re.IGNORECASE)
            print m
            string1=''.join(m)
            #from the url,we are trying to extract just the final service name called
            ms=re.findall("http.*/([^/]+).svc",string1,re.IGNORECASE)
            st=''.join(ms)
            
            if not os.path.exists(d+st):
                os.mkdir(d+st)

                #this is to get the url+method called
            s=re.findall(r'SOAPAction: "([: \w / .]+)"',g1,re.IGNORECASE)

            #to extract just the method name
            sm = re.findall("SOAPAction.*/([^/]+)\"",g1,re.IGNORECASE)
            st1=''.join(sm)
            print st1

            #this is the actual soap xml request(so include all the special chars that could be there
            k=re.findall(r'\n\n([- " : \w / . > \s = < # + @ ! $ % & * , ? ; : ` ~ \']+)',g1,re.IGNORECASE)


            if not os.listdir(d+st):
                fileout=open(d+st+'\\'+st1+'.txt','w')
                c = itertools.chain(m,s,k)
                for i in c:
                       fileout.write("\n\n"+i)
            else:
                for files in os.listdir(d+st):
                    if not st1 in files:
                        fileout=open(d+st+'\\'+st1+'.txt','w')
                        c = itertools.chain(m,s,k)
                        for i in c:
                            fileout.write("\n\n"+i)
                    else:
                        fileout=open(d+st+'\\'+st1+'.txt','a')
                        c = itertools.chain(m,s,k)
                        for i in c:
                            fileout.write("\n\n"+i)

                            
def main():
    readfolder=raw_input("Enter the path where Fiddler decompressed files are saved\n")
    writefolder=raw_input("Enter the path of the folder where the output has to be saved\n")
    writefolder=writefolder+ '\\'
    
    y=readfolder.replace("\\","\\\\")
    y1=writefolder.replace("\\","\\\\")
    print y1
    extractor(y,y1)
    
if __name__ == "__main__":
    main()
