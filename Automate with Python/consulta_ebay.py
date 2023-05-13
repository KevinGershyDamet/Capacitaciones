
import bs4, requests

def precioEbay(url):
    descarga = requests.get(url)
    descarga.raise_for_status()

    soup = bs4.BeautifulSoup(descarga.text, 'html.parser')
    elems = soup.select('#mainContent > form > div.vim-buybox-wrapper > div > div:nth-child(1) > div.x-buybox__price-section > div > div.x-bin-price__content > div.x-price-primary > span:nth-child(1) > span')
    return elems[0].text.strip()


price = precioEbay(r'https://www.ebay.com/itm/394498177508?hash=item5bd9ec79e4:g:qx8AAOSwDNBkBZYy&amdata=enc%3AAQAIAAAA8M1uqbvR40xEjukp1EPAHQ7jhNEdUQIb0V%2F5eKOIpvwbzH8ESE5jfM9qkwyCLGEqI8Fz8DCP5hQqCJdAzVtfkSsXgHDOXuSBB0ed3XIZoAzJNw1FmR%2Fp7Qr3WVntTDkFZEiEbs8D9tVBfy9%2FsomSig%2FqEOvnqWz%2BjJzO0n49a9%2F9odThWGrEq4kQfticnesakKDtzTKRumoQrlOVMmrNcOq2%2FRZokUV9Bf46jrwPa%2B6gbnh0ajeAasdnsph0lOBhkcBR4dU%2FwBiAjNi%2FyxEwXwfsFJ5W7uRJQ5meRRHaFk3dxPqitpDf184Pci92ENgg7g%3D%3D%7Ctkp%3ABFBM-OPWzv9h')
# print('El precio es ' + price)