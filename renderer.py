import verovio, os
from cairosvg import svg2png
from data import Data
from PIL import Image, ImageOps

class Renderer:

    def renderScoreWithOtherFont(path):
        os.system(f"verovio -r verovio/data --handwritten-font petaluma --font petaluma {path}")
        

    def renderScore(path, output):
        width = Renderer.krnToSvg(path, output)
        Renderer.svgtopng(output, "example.png", width)

    def countLines(path):
            
        with open(path, 'r') as fp:
            n_lines = len(fp.readlines())
        return n_lines

    def krnToSvg(path, output):
        tk = verovio.toolkit()
        # if multivoice
        #options = { "pageHeight": 400, "pageWidth": 2100 }
        # if solo voice

        n_lines = Renderer.countLines(path)
        width = n_lines * 35
        # if width > 3000:
        #     width = width - (width//5)
        #     options = { "pageWidth": width , "scale": 65 }
        # else:
        if width < 2100:
            width = 2100
        #options = { "pageWidth": width, 'font': 'bravura', 'smuflTextFont': 'bravura' }
        options = {"pageWidth": width}

        tk.setOptions(options)
        tk.loadFile(path)
        tk.getPageCount()
        tk.renderToSVGFile(output, 1)
        return width

    def svgtopng(input, output, width):
        # Código maría
        # with open(input, mode="r") as input_file:
        #         svg_stream = input_file.read()
        #         # See https://github.com/Kozea/CairoSVG/issues/300 for the reason why we have to replace inherit with visible here
        #         svg_stream = svg_stream.replace("overflow=\"inherit\"", "overflow=\"visible\"")
        #         svg2png(bytestring=svg_stream, background_color="transparent", write_to=output)

        with open(input, mode="r") as input_file:
            svg_stream = input_file.read()
            
            svg_stream = svg_stream.replace("overflow=\"inherit\"", "overflow=\"visible\"")
            #svg2png(bytestring=svg_stream, background_color="transparent", write_to=output)
            svg2png(bytestring=svg_stream, background_color="white", write_to=output)

            img = Image.open(output)
            # First we crop to 300 because of the watermark of verovio engraving in the page's bottom
            img = img.crop((0, 0,width,300))
            img = ImageOps.invert(img)
            area = img.getbbox()
            img = img.crop(area)
            img = ImageOps.invert(img)
            img.save(output)

            # change background and crop with the img.getbbox coordinates
            if Data.change_background:
                other_bg_output = "pruebaFondo.png"
                Data.change_color()
                svg2png(bytestring=svg_stream, background_color=Data.bg_color, write_to=other_bg_output)
                img = Image.open(other_bg_output)
                img = img.crop(area)
                img.save(other_bg_output)


if __name__ == "__main__":
    Renderer.svgtopng()