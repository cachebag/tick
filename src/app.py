# app.py
from textual.app import App
from views.home import HomeScreen
from textual.binding import Binding
from textual.widgets import Button

class ProductivityApp(App):
    CSS_PATH = "theme.css"
    SCREENS = {"home": HomeScreen}
    TITLE = "TICK"
    
    # Define keyboard bindings for the entire application
    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("up", "focus_previous", "Move Up", show=True),
        Binding("down", "focus_next", "Move Down", show=True),
        Binding("enter", "select_item", "Select", show=True),
    ]
    
    def on_mount(self) -> None:
        self.push_screen("home")
        self.disable_mouse()  

    def on_screen_resume(self) -> None:
        try:
            first_menu_item = self.screen.query_one("MenuItem")
            if first_menu_item:
                first_menu_item.focus()
        except Exception:
            pass

    def disable_mouse(self) -> None:
        for widget in self.query("*"):
            if hasattr(widget, "can_focus"):
                widget.can_focus = False
            if hasattr(widget, "show_cursor"):
                widget.show_cursor = False

    def action_focus_next(self) -> None:
        current = self.focused
        menu_items = list(self.screen.query("MenuItem"))
        if menu_items and current in menu_items:
            index = menu_items.index(current)
            next_index = (index + 1) % len(menu_items)
            menu_items[next_index].focus()

    def action_focus_previous(self) -> None:
        current = self.focused
        menu_items = list(self.screen.query("MenuItem"))
        if menu_items and current in menu_items:
            index = menu_items.index(current)
            prev_index = (index - 1) % len(menu_items)
            menu_items[prev_index].focus()

    def action_select_item(self) -> None:
        if self.focused and isinstance(self.focused, Button):
            self.focused.press()

if __name__ == "__main__":
    app = ProductivityApp()
    app.run()
