import xml.etree.ElementTree as ET
import json
data = {'1': ['张三', 100, 120, 150], '2': ['李四', 90, 89, 60], '3': ['王五', 60, 80, 120]}


def process_xml():
    new_xml = ET.Element('Root')
    students = ET.SubElement(new_xml, 'Students')
    students.text = json.dumps(data)
    et = ET.ElementTree(new_xml)
    et.write('student.xml', encoding='utf-8', xml_declaration=True)
    ET.dump(et)


if __name__ == '__main__':
    process_xml()
