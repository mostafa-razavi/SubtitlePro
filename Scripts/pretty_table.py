import ntpath

def prettyTable(dictionary, cssClass=''):
    ''' pretty prints a dictionary into an HTML table(s) '''
    if isinstance(dictionary, str):
        return '<td>' + dictionary + '</td>'
    s = ['<table ']
    if cssClass != '':
        s.append('class="%s"' % (cssClass))
    s.append('>\n')
    for key, value in dictionary.items():
        s.append('<tr>\n  <td valign="top"><strong>%s</strong></td>\n' % str(key))
        if isinstance(value, dict):
            if key == 'picture' or key == 'icon':
                s.append('  <td valign="top"><img src="%s"></td>\n' % prettyTable(value, cssClass))
            else:
                s.append('  <td valign="top">%s</td>\n' % prettyTable(value, cssClass))
        elif isinstance(value, list):
            s.append("<td><table>")
            for i in value:
                s.append('<tr><td valign="top">%s</td></tr>\n' % prettyTable(i, cssClass))
            s.append('</table>')
        else:
            if key == 'picture' or key == 'icon':
                s.append('  <td valign="top"><img src="%s"></td>\n' % value)
            else:
                s.append('  <td valign="top">%s</td>\n' % value)
        s.append('</tr>\n')
    s.append('</table>')

    return '\n'.join(s)

def generate_html_from_dictionary(dictionary, output_html_path):
    with open(output_html_path, 'w', encoding='utf-8') as filehandle:
        for listitem in prettyTable(dictionary, cssClass=''):
            filehandle.write(listitem)  
    return ntpath.basename(output_html_path)
