import easygui
path = easygui.fileopenbox()


from PIL import Image
filename = path



with Image.open(filename) as img:
    img.load()


    #def change_color(im):
    new_img_data = []
    # цвета из MakeCode Arcade (RGB)
    # 1 - (255,255,255) - белый
    # 2 - (255,33,33) - красный
    # 3 - (255,147,196) - розовый
    # 4 - (255,129,53) - оранжевый
    # 5 - (255,246,9) - желтый
    # 6 - (36,156,163) - тот самый непонятный , бирюзовый
    # 7 - (120,220,82) - салатовый
    # 8 - (0,63,173) - синий
    # 9 - (135,242,255) - голубой
    # a - (142,46,196) - фиолетовый(фуксия)
    # b - (164,131,159) - какой-то фиолетовый
    # c - (92,64,108) - грязно-фиолетовый
    # d - (229,205,196) - бежевый
    # e - (145,70,61) - коричневый
    # f - (0,0,0) - чёрный
    color_img_1 = (255, 255, 255)
    color_img_2 = (255, 33, 33)
    color_img_3 = (255, 147, 196)
    color_img_4 = (255, 129, 53)
    color_img_5 = (255, 246, 9)
    color_img_6 = (36, 156, 163)
    color_img_7 = (120, 220, 82)
    color_img_8 = (0, 63, 173)
    color_img_9 = (135, 242, 255)
    color_img_a = (142, 46, 196)
    color_img_b = (164, 131, 159)
    color_img_c = (92, 64, 108)
    color_img_d = (229, 205, 196)
    color_img_e = (145, 70, 61)
    color_img_f = (0, 0, 0)

    for i in img.getdata():
        R = round((i[0]+1)/32)
        G = round((i[1]+1)/32)
        B = round((i[2]+1)/32)

        if R == 8:
            if G == 8:
                if B > 6:
                    new_img_data.append(color_img_1)
                else:
                    new_img_data.append(color_img_5)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_d)
                else:
                    new_img_data.append(color_img_5)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_d)
                else:
                    new_img_data.append(color_img_4)
            elif G == 5:
                if B >= 6:
                    new_img_data.append(color_img_3)
                else:
                    new_img_data.append(color_img_4)
            elif G == 4:
                if B >= 6:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_4)
            elif G == 3:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 2:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 1:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 0:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
        elif R == 7:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_5)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_b)
                else:
                    new_img_data.append(color_img_5)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_d)
                else:
                    new_img_data.append(color_img_5)
            elif G == 5:
                if B >= 6:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_4)
            elif G == 4:
                if B >= 6:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_4)
            elif G == 3:
                if B >= 6:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 2:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 1:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 0:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
        elif R == 6:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_5)
            elif G == 5:
                if B >= 6:
                    new_img_data.append(color_img_b)
                else:
                    new_img_data.append(color_img_e)
            elif G == 4:
                if B >= 5:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_e)
            elif G == 3:
                if B >= 5:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_e)
            elif G == 2:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 1:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 0:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
        elif R == 5:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 5:
                if B >= 5:
                    new_img_data.append(color_img_b)
                else:
                    new_img_data.append(color_img_e)
            elif G == 4:
                if B >= 5:
                    new_img_data.append(color_img_b)
                else:
                    new_img_data.append(color_img_d)
            elif G == 3:
                if B >= 5:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_e)
            elif G == 3:
                if B >= 5:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_e)
            elif G == 2:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_e)
            elif G == 1:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 0:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
        elif R == 4:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 5:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_e)
            elif G == 4:
                if B >= 4:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_b)
            elif G == 3:
                if B >= 4:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_b)
            elif G == 2:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_e)
            elif G == 1:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
            elif G == 0:
                if B >= 3:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_2)
        elif R == 3:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 5:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 4:
                if B >= 6:
                    new_img_data.append(color_img_c)
                else:
                    new_img_data.append(color_img_6)
            elif G == 3:
                if B >= 4:
                    new_img_data.append(color_img_a)
                else:
                    new_img_data.append(color_img_c)
            elif G == 2:
                if B >= 4:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_c)
            elif G == 1:
                if B >= 2:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_e)
            elif G == 0:
                if B >= 2:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_e)
        elif R == 2:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 5:
                if B >= 4:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 4:
                if B >= 4:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 3:
                if B >= 3:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_6)
            elif G == 2:
                if B >= 3:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_e)
            elif G == 1:
                if B >= 3:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_c)
            elif G == 0:
                if B >= 3:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_c)
        elif R == 1:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 5:
                if B >= 4:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 4:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 3:
                if B >= 4:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_7)
            elif G == 2:
                if B >= 2:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_c)
            elif G == 1:
                if B >= 2:
                    new_img_data.append(color_img_c)
                else:
                    new_img_data.append(color_img_7)
            elif G == 0:
                if B >= 2:
                    new_img_data.append(color_img_c)
                else:
                    new_img_data.append(color_img_7)
        elif R == 0:
            if G == 8:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 7:
                if B >= 6:
                    new_img_data.append(color_img_9)
                else:
                    new_img_data.append(color_img_7)
            elif G == 6:
                if B >= 6:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 5:
                if B >= 4:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 4:
                if B >= 4:
                    new_img_data.append(color_img_6)
                else:
                    new_img_data.append(color_img_7)
            elif G == 3:
                if B >= 4:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_7)
            elif G == 2:
                if B >= 2:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_6)
            elif G == 1:
                if B >= 2:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_a)
            elif G == 0:
                if B >= 2:
                    new_img_data.append(color_img_8)
                else:
                    new_img_data.append(color_img_f)


    recolor_new_image = Image.new(img.mode, img.size)
    recolor_new_image.putdata(new_img_data)
    #return recolor_new_image

    recolor_new_image.show()
    #фиксируем ширину получаемой картинки
    fixed_width = 160
    #получаем высоту и ширину
    h, w = recolor_new_image.size
    #получаем процент сжатия относительно ширины
    width_percent = (fixed_width / w)
    #применяем процент сжатия к высоте
    height_size = int((h * float(width_percent)))
    new_img = recolor_new_image.resize((fixed_width, height_size))




    # показать итоговую картинку
    new_img.show()


