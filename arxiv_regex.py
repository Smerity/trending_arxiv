import re

tests = [
  'http://arxiv.org/pdf/1603.01547v2.pdf',
  'arxiv.org/pdf/1602.02218v2.pdf',
  'http://arxiv.org/abs/1603.01547',
  'https://arxiv.org/abs/1605.01335v1',
  'https://arxiv.org/dog/1605.01335v1',
]

re_get_arxiv_id = re.compile(r'arxiv.org/(?:abs|pdf)/(\d{4}\.\d{5})(?:v\d)?(?:\.pdf)?')

def get_arxiv_id(url):
  matches = re_get_arxiv_id.findall(url)
  if not matches:
    return None
  return matches[0]

if __name__ == '__main__':
  for t in tests:
    print re_get_arxiv_id.findall(t)
    print get_arxiv_id(t)
