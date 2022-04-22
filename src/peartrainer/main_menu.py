"""Define main menu."""
import inquirer

menuChoices = [
    "Interval Training (ascending)",
    "Interval Training (descending)",
    "Interval Training (ascending and descending)",
    "Quit",
]

mainMenu = [
    inquirer.List(
        "mainMenu",
        message="Main Menu",
        choices=menuChoices,
    )
]
