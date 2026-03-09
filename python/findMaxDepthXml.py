# Implement a function to reverse a linked list (you don't need to define a full linked list class, just the logic).
# Complexity: 
# Desired time: 
# Time taken to solve: 
"""
Sample input1
2
<feed xml:lang='en'>
</feed>
0
Expected Output: 0

Sample input2
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Expected Output: 2

Sample input3
21
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>
Expected Output: 2
"""
import xml.etree.ElementTree as etree

# Initialize maximum depth
max_depth = 0

def depth(elem, level):
    global max_depth
    # Update the maximum depth if the current level exceeds it
    if level > max_depth:
        max_depth = level
    # Recursively process child elements
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    # Input the number of lines and the XML document
    n = int(input())
    xml_data = ""
    for _ in range(n):
        #xml_data += input().strip()
        xml_data += input() + "\n"
            
    # Parse the XML and compute depth
    tree = etree.ElementTree(etree.fromstring(xml_data))
    root = tree.getroot()
    depth(root, 0)

    # Output the maximum depth
    print(max_depth)