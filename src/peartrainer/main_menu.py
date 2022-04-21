"""Define main menu."""
import inquirer

mainMenu = [
    inquirer.List(
        "mainMenu",
        message="Main Menu",
        choices=[
            "Interval Training played upwards",
            "Interval Training played downwards",
            "Interval Training played up- and downwards",
            "Quit",
        ],
    )
]
