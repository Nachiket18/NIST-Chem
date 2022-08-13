import mechanicalsoup
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

print(profiles_page.url)



