import bs4
import certifi
import urllib3



def make_soup(html):
    return bs4.BeautifulSoup(html, 'html.parser')


def get_page(url):
    #http = urllib3.PoolManager()
    http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED', 
                               ca_certs = certifi.where())

    try:
        r = http.request('GET', url)

    except r.status != '200':
        
        print('deu m*Rd*!')
        return
    
    return r.data


def read_file(fpath):
    with open(fpath, 'rb') as fh:
        return fh.read()


def write_file(fpath, text):
    with open(fpath, 'wb') as fh:
        fh.write(text)


def index_page(url):
    data = get_page(url)

    write_file('pg1', data)

    print('indexed page %s'%url)

#url = "https://www.correiobraziliense.com.br/euestudante"
url = "https://www.correiobrasiliense.com.br/euestudante"
#index_page(url)

def parse_page(fname):
    html = read_file('pg1')
    soup = make_soup(html)
    print(soup.title)
    for el in (soup.findAll('h3')):
        print(el)

#parse_page('pg1')


