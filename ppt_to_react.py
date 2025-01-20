import json

def px_from_points(points):
    return f"{points * 1.33333}px"

def convert_color(color):
    return color.lower()

def format_style_dict(style_dict):
    return ("{{" + ", ".join(f'{k}: "{v}"' for k, v in style_dict.items()) + "}}").replace("'", "")

def format_text_style(font):
    style = {}
    if 'Color' in font:
        style['color'] = convert_color(font['Color'])
    if 'FontSize' in font:
        style['fontSize'] = f"{font['FontSize']}px"
    if 'FontName' in font:
        style['fontFamily'] = font['FontName']
    if font.get('Bold'):
        style['fontWeight'] = 'bold'
    if font.get('Italic'):
        style['fontStyle'] = 'italic'
    return style

def handle_bullet_points(paragraphs):
    has_bullets = any(para.get('ListFormat', {}).get('Type') == 'Bulleted' for para in paragraphs)
    if not has_bullets:
        return False, []
    
    bullet_items = []
    for para_idx, para in enumerate(paragraphs):
        if not para.get('Text'):
            continue
            
        text_style = {}
        if para.get('TextParts'):
            text_style = format_text_style(para['TextParts'][0]['Font'])
        
        indent = para.get('IndentLevelNumber', 0) * 20
        text_style['marginLeft'] = f"{indent}px"
        
        bullet_items.append(f"          <li key='{para_idx}' style={format_style_dict(text_style)}>{para['Text']}</li>")
    
    return True, bullet_items

def convert_to_react(data):
    react_code = [
        "import React from 'react';",
        "",
        "const SlideComponent = () => {",
        "  return (",
        "    <div style={{ position: 'relative', width: '100%', height: '100%', backgroundColor: '#fff', paddingBottom: '30px' }}>"
    ]
    
    for idx, item in enumerate(data):
        if item.get('Info'):
            continue
            
        if item['SlideItemType'] == 'AutoShape':
            style = {
                'position': 'absolute',
                'left': px_from_points(item['Left']),
                'top': px_from_points(item['Top']),
                'width': px_from_points(item['Width']),
                'height': px_from_points(item['Height']),
                'transform': f"rotate({item.get('Rotation', 0)}deg)",
            }
            
            shape_type = item['AutoShapeType'].lower()
            if shape_type == 'rightarrow':
                style['clipPath'] = 'polygon(0% 20%, 75% 20%, 75% 0%, 100% 50%, 75% 100%, 75% 80%, 0% 80%)'
                style['backgroundColor'] = '#E97032'
            elif shape_type == 'rectangle' and item['TextBody'].get("WrapText") == True:
                style['backgroundColor'] = '#156082' 
            #hardcoded color for rectangle due to missing color property in json
               

            react_code.append(f"      <div key='{idx}' style={format_style_dict(style)}>")
            
            if 'TextBody' in item:
                is_bullet_list, bullet_items = handle_bullet_points(item['TextBody']['Paragraphs'])
                
                if is_bullet_list:
                    react_code.append("        <ul style={{ listStyleType: 'disc', paddingLeft: '20px', margin: 0 }}>")
                    react_code.extend(bullet_items)
                    react_code.append("        </ul>")
                else:
                    isVerticalMiddle = item['TextBody'].get('VerticalAlignment') == 'Middle'
                    for para_idx, para in enumerate(item['TextBody']['Paragraphs']):
                       
                        if not para.get('Text'):
                            continue
                            
                        text_style = {}
                        if para.get('TextParts'):
                            text_style = format_text_style(para['TextParts'][0]['Font'])
                        
                        # Add text alignment
                        if para.get('HorizontalAlignment'):
                            text_style['textAlign'] = para['HorizontalAlignment'].lower()
                        if isVerticalMiddle:
                            text_style['display'] = 'flex'
                            text_style['alignItems'] = 'center'
                            text_style['justifyContent'] = 'center'
                            text_style['height'] = '100%'
                        
                   
                        
                        react_code.append(f"        <div key='{idx}-{para_idx}' style={format_style_dict(text_style)}>{para['Text']}</div>")
            
            react_code.append("      </div>")
    
    react_code.extend([
        "    </div>",
        "  );",
        "};",
        "",
        "export default SlideComponent;"
    ])
    
    return '\n'.join(react_code)




def main():
    """"Main function to convert ppt to react"""
    try:
        with open("sample_slide.json", "r") as file:
            data = json.load(file)
            react_code = convert_to_react(data)
            with open("output.jsx", "w") as file:
                file.write(react_code)
    except FileNotFoundError:
        print("sample_slide.json not found")
        return


if __name__ == "__main__":
    main()  