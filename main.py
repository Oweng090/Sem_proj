import flet as ft
import random

# --- Core Logic: Drawing the Dice Face on a Flet Canvas ---

def draw_dice_face(number: int, size: int = 150, dice_color: str = ft.Colors.BLUE_700, pip_color: str = ft.Colors.LIME_ACCENT_400):
    """
    Returns a Flet Canvas control representing a single face of a dice.
    This replaces the Tkinter Canvas drawing logic.
    """
    half = size / 2
    qtr = size / 4
    tqtr = size * 3 / 4
    pip_radius = size / 15  # Adjust size of pips relative to dice size

    # Define the coordinates for the 7 possible pip locations (center and corners)
    pips = {
        # (x, y) coordinates for the center of the pip
        'center': (half, half),
        'top_left': (qtr, qtr),
        'top_right': (tqtr, qtr),
        'bottom_left': (qtr, tqtr),
        'bottom_right': (tqtr, tqtr),
        'mid_left': (qtr, half),
        'mid_right': (tqtr, half),
    }
    
    # Map dice number to the required pip locations
    pip_map = {
        1: ['center'],
        2: ['top_left', 'bottom_right'],
        3: ['top_left', 'center', 'bottom_right'],
        4: ['top_left', 'top_right', 'bottom_left', 'bottom_right'],
        5: ['top_left', 'top_right', 'center', 'bottom_left', 'bottom_right'],
        6: ['top_left', 'top_right', 'bottom_left', 'bottom_right', 'mid_left', 'mid_right'],
    }

    # Base dice rectangle
    shapes = [
        ft.canvas.Rect(
            0, 0, size, size,
            paint=ft.Paint(
                style=ft.PaintingStyle.FILL,
                color=dice_color,
            ),
            border_radius=15 # Gives the dice a slightly rounded appearance
        )
    ]

    # Draw pips based on the number
    pip_fill = ft.Paint(style=ft.PaintingStyle.FILL, color=pip_color)
    for pip_key in pip_map.get(number, []):
        x, y = pips[pip_key]
        shapes.append(ft.canvas.Circle(x, y, pip_radius, paint=pip_fill))
    
    return ft.Container(
        content=ft.canvas.Canvas(
            shapes,
            width=size,
            height=size,
        ),
        # Add a border to mimic the original Tkinter highlight
        border=ft.border.all(2.5, ft.colors.LIME_ACCENT_400),
    )


# --- Flet Application Main Function ---

def main(page: ft.Page):
    page.title = "Flet Dice Roller"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    
    # State variables for the app
    dice_1_result = 1
    dice_2_result = 1
    is_two_sets_mode = False
    
    # Controls that need to be updated
    roll_zone_1 = draw_dice_face(dice_1_result)
    roll_zone_2 = draw_dice_face(dice_2_result)
    total_text_1 = ft.Text(f"Total: {dice_1_result}", size=18)
    total_text_2 = ft.Text(f"Total: {dice_2_result}", size=18, visible=False)
    
    # Dice containers for layout and visibility control
    dice_container_1 = ft.Column([roll_zone_1, total_text_1], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    dice_container_2 = ft.Column([roll_zone_2, total_text_2], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    
    # Colors for themes
    THEME_1 = {"bg": ft.colors.BLUE_GREY_900, "dice": ft.colors.RED_700, "pip": ft.colors.YELLOW_ACCENT_400, "highlight": ft.colors.RED_900}
    THEME_2 = {"bg": ft.colors.GREY_500, "dice": ft.colors.BLUE_700, "pip": ft.colors.LIME_ACCENT_400, "highlight": ft.colors.BLACK}
    current_theme = THEME_1

    # --- Event Handlers ---

    def roll_dice_sets(e):
        nonlocal dice_1_result, dice_2_result
        
        # Roll Dice 1
        dice_1_result = random.randint(1, 6)
        
        # Update Canvas 1 with new result
        dice_container_1.controls[0] = draw_dice_face(
            dice_1_result,
            dice_color=current_theme["dice"],
            pip_color=current_theme["pip"],
            size=150
        )
        total_text_1.value = f"Total: {dice_1_result}"
        
        # Roll Dice 2 if in two-set mode
        if is_two_sets_mode:
            dice_2_result = random.randint(1, 6)
            
            # Update Canvas 2 with new result
            dice_container_2.controls[0] = draw_dice_face(
                dice_2_result,
                dice_color=current_theme["dice"],
                pip_color=current_theme["pip"],
                size=150
            )
            total_text_2.value = f"Total: {dice_2_result}"
            
        page.update()

    def set_theme(theme_data):
        nonlocal current_theme
        current_theme = theme_data
        
        # Update page background
        page.bgcolor = current_theme["bg"]
        
        # Update controls
        # The main title text's background is often transparent in Flet, so we just change the color.
        main_title.color = ft.colors.WHITE if theme_data == THEME_1 else ft.colors.BLACK
        set_label.color = ft.colors.WHITE if theme_data == THEME_1 else ft.colors.BLACK
        
        # Re-draw dice with new colors (must re-create the canvas object)
        dice_container_1.controls[0] = draw_dice_face(
            dice_1_result,
            dice_color=current_theme["dice"],
            pip_color=current_theme["pip"],
            size=150
        )
        dice_container_2.controls[0] = draw_dice_face(
            dice_2_result,
            dice_color=current_theme["dice"],
            pip_color=current_theme["pip"],
            size=150
        )
        
        # Update the border color of the canvas containers
        for container in [dice_container_1.content, dice_container_2.content]:
             # container.content is the Canvas, we are targeting the parent Container
             container.border = ft.border.all(2.5, current_theme["highlight"])


        page.update()

    def toggle_set_mode(e):
        nonlocal is_two_sets_mode
        
        # Toggle mode based on which button was pressed
        if e.control.text == "One Set":
            is_two_sets_mode = False
            dice_container_2.visible = False
            page.window_width = 400
        else:
            is_two_sets_mode = True
            dice_container_2.visible = True
            page.window_width = 800

        page.update()

    # --- Initial UI Setup (equivalent to `root` setup) ---
    
    set_theme(THEME_1) # Apply initial theme

    main_title = ft.Text("Flet Dice Roller!", size=30, weight=ft.FontWeight.BOLD)
    set_label = ft.Text("More Sets?", size=18)
    
    # Layout the controls
    page.add(
        main_title,
        ft.Row(
            [
                dice_container_1,
                dice_container_2, # Hidden initially
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        ),
        ft.Container(height=30), # Spacer
        ft.ElevatedButton(
            "Roll Dice!",
            on_click=roll_dice_sets,
            icon=ft.icons.CASINO,
            bgcolor=ft.colors.GREEN_ACCENT_400,
            color=ft.colors.BLACK,
        ),
        ft.Container(height=20), # Spacer
        ft.Row(
            [
                ft.ElevatedButton("Theme 1", on_click=lambda e: set_theme(THEME_1), bgcolor=ft.colors.RED_900, color=ft.colors.WHITE),
                ft.ElevatedButton("Theme 2", on_click=lambda e: set_theme(THEME_2), bgcolor=ft.colors.GREY_700, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(height=30), # Spacer
        ft.Column(
            [
                set_label,
                ft.ElevatedButton("One Set", on_click=toggle_set_mode, icon=ft.icons.FILTER_1),
                ft.ElevatedButton("Two Sets", on_click=toggle_set_mode, icon=ft.icons.FILTER_2),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# --- Flet Build Command ---

if __name__ == "__main__":
    # The default view opens a desktop window or a web page
    # To run as a test: ft.app(target=main)
    # The line below ensures that the app runs embedded inside a single window/page
    ft.app(target=main)