def morse_file(filename):
    with open(filename, encoding="UTF-8") as f:
        morse = {}
        
        for row in f:
            snip = row.strip().split()
            space_join = " ".join(snip[1])
            morse[snip[0].lower()] = list(space_join)
    
    return morse

def morse_list(dic, string):         
    
    snip = string.lower().split(" ")
    
    lspace_list = [] 
        
    for seg in snip:
        space_add = ["   "] * (len(seg) * 2 -1)
        
        space_add[::2] = seg
        
        lspace_list.append(seg)
    
    wspace_list =[]
    for w in lspace_list:
    
        for l in w:
            if l in dic:
                wspace_list += dic[l]
            else:
                wspace_list += [l]
        wspace_list += ["       "]
      
    
    return wspace_list

def to_css(lst):
    
    count = 0

    for l in lst[:-1]:
        if l == "-":
            count += 3
        else:
            count += len(l)

    frame_unit = 100/count

    time = 0

    css =""

    for i in range(len(lst) - 1):
        if lst[i] == ".":
            time += frame_unit
            css += str(round(time, 2))+"%" + "{background-color: #fbff00;\n box-shadow:0 0 10px 10px rgba(255, 255, 190, 0.8);}\n"
        elif lst[i] == " ":
            time += frame_unit
            css += str(round(time, 2))+"%" + "{background-color: #a8a8a8;\n box-shadow: none;}\n"
        elif lst[i] == "-":
            time += frame_unit * 3
            css += str(round(time, 2))+"%" + "{background-color: #fbff00;\n box-shadow:0 0 10px 10px rgba(255, 255, 190, 0.8);}\n"
        elif lst[i] == "   ":
            time += frame_unit * 3
            css += str(round(time, 2))+"%" + "{background-color: #a8a8a8;\n box-shadow: none;}\n"
        elif lst[i] == "       ":
            time += frame_unit * 7
            css += str(round(time, 2))+"%" + "{background-color: #a8a8a8;\n box-shadow: none;}\n"
    
    return css
            