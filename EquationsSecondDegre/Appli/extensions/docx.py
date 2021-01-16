import zipfile
import prgm
import os

def main(path):
    file_write=zipfile.ZipFile(path+'.docx','w')
    file_write.write(r'extensions/docx/[Content_Types].xml','[Content_Types].xml',zipfile.ZIP_DEFLATED)
    file_write.write(r'extensions/docx/.rels','_rels\\.rels',zipfile.ZIP_DEFLATED)
    file_write.write(r'extensions/docx/numbering.xml','word\\numbering.xml',zipfile.ZIP_DEFLATED)
    file_write.write(r'extensions/docx/styles.xml','word\\styles.xml',zipfile.ZIP_DEFLATED)
    file_write.write(r'extensions/docx/document.xml.rels','word\\_rels\\document.xml.rels',zipfile.ZIP_DEFLATED)
    write_document=open(r'extensions/docx/document.xml','a',encoding="utf-8")
    write_document.writelines('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">\n    <w:body>')
    write_document.close()
    for i in range(len(prgm.rep)):
        write_document=open(r'extensions/docx/document.xml','a',encoding="utf-8")
        write_document.writelines('<w:p>\n            <w:r>\n                <w:rPr>\n                    <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial" />\n                    <w:color w:val="auto" /><w:spacing w:val="0" />\n                    <w:position w:val="0" />\n                    <w:sz w:val="24" />\n                    <w:shd w:fill="auto" w:val="clear" />\n                </w:rPr>\n                <w:t xml:space="preserve">'+prgm.rep[i]+'</w:t>\n            </w:r>\n        </w:p>\n')
        write_document.close()
    write_document=open(r'extensions/docx/document.xml','a',encoding="utf-8")
    write_document.writelines('    </w:body>\n</w:document>')
    write_document.close()
    file_write.write(r'extensions/docx/document.xml','word\\document.xml',zipfile.ZIP_DEFLATED)
    file_write.close()
    os.remove(r'extensions/docx/document.xml')
