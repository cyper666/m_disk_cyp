from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter


def gen_cover(filename, msg_id):
    
    try:
        fg = f"res/FG.png"
        bg = filename

        fgr = Image.open(fg).convert("RGBA")
        background = Image.open(bg).convert("RGBA")
        background = background.resize((fgr.width, fgr.height))
        background = background.filter(ImageFilter.GaussianBlur(10))
        width = (background.width - fgr.width) // 2
        height = (background.height - fgr.height) // 2
        background.paste(fgr, (width, height), fgr)
        Image.alpha_composite(fgr, background).save(f"final{msg_id}.png", format="png")
        final = f"final{msg_id}.png"
        return final
    except Exception:
        print("gen cover failed")
        
    