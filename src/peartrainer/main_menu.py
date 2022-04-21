"""Define main menu."""
import inquirer

mainMenu = [
    inquirer.List(
        'mainMenu',
        message="Main Menu",
        choices=["Interval Training", "Quit"],
    )
]
