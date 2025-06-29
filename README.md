# Disease Information Chatbot

This project is a command-line-based chatbot that provides helpful first-aid information for various common diseases and injuries. The chatbot utilizes a structured CSV file as its knowledge base to respond with relevant FAQs and solutions.

---

## 📁 Project Structure

```
├── Chatbot.ipynb           # Main notebook with chatbot logic
├── diseases.csv           # Dataset containing disease tags and responses
└── README.md               # Project documentation
```

---

## 💡 Features

* Interactive chatbot interface on the command line.
* Handles user queries related to common health conditions like **cuts**, **fever**, **headache**, etc.
* Displays a list of known issues when an unknown query is entered.
* Provides pre-written solutions and FAQs from a CSV dataset.

---

## 🛠️ How It Works

1. **Load Dataset**
   The chatbot reads the file `diseases.csv`, which contains:

   * Disease tags
   * A list of patterns (questions)
   * Suggested first-aid responses

2. **User Interaction**
   The chatbot prompts the user to ask about a disease and responds accordingly. If the disease is not found, it prints a list of known tags.

3. **Looping Mechanism**
   The program runs continuously until the user types `exit`.

---

## 📊 Sample Output

```
Bot: Ask about a disease(or type 'exit' to quit): cuts

User: cuts

**Cuts**:
- bot: What to do if Cuts?
- bot: How to cure Cuts?
- bot: Which medicine to apply for Cuts?
- bot: what to apply on cuts?
- bot: Cuts

- Solution-: Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2 minutes until bleeding stops
```

---

## 🤝 Technologies Used

* Python
* Pandas
* CSV File Handling

---

## 📚 Dataset Format (`diseases(1).csv`)

| tag  | patterns\_\_001   | patterns\_\_002 | ... | responses\_\_-                             |
| ---- | ----------------- | --------------- | --- | ------------------------------------------ |
| cuts | What to do if...? | How to cure...? | ... | Wash the cut properly and stop bleeding... |

---

## 🚀 Getting Started

1. Clone this repository.
2. Ensure `diseases.csv` is in the same directory.
3. Open `Chatbot.ipynb` in Jupyter or Colab.
4. Run all cells to start interacting with the chatbot.

---

## 💼 Use Cases

* First-aid assistant
* Basic health education chatbot
* FAQ bot for common medical situations

---

## ⚠️ Notes

* The word "deases" is misspelled and should be "diseases" in future improvements.
* Replace `NaN` values in CSV with appropriate alternatives for better responses.

---

## 🎉 Future Improvements

* Add natural language processing for more flexible queries.
* Build a web-based UI.
* Include voice interaction features.
