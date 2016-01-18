import sys
import time
import os
import urllib
import gzip
import shutil
import tarfile
import subprocess


def download_file( organism_name, type ):
    ftp_site = "ftp://ftp.wormbase.org/pub/wormbase/species/"
    file_name = organism_name + ".canonical_bioproject.current." + type + ".fa.gz"
    url = ftp_site + organism_name + "/sequence/" + type + "/" + file_name
    data = [url,file_name]
    return data

def untar(fname):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname)
        loc = fname.split(os.path.sep)[0]
        tar.extractall(loc)
        tar.close()

def unzip(location, genome_url):
    zip_file = gzip.open(location,"rb")
    un_name = genome_url[1].split(".")[0] + ".fa"
    line = location.split(os.path.sep)[0]
    location = os.path.join(line,un_name)
    uncompressed_file = open(location,"wb")

    decoded = zip_file.read()
    uncompressed_file.write(decoded)

    zip_file.close()
    uncompressed_file.close()
    return location


def main():

    f = open("organisms.txt", "r")

    for line in f:
        line = line.rstrip("\n")
        if os.path.exists(line):
            shutil.rmtree(line)
            os.makedirs(line)
        else:
            os.makedirs(line)

        inparanoid_file_name = "inparanoid_4.1.tar.gz"
        inparanoid_file_loc = os.path.join(line,inparanoid_file_name)
        shutil.copyfile(inparanoid_file_name,inparanoid_file_loc)
        untar(inparanoid_file_loc)

        genome_url = download_file(line, "protein")
        location = os.path.join(line,genome_url[1])
        urllib.urlretrieve(genome_url[0], location)

        c_elegans_url = download_file("c_elegans","protein")
        c_elegans_loc = os.path.join(line, c_elegans_url[1])
        urllib.urlretrieve(c_elegans_url[0], c_elegans_loc)

        location = unzip(location, genome_url)
        c_elegans_loc = unzip(c_elegans_loc, c_elegans_url)

        os.system("python Prototype1.py " + location)
        os.system("python Prototype1.py " + c_elegans_loc)

        # Need to move the files after being processed.
        file_loc = location.split(".")[0]
        file_loc = file_loc + "_g.fa"

        c_elegans_proc = c_elegans_loc.split(".")[0]
        c_elegans_proc = c_elegans_proc + "_g.fa"

        dest_loc = os.path.join(location.split(os.path.sep)[0], "inparanoid_4.1")
        line_dest_loc = os.path.join(dest_loc,file_loc.split(os.path.sep)[-1])
        c_elegans_dest = os.path.join(dest_loc,c_elegans_proc.split(os.path.sep)[-1])
        perl_loc = os.path.join(dest_loc,"inparanoid.pl")

        if os.path.isfile(file_loc):
            shutil.copyfile(file_loc,line_dest_loc)
        if os.path.isfile(c_elegans_proc):
            shutil.copyfile(c_elegans_proc,c_elegans_dest)

        #var = "c_elegans.fa " + file_loc.split(os.path.sep)[-1]
        #pipe = subprocess.Popen(["perl",perl_loc, "c_elegans.fa", file_loc.split(os.path.sep)[-1]])

if __name__ == "__main__":
    main()