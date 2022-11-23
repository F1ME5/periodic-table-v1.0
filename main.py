# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

#Project Modules
import window
from window import root

#implementar show info

def main():
    window.main_window_settings()
    window.elements_buttons_creation()
    window.elements_labels_settings()
    window.element_info_labels_settings()

    root.mainloop()

if __name__ == "__main__":
    main()