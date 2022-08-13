from audioop import add
import mechanicalsoup
import urllib.request
import re


def retrieve_fluid_data(downloads_folder):

    browser = mechanicalsoup.Browser()

    url = "https://webbook.nist.gov/cgi/fluid.cgi?TUnit=K&PUnit=bar&DUnit=g%2Fml&HUnit=kJ%2Fmol&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=dyn%2Fcm&Type=IsoBar&RefState=DEF&Action=Page&ID=C112403"
    page = browser.get(url)

    html_page = page.soup
    form = html_page.select('form')[0]
    form.select('input')[0]["value"] = 15
    form.select('input')[1]["value"] = 290
    form.select('input')[2]["value"] = 700
    form.select('input')[3]["value"] = 1

    form.select('select')[0]["value"] = 10 

    profiles_page = browser.submit(form, page.url)


    links = profiles_page.soup.select("a")

    base_path = "https://webbook.nist.gov/"

    for link in links:
        
        if link.has_attr('href'):
            address = link["href"]
            text = link.text
            if text.strip() == 'Download data':
                address = base_path + address
                urllib.request.urlretrieve(address,downloads_folder)
                break
            

def main():
    downloads_folder = "D:\\NIST_Automation\\downloads\\download_data.txt"
    retrieve_fluid_data(downloads_folder)  

if __name__ == '__main__': 
    main()


