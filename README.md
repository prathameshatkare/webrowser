

---

# PyQt5 Web Browser

This is a simple web browser application built using Python's PyQt5 framework. The application includes basic functionalities like navigating forward and backward, reloading pages, and manually entering URLs via a navigation bar.

## Features

- **Back**: Navigate to the previous webpage.
- **Forward**: Move to the next webpage.
- **Reload**: Refresh the current webpage.
- **Home**: Navigate to the home page (Google in this case).
- **URL Bar**: Enter a web address and press `Enter` to navigate.

## Dependencies

To run this project, you will need the following Python libraries installed:

- `PyQt5`
- `PyQtWebEngine`

You can install these using pip:

```bash
pip install PyQt5 PyQtWebEngine
```

## How to Run

1. Clone this repository or download the script file.
2. Ensure all dependencies are installed.
3. Run the Python script:

```bash
python your_script_name.py
```

## Project Structure

```bash
.
├── main.py          # Main file containing the web browser application code
└── README.md        # Project documentation
```

## Customization

- **Home Page**: The default home page is set to Google (`https://google.com`). You can change this by modifying the `NavigateHome()` method.
  
- **Browser Window Size**: The browser window is maximized by default. You can modify this behavior by changing `self.showMaximized()` to other window size methods (e.g., `self.show()` for normal size).

## Future Improvements

- Add bookmarking functionality.
- Implement tabbed browsing.
- Include history management.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---
