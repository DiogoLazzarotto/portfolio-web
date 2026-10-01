"""Verifica arquivos locais e âncoras referenciadas pelo HTML do portfólio."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT=Path(__file__).resolve().parents[1]
class References(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.refs=[]
    def handle_starttag(self,tag,attributes):
        a=dict(attributes)
        if 'id' in a:self.ids.add(a['id'])
        for name in ['src','href']:
            if name in a:self.refs.append(a[name])

def main():
    parser=References();parser.feed((ROOT/'index.html').read_text(encoding='utf-8'))
    for ref in parser.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        if url.path:
            target=ROOT/unquote(url.path)
            if not target.is_file():raise ValueError(f'Arquivo ausente: {url.path}')
        elif url.fragment and url.fragment not in parser.ids:
            raise ValueError(f'Âncora ausente: {url.fragment}')
    print(f'{len(parser.refs)} referências conferidas; arquivos e âncoras locais válidos')
if __name__=='__main__':main()
