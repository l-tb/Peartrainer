"""Define main menu."""
import inquirer

menuChoices = [
    "Interval Training (ascending)",
    "Interval Training (descending)",
    "Interval Training (ascending and descending)",
    "Interval Training (harmonic)",
    "Quit",
]

mainMenu = [
    inquirer.List(
        "mainMenu",
        message="Main Menu",
        choices=menuChoices,
    )
]
