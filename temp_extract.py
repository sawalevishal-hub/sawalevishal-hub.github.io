import zipfile, os, xml.etree.ElementTree as ET
p = os.path.join('knowledge', 'Vishal Sawale_11July 2026.docx')
z = zipfile.ZipFile(p)
data = z.read('word/document.xml')
root = ET.fromstring(data)
ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
texts = []
for par in root.findall('.//w:p', ns):
    parts = []
    for t in par.findall('.//w:t', ns):
        parts.append(t.text or '')
    txt = ''.join(parts)
    if txt.strip():
        texts.append(txt.strip())
for line in texts:
    print(line)
