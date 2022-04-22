"""Define main menu."""
import inquirer

mainMenu = [
    inquirer.List(
        "mainMenu",
        message="Main Menu",
        choices=[
            "Interval Training (ascending)",
            "Interval Training (descending)",
            "Interval Training (ascending and descending)",
            "Quit",
        ],
    )
]
