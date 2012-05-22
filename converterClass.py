import re
class fasta:
    filepat=re.compile(r"(.+)\..+")
    extpat=re.compile(r".+(\..+)")
    to_ext = ".txt"
    from_ext = ".fa"
    def extCheck(self, fileName):
        if self.from_ext == self.extpat.search(fileName).group(1):
            return True
        else:
            return False
        
    def changeExt(self, fileName):
        return self.filepat.search(fileName).group(1)+self.to_ext
    
    def main(self, fileName):
        input_file=open("{}".format(fileName), 'r')
        primary_input=input_file.read()##primary_input is now a string containing the original fasta data
        headpattern= re.compile(">(.+)$", re.M)##pattern for isolating the header
        whitespace = re.compile(r"( |\t|\r)")
        #filepat=re.compile(r"(.+)\..+")##pattern for finding the file path no matter the extension
        #input_filename=filepat.findall(fileLocation)[0]
        
        protoheaders = headpattern.findall(primary_input)
        headers = []
        for header in protoheaders:
            header = whitespace.sub('_', header)
            headers.append(header)
            
        bodies = re.split(">.*\\n", primary_input)##pattern for isolating bodies (sequences)
        bodies = bodies[1:]
        
        clean_bodies1=[]
        clean_bodies2=[]

        ##below eliminate all whitespaces that may have found their way into the sequences
        for i in bodies:
            clean_bodies1.append(re.sub("\\n", "", i))##may be redundant
        for i in clean_bodies1:
            clean_bodies2.append(i.strip(" \t\n\r"))
                
        newstring="Description\tSequence Data\n\n"
        
        for i in range(len(clean_bodies2)):
            newstring=newstring+headers[i]+"\t"+clean_bodies2[i]+"\n"##Format: head1<tab>body1<newline>...
        #print newstring
        
        output=open(self.changeExt(fileName), 'w')
        output.write(newstring)
        #print "File converted, saved as {}.tab".format(input_filename)
