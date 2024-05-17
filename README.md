# Offer Man

**Version:** 0.1 Alpha  
**Release Date:** May 17, 2024  
**Author:** Albert Bozesan

---

## Introduction

This is Offer Man, a simple Llama3-8B-based project designed to help voiceover artists quickly decide on a rate to offer clients. This is an initial alpha release, version 0.1, which runs in Terminal on Mac.

## Installation

The following things must be installed to run Offer Man:
- [Python3](https://docs.python-guide.org/starting/install3/osx/)
- [Ollama](https://github.com/ollama/ollama/tree/main) with the Llama3 8B parameter model.

## Running Offer Man

1. Place your rates in a file named `voiceover_rates.csv` in the same directory as `offerman.py`.

2. Simply run `offerman.py` in your Terminal with this command:
    ```bash
    python3 path/to/offerman.py
    ```
## Adjusting Offer Man to Your Needs

There are two ways to adjust Offer Man's behavior: the model and the prompt.

Adjusting the Modelfile will fundamentally change what the LLM thinks of itself. This is good for adjusting its general relationship with you—if you're not a voiceover artist, for example.

In offerman.py on line 24, you can find the prompt that the LLM receives after being given the CSV. This is a good place to adjust what it outputs. Don't like that it gives you a suggestion of what to send your client? Change that here!

## Troubleshooting

- Make sure you have installed Ollama correctly. Check if it runs normally before attempting to run Offer Man.
- If you continue to get errors, check if your `voiceover_rates.csv` and the Model file are in the same directory as `offerman.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
