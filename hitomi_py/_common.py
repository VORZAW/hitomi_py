'''
auxiliar module to the hitomi module
'''
import re

def subdomain_from_galleryid(g, number_of_frontends):
    try:
        o = int.from_bytes(g, 'little') % number_of_frontends
    except:
        o = g % number_of_frontends

    return ''.join(map(chr, [97 + o]))

def subdomain_from_url(url, base):
    retval = 'b'
    if base:
        retval = base
    
    number_of_frontends = 3
    
    r = '/[0-9a-f]/([0-9a-f]{2})/'
    m = re.findall(r, url)
    if not m:
        return 'a'
    
    g = bytes([int(m[0], base=16)])
    if type(g) == bytes:
        if g < b'\x30':
            number_of_frontends = 2
        if g < b'\x09':
            g = 1
        retval = subdomain_from_galleryid(g, number_of_frontends) + retval
    
    return retval

def url_from_url(url, base):
    return re.sub('//..?.hitomi.la/', '//'+subdomain_from_url(url, base)+'.hitomi.la/', url)

def full_path_from_hash(_hash):
    if len(_hash) < 3:
        return _hash
    result = re.findall('^.*(..)(.)$', _hash)
    return '{}/{}/'.format(result[0][1], result[0][0])+_hash

def url_from_hash(galleryid, image, _dir, ext):
    ext = ext or _dir or image['name'].split('.').pop(-1)
    _dir = _dir or 'images'
    
    return 'https://a.hitomi.la/'+_dir+'/'+full_path_from_hash(image['hash'])+'.'+ext

def url_from_url_from_hash(galleryid, image, _dir, ext, base):
    return url_from_url(url_from_hash(galleryid, image, _dir, ext), base)

if __name__ == '__main__':
    pass