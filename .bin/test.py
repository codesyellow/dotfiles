#!/home/digo/.bin/.venv/bin/python

from gi.repository import Gdk, GObject, Gtk, Gio, GLib

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')


class HeaderBarWindow(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title='HeaderBar Example')

        self.set_default_size(600, 600)

        header_bar = Gtk.HeaderBar()
        self.set_titlebar(header_bar)

        button = Gtk.Button(label='Button')
        header_bar.pack_start(button)

        icon_button = Gtk.Button(icon_name='open-menu-symbolic')
        header_bar.pack_end(icon_button)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_child(scrolled)

        flowbox = Gtk.FlowBox()
        flowbox.props.valign = Gtk.Align.START
        flowbox.props.max_children_per_line = 3
        flowbox.props.selection_mode = Gtk.SelectionMode.NONE
        scrolled.set_child(flowbox)

#        self.create_flowbox(flowbox)

        self.name = 'oi'
        self.picture = Gtk.Image.new_from_file(
            '/home/digo/.wallpapers/ign_robots.png')
        picture2 = Gtk.Image.new_from_file(
            '/home/digo/.wallpapers/ign_unsplash21.png')
        picture3 = Gtk.Image.new_from_file(
            '/home/digo/.wallpapers/ign_unsplash32.png')

        self.picture.set_pixel_size(200)
        picture2.set_pixel_size(200)
        picture3.set_pixel_size(200)
        flowbox.append(self.picture)
        flowbox.append(picture2)
        flowbox.append(picture3)

        drag_controller = Gtk.DragSource()
        drag_controller.connect('prepare', self.on_drag_prepare)
        drag_controller.connect('drag-begin', self.on_drag_begin)
        self.add_controller(drag_controller)

    def on_drag_prepare(self, _ctrl, _x, _y):
        file = Gio.File.new_for_path('/home/digo/.wallpapers/ign_robots.png')
        file_provider = Gdk.ContentProvider.new_for_value(file)

        try:
            # Load the file data
            data, _ = file.load_bytes(None)

            # Create GLib.Bytes from the data
            gbytes = GLib.Bytes.new(data)

            # Create content provider for the image data
            bytes_provider = Gdk.ContentProvider.new_for_bytes(
                'image/png',  # MIME type
                gbytes
            )

            # Combine both providers
            union_provider = Gdk.ContentProvider.new_union(
                [file_provider, bytes_provider])
            return union_provider

        except Exception as e:
            print(f"Error loading file: {e}")
            # Fall back to just the file provider
            return file_provider

    def on_drag_begin(self, ctrl, _drag):
        icon = Gtk.WidgetPaintable.new(self.picture)
        ctrl.set_icon(icon, 0, 0)


def on_activate(app):
    # Create window
    win = HeaderBarWindow(application=app)
    win.present()


app = Gtk.Application(application_id='com.example.App')
app.connect('activate', on_activate)

app.run(None)
