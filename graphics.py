import pyglet


class Graphics:
    batches = [pyglet.graphics.Batch()]
    objects = [[]]

    @classmethod
    def draw(cls):
        for i_layer in range(max(len(cls.batches), len(cls.objects))):
            if len(cls.batches) > i_layer:
                cls.batches[i_layer].draw()
            if len(cls.objects) > i_layer:
                for obj in cls.objects[i_layer]:
                    obj.draw()

    @classmethod
    def clear(cls):
        cls.batches = [pyglet.graphics.Batch()]
        cls.objects = [[]]

    @classmethod
    def add_batch_layer(cls, layer):
        existing_layers = len(cls.batches)
        if layer - existing_layers >= 0:
            for i in range(layer - existing_layers + 1):
                cls.batches.append(pyglet.graphics.Batch())

    @classmethod
    def add_obj_layer(cls, layer):
        existing_layers = len(cls.objects)
        if layer - existing_layers >= 0:
            for i in range(layer - existing_layers + 1):
                cls.objects.append([])

    @classmethod
    def rect(cls, x: float, y: float, width: float, height: float, color: tuple = (0, 0, 0), layer: int = 0):
        if len(cls.batches) - 1 < layer:
            cls.add_batch_layer(layer)
        return cls.batches[layer].add(4, pyglet.gl.GL_QUADS, None,
                                      ("v2f", (x, y,
                                               x + width, y,
                                               x + width, y + height,
                                               x, y + height)),
                                      ("c3B", color * 4))

    @classmethod
    def tri(cls, x: float, y: float, x2: float, y2: float, x3: float, y3: float, color: tuple = (0, 0, 0),
            layer: int = 0):
        if len(cls.batches) - 1 < layer:
            cls.add_batch_layer(layer)
        return cls.batches[layer].add(3, pyglet.gl.GL_TRIANGLES, None,
                                      ("v2f", (x, y,
                                               x2, y2,
                                               x3, y3)),
                                      ("c3B", color * 3))

    @classmethod
    def text(cls, text: str, x: float, y: float, font_size=12, bold=False, italic=False, color=(255, 255, 255, 255),
             layer: int = 0):
        label = pyglet.text.Label(text=text, x=x, y=y, font_size=font_size, bold=bold, italic=italic, color=color,
                                  anchor_x='center', anchor_y='center')
        if len(cls.objects) - 1 < layer:
            cls.add_obj_layer(layer)
        cls.objects[layer].append(label)
        return label

    @classmethod
    def sprite(cls, source: str, x: float, y: float, centered=True, layer: int = 0):
        img = pyglet.sprite.Sprite(pyglet.image.load(source), x, y)
        if centered:
            img.x -= img.width / 2
            img.y -= img.height / 2
        if len(cls.objects) - 1 < layer:
            cls.add_obj_layer(layer)
        cls.objects[layer].append(img)
        return img


if __name__ == "__main__":
    pass
