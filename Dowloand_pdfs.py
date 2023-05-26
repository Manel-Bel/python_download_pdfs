import pandas as pd
import os, requests

from bs4 import BeautifulSoup

# enter the url from which you will be downloading pdfs
def download_fon(the_url, dir_path):

    url = the_url
    rep = requests.get(url)
    print(rep) #<Response [200]>

    #to parse the text 
    parse = BeautifulSoup(rep.text,"html.parser")

    #we need the liks 
    links = parse.find_all('a')

    dossier = dir_path
    os.mkdir(dossier)
    count = 0
    #we are going to loop now in all the links to find the pdf's ones
    for link in links :
        print(link)
        if('.pdf' in link.get('href',[])):
            count += 1
            print("fichier: ", link.get('href', []))
            rep = requests.get(url + link.get('href'))
            if(rep.status_code == 200):
                fichier_path = os.path.join(dossier,os.path.basename(link.get('href')))
                print(fichier_path)
                # Write content in pdf fichier
                with open(fichier_path,'wb') as f :
                    f.write(rep.content)
                # pdf = open(str(link.get('href', [])), 'wb')
                # pdf.write(rep.content)
                # pdf.close()
                print("Fichier ", count, " downloaded")
    #  
    print("All PDF files downloaded")

if __name__ == '__main__':
    print("Enter the url")
    the_url = input()
    print("Enter the directory name")
    dir_path = input()
    download_fon(the_url,dir_path)