def brain_luck(code, input):
    output = ''
    arr = [0]
    arr_pos = 0
    arr_size = 1
    in_pos = 0
    command_pos = 0

    while command_pos < len(code):
        command = code[command_pos]
        if command == '>':
            arr_pos += 1
            if arr_pos == arr_size:
                arr.append(0)
                arr_size += 1
        elif command == '<':
            arr_pos -= 1
        elif command == '+':
            arr[arr_pos] = (arr[arr_pos] + 1) % 256
        elif command == '-':
            arr[arr_pos] = (arr[arr_pos] + 255) % 256
        elif command == '.':
            output += chr(arr[arr_pos])
        elif command == ',':
            arr[arr_pos] = ord(input[in_pos])
            in_pos += 1
        elif command == '[':
            if arr[arr_pos] == 0:
                count = 0
                while command_pos < len(code):
                    command_pos += 1
                    command = code[command_pos]
                    if command == '[':
                        count += 1
                    elif command == ']':
                        if count == 0:
                            break
                        else:
                            count -= 1
        elif command == ']':
            if not arr[arr_pos] == 0:
                count = 0
                while command_pos >= 0:
                    command_pos -= 1
                    command = code[command_pos]
                    if command == ']':
                        count += 1
                    elif command == '[':
                        if count == 0:
                            break
                        else:
                            count -= 1
        command_pos += 1
    return output

print((brain_luck(",+[-.,+]", "Codewars" + chr(255))))