from win10toast import ToastNotifier

toaster = ToastNotifier()


def start():
    toaster.show_toast("Screen Recorder",
                       "Yay! Your recording has been started...",
                       icon_path="./logo.ico",
                       duration=1)


def filesaved_path(fs_path):
    toaster.show_toast("Screen Recorder",
                       "Yay! Your file has been saved in " + fs_path,
                       icon_path="./logo.ico",
                       duration=2)


def stop():
    toaster.show_toast("Screen Recorder",
                       "Yay! Your recording has been ended...",
                       icon_path="./logo.ico",
                       duration=1)


def KeyboardInterruptted():
    toaster.show_toast("Screen Recorder",
                       "User clicked Ctrl+C to interrupt, Your recording has been ended...",
                       icon_path="./logo.ico",
                       duration=1)
