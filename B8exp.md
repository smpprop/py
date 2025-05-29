
# Batsman Score Tracker (2017–2020)

This Python application is a simple GUI tool for inputting, saving, and visualizing cricket batsmen's scores from 2017 to 2020.

## Technologies Used

- `tkinter` – for creating the GUI
- `pandas` – for reading and manipulating the CSV file
- `matplotlib` – for plotting the data

## Features

- Input batsman name and yearly scores
- Save entries to `batsman.csv`
- Plot a bar chart of scores
- Reset input fields after saving

---

## Functions

### `add()`
- Retrieves input from GUI fields
- Appends batsman's name and scores to `batsman.csv`
- Shows a confirmation dialog
- Clears the input fields

### `showplot()`
- Reads the `batsman.csv` into a DataFrame
- Displays a bar chart of scores
- Clears the CSV file after plotting (Note: leads to data loss)

---

## GUI Layout

| Field      | Description            |
|------------|------------------------|
| Batsman    | Name of the batsman    |
| 2017-2020  | Score for each year    |

Two buttons are available:
- **Add**: Save data
- **Plot**: Show score chart

---

## Suggested Improvements

- **Data Loss Warning**: `showplot()` clears data after plotting. Remove or modify for persistent storage.
- **Validation**: Add input validation for empty fields and score types.
- **CSV Format**: Use commas between scores for proper formatting.

---

## Author

Created for educational purposes.
